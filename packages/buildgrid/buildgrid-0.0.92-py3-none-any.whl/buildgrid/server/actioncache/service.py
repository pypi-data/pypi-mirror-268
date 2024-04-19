# Copyright (C) 2018 Bloomberg LP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  <http://www.apache.org/licenses/LICENSE-2.0>
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""
ActionCacheService
==================

Allows clients to manually query/update the action cache.
"""

import logging
from typing import Union, cast

import grpc

import buildgrid.server.context as context_module
from buildgrid._exceptions import NotFoundError
from buildgrid._protos.build.bazel.remote.execution.v2.remote_execution_pb2 import DESCRIPTOR as RE_DESCRIPTOR
from buildgrid._protos.build.bazel.remote.execution.v2.remote_execution_pb2 import (
    ActionResult,
    GetActionResultRequest,
    UpdateActionResultRequest,
)
from buildgrid._protos.build.bazel.remote.execution.v2.remote_execution_pb2_grpc import (
    ActionCacheServicer,
    add_ActionCacheServicer_to_server,
)
from buildgrid.server.actioncache.caches.action_cache_abc import ActionCacheABC
from buildgrid.server.actioncache.instance import ActionCache
from buildgrid.server.auth.manager import authorize_unary_unary
from buildgrid.server.metrics_names import (
    AC_CACHE_HITS_METRIC_NAME,
    AC_CACHE_MISSES_METRIC_NAME,
    AC_GET_ACTION_RESULT_TIME_METRIC_NAME,
    AC_UPDATE_ACTION_RESULT_TIME_METRIC_NAME,
)
from buildgrid.server.metrics_utils import DurationMetric, publish_counter_metric
from buildgrid.server.request_metadata_utils import printable_request_metadata
from buildgrid.server.servicer import InstancedServicer
from buildgrid.server.utils.decorators import handle_errors_unary_unary, track_request_id

LOGGER = logging.getLogger(__name__)


class ActionCacheService(ActionCacheServicer, InstancedServicer[Union[ActionCache, ActionCacheABC]]):
    REGISTER_METHOD = add_ActionCacheServicer_to_server
    FULL_NAME = RE_DESCRIPTOR.services_by_name["ActionCache"].full_name

    @authorize_unary_unary(lambda r: cast(str, r.instance_name))
    @context_module.metadatacontext()
    @track_request_id
    @handle_errors_unary_unary(ActionResult)
    def GetActionResult(self, request: GetActionResultRequest, context: grpc.ServicerContext) -> ActionResult:
        LOGGER.info(
            f"GetActionResult request from [{context.peer()}] "
            f"([{printable_request_metadata(context.invocation_metadata())}])"
        )

        try:
            instance = self.get_instance(request.instance_name)
            with DurationMetric(AC_GET_ACTION_RESULT_TIME_METRIC_NAME, request.instance_name, instanced=True):
                action_result = instance.get_action_result(request.action_digest)
            publish_counter_metric(AC_CACHE_HITS_METRIC_NAME, 1, {"instance-name": request.instance_name})
            return action_result

        except NotFoundError:
            publish_counter_metric(AC_CACHE_MISSES_METRIC_NAME, 1, {"instance-name": request.instance_name})
            raise

    @authorize_unary_unary(lambda r: cast(str, r.instance_name))
    @context_module.metadatacontext()
    @track_request_id
    @handle_errors_unary_unary(ActionResult)
    def UpdateActionResult(self, request: UpdateActionResultRequest, context: grpc.ServicerContext) -> ActionResult:
        LOGGER.info(
            f"UpdateActionResult request from [{context.peer()}] "
            f"([{printable_request_metadata(context.invocation_metadata())}])"
        )

        instance = self.get_instance(request.instance_name)
        with DurationMetric(AC_UPDATE_ACTION_RESULT_TIME_METRIC_NAME, request.instance_name, instanced=True):
            instance.update_action_result(request.action_digest, request.action_result)
        return request.action_result
