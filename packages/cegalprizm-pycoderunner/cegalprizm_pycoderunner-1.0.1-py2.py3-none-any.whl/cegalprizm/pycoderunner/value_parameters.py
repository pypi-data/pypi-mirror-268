# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.

import numpy as np
from google.protobuf.any_pb2 import Any

from .pycoderunner_pb2 import DoubleValuePayload, Double1DPayload, Double2DPayload
from .pycoderunner_pb2 import IntValuePayload, Int1DPayload, Int2DPayload
from .pycoderunner_pb2 import BoolValuePayload, Bool1DPayload
from .pycoderunner_pb2 import StringValuePayload, String1DPayload


def get_value_from_payload(parameter):
    if parameter is None:
        return (False, None)
    return get_value(parameter.content_type, parameter.content)


def get_value(content_type: str, content: Any):
    if content_type == "DoubleValuePayload":
        input = DoubleValuePayload()
        content.Unpack(input)
        return (True, input.value)
    elif content_type == "Double1DPayload":
        input = Double1DPayload()
        content.Unpack(input)
        return (True, [x for x in input.values])
    elif content_type == "Double2DPayload":
        input = Double2DPayload()
        content.Unpack(input)
        val = []
        for x in input.values:
            val.append([y for y in x.values])
        return (True, val)
    elif content_type == "IntValuePayload":
        input = IntValuePayload()
        content.Unpack(input)
        return (True, input.value)
    elif content_type == "Int1DPayload":
        input = Int1DPayload()
        content.Unpack(input)
        return (True, [x for x in input.values])
    elif content_type == "Int2DPayload":
        input = Int2DPayload()
        content.Unpack(input)
        val = []
        for x in input.values:
            val.append([y for y in x.values])
        return (True, val)
    elif content_type == "BoolValuePayload":
        input = BoolValuePayload()
        content.Unpack(input)
        return (True, input.value)
    elif content_type == "Bool1DPayload":
        input = Bool1DPayload()
        content.Unpack(input)
        return (True, [x for x in input.values])
    elif content_type == "StringValuePayload":
        input = StringValuePayload()
        content.Unpack(input)
        return (True, input.value)
    elif content_type == "String1DPayload":
        input = String1DPayload()
        content.Unpack(input)
        return (True, [x for x in input.values])
    else:
        return (False, None)


def get_payload(payload_type: str, values):
    if payload_type == "DoubleValuePayload":
        output = DoubleValuePayload()
        output.value = values
        return (True, output)
    elif payload_type == "Double1DPayload":
        output = Double1DPayload()
        for x in values:
            if (isinstance(x, np.ndarray)):
                output.values.append(x[0])
            else:
                output.values.append(x)
        return (True, output)
    elif payload_type == "Double2DPayload":
        output = Double2DPayload()
        for x in values:
            inner_tuple = get_payload("Double1DPayload", x)
            output.values.append(inner_tuple[1])
        return (True, output)
    elif payload_type == "IntValuePayload":
        output = IntValuePayload()
        output.value = values
        return (True, output)
    elif payload_type == "Int1DPayload":
        output = Int1DPayload()
        for x in values:
            if (isinstance(x, np.ndarray)):
                output.values.append(x[0])
            else:
                output.values.append(x)
        return (True, output)
    elif payload_type == "Int2DPayload":
        output = Int2DPayload()
        for x in values:
            inner_tuple = get_payload("Int1DPayload", x)
            output.values.append(inner_tuple[1])
        return (True, output)
    elif payload_type == "BoolValuePayload":
        output = BoolValuePayload()
        output.value = values
        return (True, output)
    elif payload_type == "Bool1DPayload":
        output = Bool1DPayload()
        for x in values:
            if (isinstance(x, np.ndarray)):
                output.values.append(x[0])
            else:
                output.values.append(x)
        return (True, output)
    elif payload_type == "StringValuePayload":
        output = StringValuePayload()
        output.value = values
        return (True, output)
    elif payload_type == "String1DPayload":
        output = String1DPayload()
        for x in values:
            if (isinstance(x, np.ndarray)):
                output.values.append(x[0])
            else:
                output.values.append(x)
        return (True, output)
    else:
        return (False, None)
