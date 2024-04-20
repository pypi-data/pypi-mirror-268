# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.

import sys
from typing import Iterable, Tuple

import contextlib
import uuid
import os
import papermill as pm
import asyncio
import traceback
from threading import Thread, Lock
from contextlib import redirect_stdout, redirect_stderr
from google.protobuf.any_pb2 import Any
import multiprocessing as mp
import queue

from . import logger
from .hub_helper import _clear_hub_user_access
from .redirects import RedirectStdOut, RedirectStdErr
from .pycoderunner_pb2 import RunWellKnownWorkflowResponse


class Notebook():
    def __init__(self, notebook_filepath: str, working_path: str):
        self._notebook_filepath = notebook_filepath
        self._working_path = working_path
        self._lock = Lock()
        self._valid = False
        self._error_message = None
        self._injected_vars = None
        self._script_complete_event = mp.Event()
        self._output_q_complete_event = None

        if notebook_filepath is None or len(notebook_filepath) == 0 or str.isspace(notebook_filepath):
            self._error_message = "notebook_filepath must not be None, empty or whitespace"
            return

        if not os.path.exists(notebook_filepath):
            self._error_message = f'Specified notebook_filepath not valid: {notebook_filepath}'
            return

        if working_path is None or len(working_path) == 0 or str.isspace(working_path):
            self._error_message = "working_path must not be None, empty or whitespace"
            return

        if not os.path.exists(working_path):
            self._error_message = f'Specified working_path not valid: {working_path}'
            return

        self._valid = True

    @property
    def is_valid(self) -> bool:
        return self._valid

    @property
    def is_complete(self) -> bool:
        with self._lock:
            return self._script_complete_event.is_set()

    @property
    def is_error(self) -> bool:
        with self._lock:
            return self._error_message is not None

    @property
    def error_message(self) -> str:
        with self._lock:
            return self._error_message

    def _reset(self):
        with self._lock:
            self._error_message = None
            self._injected_vars = None
            self._script_complete_event.clear()
            self._output_q_complete_event = None

    def _set_complete(self, error_message:str = None):
        with self._lock:
            self._error_message = error_message
            self._script_complete_event.set()

    def _run(self):
        try:
            if not self._valid:
                self._set_complete("Notebook not valid")
                return

            try:
                if os.name == 'nt':
                    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
            except:
                None

            unique_id = uuid.uuid1()

            working_path = os.path.dirname(os.path.abspath(self._notebook_filepath))
            output_path = os.path.join(self._working_path, f'out_{unique_id}.ipynb')
            logger.debug(f"Running notebook: {self._notebook_filepath}")
            logger.debug(f"Working dir: {working_path}")
            logger.debug(f"Output file: {output_path}")
            logger.debug(f"Parameters: {self._injected_vars}")

            with pm.execute.chdir(working_path):
                pm.execute_notebook(
                    input_path=self._notebook_filepath,
                    output_path=output_path,
                    parameters=self._injected_vars,
                    log_output=True,
                    stdout_file=sys.stdout,
                    stderr_file=sys.stderr
                )

            with contextlib.suppress(FileNotFoundError):
                os.remove(output_path)

            self._script_complete_event.set()
            if self._output_q_complete_event:
                self._output_q_complete_event.wait()

            logger.debug("Notebook completed")

        except Exception as error:
            error_message = f"Exception running notebook: {error}: {error.args}\n{traceback.format_exc()}"
            logger.error(error_message)
            self._set_complete(error_message)

    def _run_in_new_thread(self) -> None:
        thread = Thread(target=self._run)
        logger.debug(f"Starting _run")
        thread.start()

    def run_capture_outputs(self, parameters) -> Iterable[Tuple[bool, bool, Any, str]]:
        self._reset()
        try:
            response_q = mp.Queue()
            with redirect_stdout(RedirectStdOut(response_q)):
                with redirect_stderr(RedirectStdErr(response_q)):
                    self._injected_vars = parameters
                    self._run_in_new_thread()
                    for response in self._process_output(response_q):
                        yield response
        finally:
            if self.is_complete:
                if self.is_error:
                    yield (False, True, None, self._error_message)
                else:
                    yield (True, True, None, None)
            else:
                yield (False, True, None, "Notebook did not run to completion")
            _clear_hub_user_access()

    def _process_output(self, q: mp.Queue):
        if not self._output_q_complete_event:
            self._output_q_complete_event = mp.Event()

        try:
            while True:
                try:
                    tuple = q.get(block=True, timeout=1)
                    response = RunWellKnownWorkflowResponse()
                    if tuple[0] == "out":
                        response.std_out = tuple[1]
                    elif tuple[0] == "err":
                        if self._is_papermill_progress(tuple[1]):
                            response.std_out = tuple[1]
                        elif self._is_parameter_cell_missing(tuple[1]):
                            response.std_out = "Warning: " + tuple[1]
                        else:
                            response.std_err = tuple[1]
                    yield (True, False, response, None)
                except queue.Empty:
                    if self._script_complete_event.is_set():
                        break
                except Exception as error:
                    logger.error(f"q: {error} {error.args}")
                logger.debug(f"_process_output complete")
        except Exception as error:
            logger.error(f"_process_output: {error} {error.args}")
        finally:
            self._output_q_complete_event.set()

    def _is_papermill_progress(self, line: str) -> bool:
        stripped_line = line.strip()
        return stripped_line.startswith("Executing:") and (stripped_line.endswith("cell/s]") or stripped_line.endswith("/cell]"))

    def _is_parameter_cell_missing(self, line: str) -> bool:
        stripped_line = line.strip()
        return stripped_line.startswith("Input notebook does not contain a cell with tag 'parameters'")
