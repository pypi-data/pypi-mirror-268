# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.

from typing import Iterable, Tuple
import multiprocessing as mp
import time
import os

from google.protobuf.any_pb2 import Any

from cegalprizm.hub import TaskContext

from .. import logger
from ..hub_helper import _set_hub_user_access, _get_hub_user_identity
from ..workflow_library import run_workflow, get_workflow_info
from ..value_parameters import get_value_from_payload
from ..pycoderunner_pb2 import RunWellKnownWorkflowRequest, StringValuePayload



def _run(input_q: mp.Queue, output_q: mp.Queue, done_event: mp.Event):
    (info, parameters, metadata, context_id, session_id) = input_q.get()
    _set_hub_user_access(metadata)
    if context_id is not None:
        os.environ['workflow_context_id'] = context_id
    if session_id is not None:
        os.environ['session_id'] = session_id
    for r in run_workflow(info, parameters):
        output_q.put(r)
    done_event.set()


def RunWorkflow(ctx: TaskContext, payload: Any) -> Iterable[Tuple[bool, bool, Any, str]]:
    logger.info(f"Run workflow request: identity: '{_get_hub_user_identity(ctx.metadata)}'")
    request = RunWellKnownWorkflowRequest()
    payload.Unpack(request)
    parameters = None
    context_id = None
    session_id = None
    if request.parameters is not None:
        params = {}
        for item in request.parameters.dict.items():
            input = get_value_from_payload(item[1])
            if input[0]:
                if input[1] is not None:
                    params[item[0]] = input[1]
            else:
                parameter = item[1]
                if parameter.content_type == "__contextId":
                    context_id_payload = StringValuePayload()
                    parameter.content.Unpack(context_id_payload)
                    context_id = context_id_payload.value
                elif parameter.content_type == "__sessionId":
                    session_id_payload = StringValuePayload()
                    parameter.content.Unpack(session_id_payload)
                    session_id = session_id_payload.value

        parameters = {}
        parameters['parameters'] = params

    metadata = {}
    for key in ctx.metadata.keys():
        metadata[key] = ctx.metadata[key]

    logger.info(f"Parameters : {parameters}")

    info = get_workflow_info(request.workflow_id)
    if info is None:
        return (False, True, None, f"Workflow with id {request.workflow_id} not found")

    mp_ctx = mp.get_context('spawn')
    input_q = mp_ctx.Queue()
    output_q = mp_ctx.Queue()
    done_event = mp_ctx.Event()

    p = mp_ctx.Process(target=_run, args=(input_q, output_q, done_event))
    try:
        p.start()
        input_q.put((info, parameters, metadata, context_id, session_id))
        while not done_event.is_set() or not output_q.empty():
            if ctx.cancellation_token.is_cancelled():
                p.terminate()
                time.sleep(0.5)
                if p.is_alive():
                    p.kill()
                yield (False, True, None, "Run script cancelled")
                break
            while not output_q.empty():
                yield output_q.get()
            time.sleep(0.25)
            if not p.is_alive() and p.exitcode != 0:
                logger.warning(f"Workflow terminated for unknown reason: exitcode {p.exitcode}")
                yield (False, True, None, f"Workflow terminated for unknown reason: exitcode {p.exitcode}")
                break
        p.join()
    except Exception as error:
        logger.error(f"Run workflow request: {error} {error.args}")
        yield (False, True, None, f"Workflow terminated for unknown reason: exitcode {p.exitcode}")
    finally:
        p.close()
