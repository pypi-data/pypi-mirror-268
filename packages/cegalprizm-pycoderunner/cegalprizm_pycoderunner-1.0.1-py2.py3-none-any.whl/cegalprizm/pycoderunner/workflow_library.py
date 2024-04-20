# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.

from typing import Dict, Iterable, List, Tuple

import hashlib
import os
import sys
import nbformat as nbf
from google.protobuf.any_pb2 import Any

from . import logger
from .python_code_parser import _PythonCodeParser
from .notebook import Notebook
from .script import Script
from .workflow_description import ScriptTypeEnum, WorkflowDescription, WorkflowInfo


this = sys.modules[__name__]

this.environment_name: str = None
this.working_path: str = None
this.workflow_library_paths: List[str] = None
this.workflow_dict = {}


def get_environment_name():
    return this.environment_name


def initialise_workflow_library(environment_name: str, workflow_library_path: str, working_path: str):
    invalid_library_path = False
    invalid_working_path = False

    if environment_name is None or len(environment_name) == 0 or str.isspace(environment_name):
        logger.warning("environment_name must not be None, empty or whitespace")
        return

    if workflow_library_path is None or len(workflow_library_path) == 0 or str.isspace(workflow_library_path):
        logger.warning("workflow_library_path must not be None, empty or whitespace")
        return

    if working_path is None or len(working_path) == 0 or str.isspace(working_path):
        logger.warning("working_path must not be None, empty or whitespace")
        return

    workflow_library_paths = [os.path.abspath(p) for p in workflow_library_path.split(";")]
    for path in workflow_library_paths:
        if not os.path.exists(path):
            logger.warning(f'Specified library path not valid: {path}')
            invalid_library_path = True

    abs_working_path = os.path.abspath(working_path)
    if not os.path.exists(abs_working_path):
        logger.warning(f'Specified working directory not valid: {abs_working_path}')
        invalid_working_path = True

    if invalid_library_path or invalid_working_path:
        return

    this.environment_name = environment_name
    this.working_path = abs_working_path
    this.workflow_library_paths = workflow_library_paths

    logger.info(f"working_path: { this.working_path}")

    refresh_library(True)


def refresh_library(reset_library: bool = False):
    if this.workflow_library_paths is None:
        return

    if reset_library:
        this.workflow_dict.clear()

    for workflow_library_path in this.workflow_library_paths:
        logger.info(f'Refreshing library: {workflow_library_path}')

        for path, subdirs, files in os.walk(workflow_library_path):
            if path.endswith(".ipynb_checkpoints"):
                continue

            files.sort()
            
            for name in files:
                if name.endswith("-checkpoint.ipynb"):
                    continue
                if not (name.endswith(".py") or name.endswith(".ipynb")):
                    continue

                filepath = os.path.join(path, name)
                error_message = None

                logger.info(f'Parsing file: {filepath}')

                if os.path.getsize(filepath) == 0:
                    info = WorkflowDescription(name, "Invalid", "", "", "")
                    error_message = f"{filepath} is an empty file"
                    info._set_error_message(error_message)
                    logger.warning(error_message)
                    this.workflow_dict[filepath] = info
                    continue

                hash_md5 = hashlib.md5()
                with open(filepath, mode='rb') as f:
                    for chunk in iter(lambda: f.read(4096), b""):
                        hash_md5.update(chunk)
                workflow_id = hash_md5.hexdigest()

                if workflow_id in this.workflow_dict.keys():
                    info = WorkflowDescription(name, "Invalid", "", "", "")
                    error_message = f"This workflow already exists in library {filepath}"
                    info._set_error_message(error_message)
                    logger.warning(error_message)
                    this.workflow_dict[filepath] = info
                    continue

                script_type = None
                workflow_description = None
                notebook_kernel_info = {}
                pycoderunner_imports = []

                with open(filepath, "r") as f:
                    if name.endswith(".py"):
                        script_type = ScriptTypeEnum.PyScript
                        lines = f.readlines()
                        workflow_description = _PythonCodeParser.parse_workflow_description(name, lines)
                        pycoderunner_imports = _PythonCodeParser.get_pycoderunner_imports_from_code_lines(lines)
                    elif name.endswith(".ipynb"):
                        script_type = ScriptTypeEnum.Notebook
                        try:
                            nb = nbf.read(f, as_version=nbf.NO_CONVERT)
                            notebook_kernel_info = nb.metadata.get("kernelspec", {})
                            for cell in nb.cells:
                                if cell["cell_type"] == "code":
                                    lines = cell["source"].split("\n")
                                    if not workflow_description:
                                        workflow_description = _PythonCodeParser.parse_workflow_description(name, lines)
                                        pycoderunner_imports += _PythonCodeParser.get_pycoderunner_imports_from_code_lines(lines)
                        except Exception as error:
                            workflow_description = (False, "", error.args[0])
                if workflow_description is None or script_type is None:
                    continue

                info = WorkflowDescription(name, "Invalid", "", "", "")
                if workflow_description[0]:
                    code = ""
                    if pycoderunner_imports:
                        for line in pycoderunner_imports:
                            code += f"{line}\n"
                    code += workflow_description[2]
                    parameters_script = Script(workflow_id, code)
                    parameters_script._run()
                    if not parameters_script.is_valid:
                        error_message = f"WorkflowDescription does not compile"
                        info._set_error_message(error_message)
                        logger.warning(f'{filepath}: {error_message}')
                    elif parameters_script.is_error:
                        error_message = parameters_script.error_message
                        info._set_error_message(error_message)
                        logger.warning(f'{filepath}: {error_message}')
                    elif workflow_description[1] in parameters_script.variables.keys():
                        info = parameters_script.variables[workflow_description[1]]
                    else:
                        error_message = f"WorkflowDescription object incorrectly defined"
                        info._set_error_message(error_message)
                        logger.warning(f'{filepath}: {error_message}')
                else:
                    info._set_error_message(workflow_description[2])
                    logger.warning(workflow_description[2])

                info._set_filepath(filepath)
                info._set_script_type(script_type)

                if script_type == ScriptTypeEnum.Notebook and not notebook_kernel_info:
                    info._category = "Invalid"
                    error_message = f"Notebook kernel not defined. A notebook must have a kernel defined before it can be used as a workflow"
                    info._set_error_message(error_message)
                    logger.warning(f'{filepath}: {error_message}')

                duplicate_info = next((i for i in this.workflow_dict.values() if i._get_name() == info._get_name() and i._get_version() == info._get_version()), None)
                if duplicate_info is not None:
                    error_message = f"This workflow appears to be a duplicate of {duplicate_info._get_filepath()} which already exists in library"
                    info._set_error_message(error_message)
                    logger.warning(f'{filepath}: {error_message}')

                this.workflow_dict[workflow_id] = info
                logger.info(f'Add workflow: {info._get_name()}')


def run_workflow(info: WorkflowInfo, parameters) -> Iterable[Tuple[bool, bool, Any, str]]:
    try:
        working_path = info.working_path
        logger.debug(f"working_path: {working_path}")

        if info.script_type == ScriptTypeEnum.Notebook:

            notebook = Notebook(info.filepath, working_path)

            if not notebook.is_valid:
                return [(False, True, None, notebook.error_message)]

            return notebook.run_capture_outputs(parameters)

        elif info.script_type == ScriptTypeEnum.PyScript:
            with open(info.filepath, 'r') as file:
                parameters["working_path"] = working_path
                path = os.path.normpath(os.path.dirname(info.filepath)).replace('\\', '/')
                os.chdir(path)
                code = f"import sys\nsys.path.append('{path}')\n"
                code += file.read()

                script = Script("temp", code)

                if not script.is_valid:
                    return [(False, True, None, script.error_message)]

                return script.run_capture_outputs(parameters)
        else:
            logger.warning(f'{e}')
            return [(False, True, None, f"Error running {info.name}")]

    except Exception as e:
        logger.warning(f'{e}')
        return [(False, True, None, f"Error running workflow {e}")]


def list_available_workflows() -> Iterable[Tuple[str, WorkflowDescription]]:
    for key in this.workflow_dict.keys():
        yield (key, this.workflow_dict[key])


def get_workflow_info(workflow_id: str) -> WorkflowInfo:
    if workflow_id not in this.workflow_dict.keys():
        return None
    return WorkflowInfo(this.workflow_dict[workflow_id])
