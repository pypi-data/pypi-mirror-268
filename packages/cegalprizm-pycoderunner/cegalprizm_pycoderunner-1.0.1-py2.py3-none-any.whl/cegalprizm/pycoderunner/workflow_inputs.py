# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.

from typing import Dict, List

from .pycoderunner_pb2 import WellKnownWorkflowInput


class BaseWorkflowInput():

    def __init__(self, type: str, name: str, label: str, description: str, default_value):
        self._type = type
        self._name = name
        self._label = label
        self._description = description
        self._default_value = default_value

    def get_type(self):
        return self._type

    def get_name(self):
        return self._name

    def get_label(self):
        return self._label

    def get_description(self):
        return self._description

    def get_default_value(self):
        return self._default_value

    def get_wellknown_workflow_input(self):
        input = WellKnownWorkflowInput()
        input.name = self.get_name()
        input.type = self.get_type()
        input.label = self.get_label()
        input.description = self.get_description()
        return input


class BooleanWorkflowInput(BaseWorkflowInput):

    def __init__(self, name: str, label: str, description: str, default_value: bool):
        super().__init__("bool", name, label, description, default_value)

    def get_wellknown_workflow_input(self):
        input = super().get_wellknown_workflow_input()
        input.boolean_input.default_value = self.get_default_value()
        return input


class IntegerWorkflowInput(BaseWorkflowInput):

    def __init__(self, name: str, label: str, description: str, default_value: int, minimum_value: int, maximum_value: int):
        super().__init__("int", name, label, description, default_value)
        self._minimum_value = minimum_value
        self._maximum_value = maximum_value

    def get_minimum_value(self):
        return self._minimum_value

    def get_maximum_value(self):
        return self._maximum_value

    def get_wellknown_workflow_input(self):
        input = super().get_wellknown_workflow_input()
        input.int_input.default_value = self.get_default_value()
        input.int_input.minimum = self.get_minimum_value() or 0
        input.int_input.maximum = self.get_maximum_value() or 0
        input.int_input.has_minimum = self.get_minimum_value() is not None
        input.int_input.has_maximum = self.get_maximum_value() is not None
        return input


class DoubleWorkflowInput(BaseWorkflowInput):

    def __init__(self, name: str, label: str, description: str, default_value: float, minimum_value: float, maximum_value: float, measurement_name: str, display_symbol: str):
        super().__init__("double", name, label, description, default_value)
        self._minimum_value = minimum_value
        self._maximum_value = maximum_value
        self._measurement_name = measurement_name
        self._display_symbol = display_symbol

    def get_minimum_value(self):
        return self._minimum_value

    def get_maximum_value(self):
        return self._maximum_value

    def get_measurement_name(self):
        return self._measurement_name

    def get_display_symbol(self):
        return self._display_symbol

    def get_wellknown_workflow_input(self):
        input = super().get_wellknown_workflow_input()
        input.double_input.default_value = self.get_default_value()
        input.double_input.minimum = self.get_minimum_value() or 0
        input.double_input.maximum = self.get_maximum_value() or 0
        input.double_input.has_minimum = self.get_minimum_value() is not None
        input.double_input.has_maximum = self.get_maximum_value() is not None
        input.double_input.measurement_name = self.get_measurement_name() or ""
        input.double_input.display_symbol = self.get_display_symbol() or ""
        return input


class StringWorkflowInput(BaseWorkflowInput):

    def __init__(self, name: str, label: str, description: str, default_value: str):
        super().__init__("string", name, label, description, default_value)

    def get_wellknown_workflow_input(self):
        input = super().get_wellknown_workflow_input()
        input.string_input.default_value = self.get_default_value()
        return input


class EnumWorkflowInput(BaseWorkflowInput):

    def __init__(self, name: str, label: str, description: str, options: Dict[int, str], default_value: int):
        super().__init__("enum", name, label, description, default_value)
        self._options = options

    def get_wellknown_workflow_input(self):
        input = super().get_wellknown_workflow_input()
        input.enum_input.default_value = self.get_default_value()
        for key in self._options.keys():
            input.enum_input.options[key] = self._options[key]
        return input


class FileWorkflowInput(BaseWorkflowInput):

    def __init__(self, name: str, label: str, description: str, file_extensions: str, select_multiple: bool = False):
        super().__init__("file", name, label, description, None)
        self._file_extensions = file_extensions
        self._select_multiple = select_multiple

    def get_file_extensions(self) -> bool:
        return self._file_extensions

    def get_select_multiple(self) -> bool:
        return self._select_multiple

    def get_wellknown_workflow_input(self):
        input = super().get_wellknown_workflow_input()
        input.file_input.file_extensions = self.get_file_extensions()
        input.file_input.select_multiple = self.get_select_multiple()
        return input


class FolderWorkflowInput(BaseWorkflowInput):

    def __init__(self, name: str, label: str, description: str):
        super().__init__("folder", name, label, description, None)

    def get_wellknown_workflow_input(self):
        input = super().get_wellknown_workflow_input()
        return input


class ObjectRefWorkflowInput(BaseWorkflowInput):

    def __init__(self, name: str, label: str, description: str, object_name: str, template_names: List[str], measurement_name: str, select_multiple: bool, linked_input_name: str):
        super().__init__("object_ref", name, label, description, None)
        self._object_name = object_name
        self._template_names = template_names
        self._measurement_name = measurement_name
        self._select_multiple = select_multiple
        self._linked_input_name = linked_input_name

    def get_object_name(self) -> str:
        return self._object_name

    def get_template_names(self) -> List[str]:
        return self._template_names

    def get_measurement_name(self) -> str:
        return self._measurement_name

    def get_select_multiple(self) -> bool:
        return self._select_multiple

    def get_linked_input_name(self) -> str:
        return self._linked_input_name

    def get_wellknown_workflow_input(self):
        input = super().get_wellknown_workflow_input()
        input.object_ref_input.object_name = self.get_object_name()
        template_names = self.get_template_names()
        if template_names:
            input.object_ref_input.property_name = ';'.join(template_names)
        else:
            input.object_ref_input.property_name = ""
        input.object_ref_input.measurement_name = self.get_measurement_name() or ""
        input.object_ref_input.select_multiple = self.get_select_multiple() or False
        input.object_ref_input.linked_input_name = self.get_linked_input_name() or ""
        return input
