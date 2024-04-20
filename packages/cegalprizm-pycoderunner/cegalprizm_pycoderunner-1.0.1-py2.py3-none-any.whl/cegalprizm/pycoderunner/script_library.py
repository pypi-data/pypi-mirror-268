# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.

import hashlib
from contextlib import redirect_stdout, redirect_stderr
import sys

from . import logger
from .redirects import RedirectStdOut, RedirectStdErr
from .script import Script

this = sys.modules[__name__]
this.script_dict = {}


def add_script(code: str):
    if code is None or len(code) == 0 or str.isspace(code):
        return (False, "code must not be None, empty or whitespace")

    try:
        function_id = hashlib.sha256(code.encode('utf-8')).hexdigest()
        if function_id in this.script_dict.keys():
            logger.debug(f"Script already exists")
            return (True, function_id)

        try:
            logger.debug(f"Compiling script\n{code}")
            script = Script(function_id, code)
            if script.is_error:
                return (False, script.error_message)
            this.script_dict[function_id] = script
            return (True, function_id)
        except Exception as error:
            error_message = f"Exception compiling script: {type(error)}: {error}: {error.args}"
            logger.error(error_message)
            return (False, error_message)

    except:
        return (False, "Script not valid")


# def compile_script(script, injected_vars=None, injected_code=None, cache_module=True):
#     try:
#         function_id = hashlib.md5(script.encode('utf-8')).hexdigest()
#         if function_id in this.script_dict.keys():
#             logger.debug(f"Script already exists")
#             return (True, function_id, None, None)

#         try:
#             logger.debug(f"Compiling script")

#             injection_code = ""

#             if injected_code is not None and len(injected_code) > 0:
#                 injection_code += f"{injected_code}\n"

#             if injected_vars is not None and len(injected_vars) > 0:
#                 for key, value in injected_vars.items():
#                     if isinstance(value, str):
#                         injection_code += f"{key} = '{value}'\n"
#                     else:
#                         injection_code += f"{key} = {value}\n"

#             code = ""

#             if len(injection_code) > 0:
#                 code += f"{injection_code}\n"
#             code += script

#             logger.debug(code)
#             script_obj = Script(function_id, code)

#             if cache_module:
#                 this.script_dict[function_id] = script_obj

#             with redirect_stdout(RedirectStdOut()) as stdout:
#                 with redirect_stderr(RedirectStdErr()) as stderr:
#                     script_obj._run()
#                     return (True, function_id, stdout.get_string(), stderr.get_string())

#         except Exception as error:
#             error_message = f"Exception compiling script: {type(error)}: {error}: {error.args}"
#             logger.error(error_message)
#             return (False, error_message)

#     except:
#         return (False, "Script not valid")


def get_script(function_id: str) -> Script:
    if function_id not in this.script_dict.keys():
        return None

    return this.script_dict[function_id]
