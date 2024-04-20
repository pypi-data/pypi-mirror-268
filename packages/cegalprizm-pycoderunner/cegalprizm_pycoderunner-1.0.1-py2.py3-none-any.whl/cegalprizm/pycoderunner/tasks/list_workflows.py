# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.

from typing import Tuple

from google.protobuf.any_pb2 import Any

from .. import logger
from ..workflow_library import get_environment_name, list_available_workflows, refresh_library
from ..pycoderunner_pb2 import WellKnownWorkflow, ListWellKnownWorkflowsRequest, ListWellKnownWorkflowsResponse


def ListWorkflows(payload: Any) -> Tuple[bool, Any, str]:
    logger.info(f"List workflows request")
    request = ListWellKnownWorkflowsRequest()
    payload.Unpack(request)

    result = ListWellKnownWorkflowsResponse()

    refresh_library(True)

    for workflow_tuple in list_available_workflows():
        try:
            item = WellKnownWorkflow()
            item.environment_name = get_environment_name()
            item.workflow_id = workflow_tuple[0]
            item.name = workflow_tuple[1]._get_name()
            item.category = workflow_tuple[1]._get_category()
            item.description = workflow_tuple[1]._get_description()
            item.authors = workflow_tuple[1]._get_authors()
            item.version = workflow_tuple[1]._get_version()
            item.filepath = workflow_tuple[1]._get_filepath()
            item.is_valid = workflow_tuple[1]._is_valid
            if item.is_valid:
                for parameter in workflow_tuple[1]._get_parameters():
                    item.inputs.append(parameter.get_wellknown_workflow_input())
            else:
                item.error_message = workflow_tuple[1]._get_error_message()
            result.workflows.append(item)
        except Exception as e:
            logger.warning(f'{e}')
            logger.warning(f"Exception listing workflow {workflow_tuple[1]._get_filepath()}")

    logger.info(f"List workflows successful")
    return (True, result, None)
