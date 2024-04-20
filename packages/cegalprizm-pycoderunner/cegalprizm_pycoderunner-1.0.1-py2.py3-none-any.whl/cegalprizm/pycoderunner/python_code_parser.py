# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.
from typing import Dict, List, Tuple

import re
import ast

from . import logger


class _PythonCodeParser():

    def __new__(cls):
        raise TypeError("This is a static class and cannot be instantiated.")

    @staticmethod
    def get_pycoderunner_imports_from_code_lines(code_lines: List[str]) -> List[str]:
        import_lines = []
        for line in code_lines:
            if re.match(r'^\s*(import|from)\s.*cegalprizm\.pycoderunner.*', line):
                import_lines.append(line.strip())
        return import_lines

    # @staticmethod
    # def get_variables_from_code_string(code: str) -> Dict[str, any]:
    #     user_defined_vars = {}
    #     assign_nodes = PythonCodeParser._get_variable_assign_nodes_from_code_string(code)
    #     for node in assign_nodes:
    #         for target in node.targets:
    #             try:
    #                 var_content = eval(compile(ast.Expression(node.value), '<string>', 'eval'), globals(), user_defined_vars)
    #             except NameError:
    #                 var_content = None
    #             if isinstance(target, ast.Name) and var_content is not None:
    #                 var_name = target.id
    #                 user_defined_vars[var_name] = var_content
    #             elif (isinstance(target, ast.Tuple) or isinstance(target, ast.List) and var_content is not None):
    #                 for i, elt in enumerate(target.elts):
    #                     if isinstance(elt, ast.Name):
    #                         var_name = elt.id
    #                         user_defined_vars[var_name] = var_content[i]
    #     return user_defined_vars

    # @staticmethod
    # def _get_variable_assign_nodes_from_code_string(code: str) -> List[ast.Assign]:
    #     code_tree = ast.parse(code)
    #     return [node for node in ast.walk(code_tree) if isinstance(node, ast.Assign)]

    @staticmethod
    def parse_workflow_description(filename: str, lines: List[str]) -> Tuple[bool, str, str]:
        return _PythonCodeParser._parse_description("PWR Description", "WorkflowDescription", filename, lines)

    @staticmethod
    def _parse_description(identifier: str, class_name: str, filename: str, lines: List[str]) -> Tuple[bool, str, str]:
        count = 0
        start_description_line = -1
        stop_description_line = -1
        description_found = False
        description_invalid = False
        code_lines: List[str] = []
        variables: List[str] = []

        # Strips the newline character
        for line in lines:
            stripped_line = line.strip()
            if stripped_line == f"# Start: {identifier}":
                start_description_line = count
            if stripped_line == f"# End: {identifier}":
                stop_description_line = count
                break
            stripped_line = stripped_line.replace(" ", "")
            index = stripped_line.find(f"={class_name}(")
            if index > 0:
                description_found = True
                description_invalid = start_description_line == -1
                variables.append(stripped_line[0:index])

            if start_description_line != -1 and count > start_description_line and stop_description_line == -1:
                code_lines.append(line)
            count += 1

        if start_description_line == -1 and stop_description_line == -1 and not description_found:
            return None

        if start_description_line == -1 and stop_description_line == -1 and description_invalid:
            return (False, "", f'{filename}: {class_name} defined outside a {identifier} block')

        if start_description_line >= 0 and stop_description_line == -1:
            return (False, "", f'{filename}: End: {identifier} not valid')

        if start_description_line == -1 and stop_description_line >= 0:
            return (False, "", f'{filename}: Start: {identifier} not valid')

        if len(variables) == 0:
            return (False, "", f'{filename}: No {class_name} found within {identifier} block')

        if len(variables) > 1:
            return (False, "", f'{filename}: Multiple {class_name} defined within {identifier} block')

        for line in code_lines:
            stripped_line = line.strip().replace(" ", "")
            if len(stripped_line) == 0:
                continue

            if line.startswith("from") or line.startswith("import"):
                continue
            elif line.startswith(variables[0]):
                continue
            elif line.startswith(" "):
                continue
            else:
                logger.warning(f'{filename}:{line}')
                logger.warning(f'{filename}: {identifier} may contain unexpected code')
                logger.warning(f'Please ensure only the {class_name} is defined in within {identifier} block')
                break

        description_code = ""
        for line in code_lines:
            description_code += f"{line}\n"

        # logger.debug(description_code)

        return (True, variables[0], description_code)
