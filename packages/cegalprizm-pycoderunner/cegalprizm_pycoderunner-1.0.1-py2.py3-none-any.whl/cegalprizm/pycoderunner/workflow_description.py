# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.

import os
from typing import Dict, Iterable, List, Tuple, Union

from enum import Enum

from . import logger
from .enums.domain_objects import DomainObjectsEnum
from .enums.measurement_names import MeasurementNamesEnum
from .enums.template_names import TemplateNamesEnum
from .workflow_inputs import BaseWorkflowInput
from .workflow_inputs import BooleanWorkflowInput, IntegerWorkflowInput, DoubleWorkflowInput
from .workflow_inputs import StringWorkflowInput, FileWorkflowInput, FolderWorkflowInput
from .workflow_inputs import EnumWorkflowInput, ObjectRefWorkflowInput


class ScriptTypeEnum(Enum):
    PyScript = 1
    Notebook = 2


class WorkflowDescription():

    def __init__(self, name: str, category: str, description: str, authors: str, version: str):
        """
        Describes a PWR workflow

        Args:
            name (str): The name of the workflow.
            category (str): The category of the workflow (this is a free text string that can be used by the user to help filter and discover workflows)
            description (str): A free text field description of the workflow and what is does.
            authors (str): A free text field that can be used to list the names/email addresses of who should be contacted for support and/or additional information about this workflow.
            version (str): A free text field that can be used to describe the version of the workflow.
        """
        self._is_valid = True
        self._error_message = ""

        if not isinstance(name, str):
            self._is_valid = False
            raise ValueError(f"name must be a str")
        if not isinstance(category, str):
            self._is_valid = False
            raise ValueError(f"category must be a str")
        if not isinstance(description, str):
            self._is_valid = False
            raise ValueError(f"description must be a str")
        if not isinstance(authors, str):
            self._is_valid = False
            raise ValueError(f"authors must be a str")
        if not isinstance(version, str):
            self._is_valid = False
            raise ValueError(f"version must be a str")

        self._name = name
        self._category = category
        self._description = description
        self._authors = authors
        self._version = version
        self._filepath = ""
        self._script_type = ScriptTypeEnum.PyScript
        self._parameters: List[BaseWorkflowInput] = []

    def _get_name(self) -> str:
        return self._name

    def _get_category(self) -> str:
        return self._category

    def _get_description(self) -> str:
        return self._description

    def _get_authors(self) -> str:
        return self._authors

    def _get_version(self) -> str:
        return self._version

    def _get_script_type(self) -> ScriptTypeEnum:
        return self._script_type

    def _set_script_type(self, script_type: ScriptTypeEnum):
        self._script_type = script_type

    def _get_filepath(self) -> str:
        return self._filepath

    def _set_filepath(self, filepath: str):
        self._filepath = filepath

    def _get_parameters(self) -> Iterable[BaseWorkflowInput]:
        return self._parameters

    def _get_error_message(self) -> str:
        return self._error_message

    def _set_error_message(self, error_message: str):
        self._error_message = error_message
        self._is_valid = False

    def add_boolean_parameter(self, name: str, label: str, description: str, default_value: bool):
        """
        Adds a boolean parameter to the workflow description.

        This will generate a checkbox in the workflow UI.

        Args:
            name (str): The name of the object created the parameters dictionary. This name must be unique within the workflow.
            label (str): The label text that will be displayed next to the checkbox in the workflow UI.
            description (str): A description of what the parameter represents. This description will be shown in the tooltip next to the checkbox in the workflow UI.
            default_value (bool): The default value to be assigned to the parameter.

        Raises:
            ValueError: If the name is already used in the workflow.
        """

        valid = self._is_common_parameters_valid(name, label, description)
        if not valid[0]:
            self._is_valid = False
            self._error_message = valid[1]
            raise ValueError(self._error_message)

        if not isinstance(default_value, bool):
            self._is_valid = False
            self._error_message = f"Parameter {name}: default_value must be a bool"
            raise ValueError(self._error_message)

        self._parameters.append(BooleanWorkflowInput(name, label, description, default_value))
        return self

    def add_integer_parameter(self, name: str, label: str, description: str, default_value: int = 0,
                              minimum_value: int = None, maximum_value: int = None):
        """
        Adds a integer parameter to the workflow description.

        This will generate an integer number field in the workflow UI.

        Args:
            name (str): The name of the object created the parameters dictionary. This name must be unique within the workflow.
            label (str): The label text that will be displayed next to the field in the workflow UI.
            description (str): A description of what the parameter represents. This description will be shown in the tooltip next to the field in the workflow UI.
            default_value (int, optional): If defined this specifies the default value to be assigned to the parameter. Defaults to 0.
            minimum_value (int, optional): If defined this specifies the lowest value the field can accept. Defaults to None.
            maximum_value (int, optional): If defined this specifies the highest value the field can accept. Defaults to None.

        Raises:
            ValueError: If the name is already used in the workflow.
        """

        valid = self._is_common_parameters_valid(name, label, description)
        if not valid[0]:
            self._is_valid = False
            self._error_message = valid[1]
            raise ValueError(self._error_message)

        if not isinstance(default_value, int):
            self._is_valid = False
            self._error_message = f"Parameter {name}: default_value must be an int"
            raise ValueError(self._error_message)
        if minimum_value and not isinstance(minimum_value, int):
            self._is_valid = False
            self._error_message = f"Parameter {name}: default_value must be a int or None"
            raise ValueError(self._error_message)
        if maximum_value and not isinstance(maximum_value, int):
            self._is_valid = False
            self._error_message = f"Parameter {name}: maximum_value must be a int or None"
            raise ValueError(self._error_message)

        self._parameters.append(IntegerWorkflowInput(name, label, description, default_value,
                                                     minimum_value, maximum_value))
        return self

    def add_float_parameter(self, name: str, label: str, description: str, default_value: float = 0.0,
                            minimum_value: float = None, maximum_value: float = None,
                            measurement_type: Union[MeasurementNamesEnum, str] = None,
                            display_symbol: str = None):
        """Adds a float parameter to the workflow description.

        This will generate an float number field in the workflow UI.

        Args:
            name (str): The name of the object created the parameters dictionary. This name must be unique within the workflow.
            label (str): The label text that will be displayed next to the field in the workflow UI.
            description (str): A description of what the parameter represents. This text will be shown in the tooltip next to the field in the workflow UI.
            default_value (float, optional): If defined this specifies the default value to be assigned to the parameter. Defaults to 0.
            minimum_value (float, optional): If defined this specifies the lowest value the field can accept. Defaults to None.
            maximum_value (float, optional): If defined this specifies the highest value the field can accept. Defaults to None.
            measurement_type (Union[MeasurementNamesEnum, str], optional): If defined this specifies the measurement type of the parameter. Defaults to None.
            display_symbol (str, optional): If defined this specifies the units of the supplied parameter.
                                            This allows the workflow to ensure that the parameter will be in the given units irrespective of the display units in the Petrel project.
                                            Defaults to None.

        Raises:
            ValueError: If the name is already used in the workflow.
            ValueError: If the measurement_type is not MeasurementNamesEnum or a str
        """

        valid = self._is_common_parameters_valid(name, label, description)
        if not valid[0]:
            self._is_valid = False
            self._error_message = valid[1]
            raise ValueError(self._error_message)

        if not isinstance(default_value, float) and not isinstance(default_value, int):
            self._is_valid = False
            self._error_message = f"Parameter {name}: default_value must be a float"
            raise ValueError(self._error_message)
        if minimum_value and not isinstance(minimum_value, float) and not isinstance(minimum_value, int):
            self._is_valid = False
            self._error_message = f"Parameter {name}: minimum_value must be a float or None"
            raise ValueError(self._error_message)
        if maximum_value and not isinstance(maximum_value, float) and not isinstance(maximum_value, int):
            self._is_valid = False
            self._error_message = f"Parameter {name}: maximum_value must be a float or None"
            raise ValueError(self._error_message)

        measurement_name = None
        if measurement_type:
            if isinstance(measurement_type, MeasurementNamesEnum):
                measurement_name = measurement_type.value
            elif isinstance(measurement_type, str):
                measurement_name = measurement_type
            else:
                self._is_valid = False
                self._error_message = f"Parameter {name}: measurement_type invalid: must be MeasurementNamesEnum or str or None"
                raise ValueError(self._error_message)

        if display_symbol:
            if not measurement_type:
                self._is_valid = False
                self._error_message = f"Parameter {name}: display_symbol should only be defined if measurement_type is defined"
                raise ValueError(self._error_message)
            if not isinstance(display_symbol, str):
                self._is_valid = False
                self._error_message = f"Parameter {name}: display_symbol must be a str"
                raise ValueError(self._error_message)

        if measurement_type:
            if not display_symbol:
                self._is_valid = False
                self._error_message = f"Parameter {name}: display_symbol must be defined if measurement_type is defined"
                raise ValueError(self._error_message)

        _default_value = None
        if default_value is not None:
            _default_value = float(default_value)

        _minimum_value = None
        if minimum_value is not None:
            _minimum_value = float(minimum_value)

        _maximum_value = None
        if maximum_value is not None:
            _maximum_value = float(maximum_value)

        self._parameters.append(DoubleWorkflowInput(name, label, description, _default_value,
                                                    _minimum_value, _maximum_value,
                                                    measurement_name,
                                                    display_symbol))
        return self

    def add_string_parameter(self, name: str, label: str, description: str, default_value: str = ""):
        """
        Adds a string parameter to the workflow description.

        This will generate a text field in the workflow UI.

        Args:
            name (str): The name of the object created the parameters dictionary. This name must be unique within the workflow.
            label (str): The label text that will be displayed next to the text field in the workflow UI.
            description (str): A description of what the parameter is used for. This description will be shown in the tooltip next to the text field in the workflow UI.
            default_value (str, optional): The default value to be assigned to the parameter.

        Raises:
            ValueError: If the name is already used in the workflow.
        """

        valid = self._is_common_parameters_valid(name, label, description)
        if not valid[0]:
            self._is_valid = False
            self._error_message = valid[1]
            raise ValueError(self._error_message)

        if not isinstance(default_value, str):
            self._is_valid = False
            self._error_message = f"Parameter {name}: default_value must be a str"
            raise ValueError(self._error_message)

        self._parameters.append(StringWorkflowInput(name, label, description, default_value))
        return self

    def add_enum_parameter(self, name: str, label: str, description: str, options: Dict[int, str], default_value: int = None):
        """
        Adds a enum parameter to the workflow description.

        This will generate a combobox in the workflow UI.

        Args:
            name (str): The name of the object created the parameters dictionary. This name must be unique within the workflow.
            label (str): The label text that will be displayed next to the text field in the workflow UI.
            description (str): A description of what the parameter is used for. This description will be shown in the tooltip next to the combobox in the workflow UI.
            options (Dict[int, str]): A dictionary of options where each option is described by a value and the text to be shown for it.
            default_value (int, optional): The default value to be assigned to the parameter.

        Raises:
            ValueError: If the name is already used in the workflow.
        """

        valid = self._is_common_parameters_valid(name, label, description)
        if not valid[0]:
            self._is_valid = False
            self._error_message = valid[1]
            raise ValueError(self._error_message)

        if not isinstance(options, dict):
            self._is_valid = False
            self._error_message = f"Parameter {name}: options must be a dict"
            raise ValueError(self._error_message)
        if len(options) == 0:
            self._is_valid = False
            self._error_message = f"Parameter {name}: options must not be empty"
            raise ValueError(self._error_message)

        valid_keys = []
        valid_options = {}
        for key in options.keys():
            if not isinstance(key, int):
                self._is_valid = False
                self._error_message = f"Parameter {name}: option {str(key)} key must be int"
                raise ValueError(self._error_message)
            if not isinstance(options[key], str):
                self._is_valid = False
                self._error_message = f"Parameter {name}: option {str(key)} value must be str"
                raise ValueError(self._error_message)
            if options[key] in valid_options.values():
                self._is_valid = False
                self._error_message = f"Parameter {name}: option {str(key)} value is already defined as an option"
                raise ValueError(self._error_message)
            valid_keys.append(key)
            valid_options[key] = options[key]

        if default_value is None:
            default_value = valid_keys[0]
        if not isinstance(default_value, int):
            self._is_valid = False
            self._error_message = f"Parameter {name}: default_value must be a int"
            raise ValueError(self._error_message)
        if default_value not in valid_options.keys():
            self._is_valid = False
            self._error_message = f"Parameter {name}: default_value must be a defined option"
            raise ValueError(self._error_message)

        self._parameters.append(EnumWorkflowInput(name, label, description, options, default_value))
        return self

    def add_file_parameter(self, name: str, label: str, description: str, file_extensions: str, select_multiple: bool = False):
        """
        Adds a file parameter to the workflow description.

        This will generate a file selection in the workflow UI.

        Args:
            name (str): The name of the object created the parameters dictionary. This name must be unique within the workflow.
            label (str): The label text that will be displayed next to the text field in the workflow UI.
            description (str): A description of what the parameter is used for. This description will be shown in the tooltip next to the text field in the workflow UI.
            file_extensions (str): The file extensions supported.
            select_multiple (bool, optional): Specifies if the parameter can contain multiple values. Defaults to False.

        Raises:
            ValueError: If the name is already used in the workflow.
        """

        valid = self._is_common_parameters_valid(name, label, description)
        if not valid[0]:
            self._is_valid = False
            self._error_message = valid[1]
            raise ValueError(self._error_message)

        if not isinstance(file_extensions, str):
            self._is_valid = False
            self._error_message = f"Parameter {name}: file_extensions must be a str0"
            raise ValueError(self._error_message)

        if not isinstance(select_multiple, bool):
            self._is_valid = False
            self._error_message = f"Parameter {name}: select_multiple must be a bool"
            raise ValueError(self._error_message)

        self._parameters.append(FileWorkflowInput(name, label, description, file_extensions, select_multiple))
        return self

    def add_folder_parameter(self, name: str, label: str, description: str):
        """
        Adds a folder parameter to the workflow description.

        This will generate a folder selection in the workflow UI.

        Args:
            name (str): The name of the object created the parameters dictionary. This name must be unique within the workflow.
            label (str): The label text that will be displayed next to the text field in the workflow UI.
            description (str): A description of what the parameter is used for. This description will be shown in the tooltip next to the text field in the workflow UI.

        Raises:
            ValueError: If the name is already used in the workflow.
        """

        valid = self._is_common_parameters_valid(name, label, description)
        if not valid[0]:
            self._is_valid = False
            self._error_message = valid[1]
            raise ValueError(self._error_message)

        self._parameters.append(FolderWorkflowInput(name, label, description))
        return self

    def add_object_ref_parameter(self, name: str, label: str, description: str,
                                 object_type: Union[DomainObjectsEnum, str],
                                 template_type: Union[Iterable[Union[TemplateNamesEnum, str]], TemplateNamesEnum, str] = None,
                                 measurement_type: Union[MeasurementNamesEnum, str] = None,
                                 select_multiple: bool = False,
                                 linked_input_name: str = None):
        """
        Adds a string parameter to the workflow description.

        This will generate a domain object selector (blue arrow control) in the workflow UI.

        Note: If select_multiple is False then the parameter value will be set to the DROID of the selected domain object.
              If select_multiple is True then the parameter value will be a list of DROIDs for the selected domain objects.

        Args:
            name (str): The name of the object created the parameters dictionary. This name must be unique within the workflow.
            label (str): The label text that will be displayed next to the dropbox in the workflow UI.
            description (str): A description of what the parameter is used for. This description will be shown in the tooltip next to the text field in the workflow UI.
            object_type (Union[DomainObjectsEnum, str]): The domain object type that must be supplied for this parameter.
                                                         The workflow UI will limit the user to selecting only domain objects for this type.
            template_type (Union[Iterable[Union[TemplateNamesEnum, str]], TemplateNamesEnum, str], optional): If defined this specifies the template types accepted for the parameter. Defaults to None.
            measurement_type (Union[MeasurementNamesEnum, str], optional): If defined this specifies the measurement type accepted for the parameter. Defaults to None.
            select_multiple (bool, optional): Specifies if the parameter can contain multiple values. Defaults to False.
            linked_input_name (str, optional): If defined this specifies the name of another parameter defined in the workflow which must be specified to enable this parameter in the workflow UI.
                                               Defaults to None.

        Raises:
            ValueError: If the name is already used in the workflow.
            ValueError: If the object_type is not DomainObjectsEnum or a str
            ValueError: If the template_type is not Iterable[TemplateNamesEnum] or a Iterable[str] or TemplateNamesEnum or a str
            ValueError: If the measurement_type is not MeasurementNamesEnum or a str
        """

        valid = self._is_common_parameters_valid(name, label, description)
        if not valid[0]:
            self._is_valid = False
            self._error_message = valid[1]
            raise ValueError(self._error_message)

        object_name = None
        if isinstance(object_type, DomainObjectsEnum):
            object_name = object_type.value
        elif isinstance(object_type, str):
            object_name = object_type
        else:
            self._is_valid = False
            self._error_message = f"Parameter {name}: object_type invalid: must be DomainObjectsEnum or str"
            raise ValueError(self._error_message)

        template_names = None
        if template_type:
            template_type_valid = False
            if isinstance(template_type, TemplateNamesEnum):
                template_type_valid = True
                template_names = []
                template_names.append(template_type.value)
            elif isinstance(template_type, str):
                template_type_valid = True
                template_names = []
                template_names.append(template_type)
            else:
                try:
                    template_type_valid = True
                    template_names = []
                    for val in iter(template_type):
                        if isinstance(val, TemplateNamesEnum):
                            template_names.append(val.value)
                        elif isinstance(val, str):
                            template_names.append(val)
                        else:
                            template_type_valid = False
                            break
                except TypeError:
                    # not iterable
                    template_type_valid = False

            if not template_type_valid:
                self._is_valid = False
                self._error_message = f"Parameter {name}: template_type invalid: must be an iterable or TemplateNamesEnum or str"
                raise ValueError(self._error_message)

        measurement_name = None
        if measurement_type:
            if isinstance(measurement_type, MeasurementNamesEnum):
                measurement_name = measurement_type.value
            elif isinstance(measurement_type, str):
                measurement_name = measurement_type
            else:
                self._is_valid = False
                self._error_message = f"Parameter {name}: measurement_type invalid: must be MeasurementNamesEnum or str"
                raise ValueError(self._error_message)

        if not isinstance(select_multiple, bool):
            self._is_valid = False
            self._error_message = f"Parameter {name}: select_multiple must be a bool"
            raise ValueError(self._error_message)

        if linked_input_name:
            if not isinstance(linked_input_name, str):
                self._is_valid = False
                self._error_message = f"Parameter {name}: linked_input_name must be a str"
                raise ValueError(self._error_message)

        self._parameters.append(ObjectRefWorkflowInput(name, label, description,
                                                       object_name,
                                                       template_names,
                                                       measurement_name,
                                                       select_multiple,
                                                       linked_input_name))
        return self

    def is_valid(self) -> bool:
        """Returns a bool indicating if the workflow is valid

        Returns:
            bool: Indicates the if the workflow is valid
        """
        if not self._is_valid:
            return False

        linked_names_valid = self._linked_names_valid()
        if not linked_names_valid[0]:
            raise ValueError(linked_names_valid[1])

        return True

    def get_default_parameters(self) -> Dict[str, object]:
        """
        Returns a dictionary of the default values for parameters required by the workflow.

        THis is useful when testing the workflow outside of PWR.

        Returns:
            Dict[str, object]: _description_
        """
        try:
            if not self.is_valid():
                return None
        except:
            return None

        default_parameters = {}
        for item in self._parameters:
            default_parameters[item.get_name()] = item.get_default_value()
        return default_parameters

    def get_label(self, name: str) -> str:
        if not isinstance(name, str):
            raise ValueError(f"Parameter {name}: name must be a str")
        item = next((x for x in self._parameters if x.get_name() == name), None)
        if item is None:
            raise ValueError(f"Parameter {name}: No parameter defined with '{name}'")
        return item.get_label()
    
    def _is_common_parameters_valid(self, name: str, label: str, description: str) -> Tuple[bool, str]:
        if not isinstance(name, str):
            return (False, f"Parameter {name}: name must be a str")
        item = next((x for x in self._parameters if x.get_name() == name), None)
        if item is not None:
            return (False, f"Parameter {name}: Parameter already defined with '{name}'")
        elif name.lower() != name:
            return (False, f"Parameter {name}: name must be lowercase")
        elif ' ' in name:
            return (False, f"Parameter {name}: name must not contain spaces")

        if not isinstance(label, str):
            self._is_valid = False
            self._error_message = f"Parameter {name}: label must be a str"
            raise ValueError(self._error_message)

        if not isinstance(description, str):
            self._is_valid = False
            self._error_message = f"Parameter {name}: description must be a str"
            raise ValueError(self._error_message)

        return (True, "")

    def _linked_names_valid(self) -> Tuple[bool, str]:
        for parameter in self._parameters:
            if isinstance(parameter, ObjectRefWorkflowInput):
                linked_input_name = parameter.get_linked_input_name()
                if linked_input_name:
                    if linked_input_name == parameter.get_name():
                        return (False, f"Parameter '{parameter.get_name()}': cannot be is linked to itself in workflow {self._get_filepath()}")

                    linked_parameter = next((x for x in self._parameters if x.get_name() == linked_input_name), None)
                    if linked_parameter is None:
                        return (False, f"Parameter '{parameter.get_name()}': linked parameter '{linked_input_name}' is not defined in the workflow {self._get_filepath()}")
        return (True, "")


class WorkflowInfo():
    def __init__(self, description: WorkflowDescription):
        self.is_valid = description.is_valid()
        self.script_type = description._get_script_type()
        self.filepath = description._get_filepath()
        self.name = description._get_name()
        self.working_path = os.environ['pwr_working_path']
