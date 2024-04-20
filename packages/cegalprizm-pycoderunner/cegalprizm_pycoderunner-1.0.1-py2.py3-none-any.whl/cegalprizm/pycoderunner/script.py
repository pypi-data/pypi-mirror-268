# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.

from typing import Callable, Dict, Iterable, List, Tuple
from types import ModuleType, FunctionType

import traceback
from contextlib import redirect_stdout, redirect_stderr
from google.protobuf.any_pb2 import Any
from inspect import getmembers, isfunction
import multiprocessing as mp
import queue
from threading import Thread, Lock
import time

from . import logger
from .hub_helper import _clear_hub_user_access
from .redirects import RedirectStdOut, RedirectStdErr
from .pycoderunner_pb2 import RunWellKnownWorkflowResponse


class Script():
    def __init__(self, function_id: str, code: str):
        self._function_id = function_id
        self._code = code
        self._code_lines = []
        self._lock = Lock()
        self._compiled = None
        self._module = None
        self._valid = False
        self._script_complete_event = mp.Event()
        self._output_q_complete_event = None
        self._reset()

        if function_id is None or len(function_id) == 0 or str.isspace(function_id):
            self._error_message = "function_id must not be None, empty or whitespace"
            return

        if code is None or len(code) == 0 or str.isspace(code):
            self._error_message = "code must not be None, empty or whitespace"
            return

        self._code_lines = [f"{index+1}: {line}" for index, line in enumerate(code.split("\n"))]

        try:
            # logger.debug(f"{self._code}")
            self._compiled = compile(self._code, '', 'exec')
            self._module = ModuleType(self._function_id)
            self._valid = True
        except Exception as error:
            with self._lock:
                self._error_message = self._handle_error(error, "compiling")
                logger.error(self._error_message)
                self._valid = False

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

    @property
    def variables(self) -> Dict:
        with self._lock:
            return self._module.__dict__

    def _reset(self):
        with self._lock:
            self._function_result = None
            self._error_message = None
            self._injected_vars = None
            self._script_complete_event.clear()
            self._output_q_complete_event = None

    def _set_complete(self, error_message:str = None):
        with self._lock:
            self._error_message = error_message
            self._script_complete_event.set()

    def _get_functions(self):
        if not self._valid:
            return []
        self._run()
        return getmembers(self._module, isfunction)

    def find_first_function(self, function_names_to_ignore: List[str]) -> FunctionType:
        functions = self._get_functions()
        # logger.debug(f"Functions:\n{functions}")
        for fn_index, val in enumerate(functions):
            if function_names_to_ignore is None:
                return functions[fn_index][1]
            elif val[0] not in function_names_to_ignore:
                return functions[fn_index][1]

    def _run(self):
        try:
            if not self._valid:
                self._set_complete("Script not valid")
                return

            logger.debug(f"Running code with parameters: {self._injected_vars}")

            context = self._module.__dict__
            if self._injected_vars:
                for k in self._injected_vars.keys():
                    context[k] = self._injected_vars[k]

            exec(self._compiled, context, context)
            self._script_complete_event.set()
            if self._output_q_complete_event:
                self._output_q_complete_event.wait()
            logger.debug("Code completed")
        except Exception as error:
            self._set_complete(self._handle_error(error, "running"))

    def _run_function(self):
        try:
            if not self._valid:
                self._set_complete("Script not valid")
                return

            logger.debug(f"Running function: {self._function_input}")
            self._function_result = self._selected_fn(self._function_input)
            logger.debug(f"Function complete {self._function_result}")
            self._script_complete_event.set()

        except Exception as error:
            self._set_complete(self._handle_error(error, "running"))

    def _run_script_in_new_thread(self) -> None:
        thread = Thread(target=self._run)
        logger.debug(f"Starting _run")
        thread.start()

    def _run_function_in_new_thread(self) -> None:
        thread = Thread(target=self._run_function)
        logger.debug(f"Starting _run_function")
        thread.start()

    def run_capture_outputs(self, parameters: Dict) -> Iterable[Tuple[bool, bool, Any, str]]:
        self._reset()
        try:
            response_q = mp.Queue()
            with redirect_stdout(RedirectStdOut(response_q)):
                with redirect_stderr(RedirectStdErr(response_q)):
                    self._injected_vars = parameters
                    self._run_script_in_new_thread()
                    for response in self._process_output(response_q):
                        yield response
        finally:
            if self.is_complete:
                if self.is_error:
                    yield (False, True, None, self._error_message)
                else:
                    yield (True, True, None, None)
            else:
                yield (False, True, None, "Script did not run to completion")
            _clear_hub_user_access()

    def run_function(self, fn: FunctionType, input_values, output_payload_type: str, create_return_payload: Callable[[str, Any], Any]):
        self._reset()
        self._function_input = input_values
        self._selected_fn = fn
        self._run_function()
        if self.is_complete:
            if self.is_error:
                return (False, None, self.error_message)
            response = create_return_payload(output_payload_type, self._function_result)
            if response:
                return (True, response, None)
            else:
                return (False, None, "Function results invalid")
        else:
            return (False, None, "Function did not run to completion")

    def run_function_async(self, fn: FunctionType, input_values, output_payload_type: str, create_return_payload: Callable[[str, Any], Any]):
        self._reset()
        response_q = mp.Queue()
        with redirect_stdout(RedirectStdOut(response_q)):
            with redirect_stderr(RedirectStdErr(response_q)):
                self._function_input = input_values
                self._selected_fn = fn
                self._run_function_in_new_thread()
                for response in self._process_output(response_q):
                    yield response
        if self.is_complete:
            response = create_return_payload(output_payload_type, self._function_result)
            if response:
                yield (True, True, response, None)
            else:
                yield (False, True, None, "Function results invalid")
        else:
            yield (False, True, None, "Function did not run to completion")

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

    def _handle_error(self, error: Exception, run_type: str) -> str:
        try:
            detail = error.args[0]
        except:
            detail = ""
        # cl, exc, tb = sys.exc_info()
        # extracted_tb = traceback.extract_tb(tb)
        # walked = list(traceback.walk_tb())
        tb_lines = traceback.format_exc().split("\n")
        count = 0
        for line in tb_lines:
            if count > 1:
                break
            if not line.strip().startswith("File "):
                continue
            try:
                start = line.index(", line ") + 7
            except:
                continue
            try:
                end = line.index(",", start)
            except:
                end = len(line)
            try:
                if count < 2:
                    line_number = int(line[start:end])
                count += 1
            except:
                line_number = -1
                break

        # print(traceback.format_exc())
        # print(extracted_tb)
        fragment_start_line = max(0, line_number - 3)
        fragment_end_line = min(len(self._code_lines), line_number + 2)
        debug_fragment = ""
        debug_fragment = self._append(debug_fragment, "Debug code fragment:")
        for i in range(fragment_start_line, fragment_end_line):
            debug_fragment = self._append(debug_fragment, self._code_lines[i])
        tb_fragment = ""
        tb_fragment = self._append(tb_fragment, tb_lines[0])
        tb_fragment = self._append(tb_fragment, f"  Script, line {line_number}, in debug fragment above")
        for line in tb_lines[4:]:
            tb_fragment = self._append(tb_fragment, line)
        error_message = f"""Exception {run_type} script: line {line_number}: {type(error).__name__}: {detail}
{debug_fragment}
{tb_fragment}"""
        return error_message

    def _append(self, f, s):
        f += f"{s}\n"
        return f
