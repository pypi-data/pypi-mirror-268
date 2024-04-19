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
OperationsService
=================

"""

import logging
from typing import Dict, Tuple, cast

import grpc
from google.protobuf.empty_pb2 import Empty

from buildgrid._exceptions import InvalidArgumentError
from buildgrid._protos.google.longrunning.operations_pb2 import DESCRIPTOR as OPS_DESCRIPTOR
from buildgrid._protos.google.longrunning.operations_pb2 import (
    CancelOperationRequest,
    DeleteOperationRequest,
    GetOperationRequest,
    ListOperationsRequest,
    ListOperationsResponse,
    Operation,
)
from buildgrid._protos.google.longrunning.operations_pb2_grpc import (
    OperationsServicer,
    add_OperationsServicer_to_server,
)
from buildgrid.server.auth.manager import authorize_unary_unary
from buildgrid.server.metrics_names import (
    OPERATIONS_CANCEL_OPERATION_TIME_METRIC_NAME,
    OPERATIONS_DELETE_OPERATION_TIME_METRIC_NAME,
    OPERATIONS_GET_OPERATION_TIME_METRIC_NAME,
    OPERATIONS_LIST_OPERATIONS_TIME_METRIC_NAME,
)
from buildgrid.server.metrics_utils import DurationMetric
from buildgrid.server.operations.instance import OperationsInstance
from buildgrid.server.request_metadata_utils import request_metadata_from_scheduler_dict
from buildgrid.server.servicer import InstancedServicer
from buildgrid.server.utils.decorators import handle_errors_unary_unary, track_request_id
from buildgrid.settings import REQUEST_METADATA_HEADER_NAME

LOGGER = logging.getLogger(__name__)


def _parse_instance_name(operation_name: str) -> str:
    names = operation_name.split("/")
    return "/".join(names[:-1]) if len(names) > 1 else ""


def _parse_operation_name(name: str) -> str:
    names = name.split("/")
    return names[-1] if len(names) > 1 else name


class OperationsService(OperationsServicer, InstancedServicer[OperationsInstance]):
    REGISTER_METHOD = add_OperationsServicer_to_server
    FULL_NAME = OPS_DESCRIPTOR.services_by_name["Operations"].full_name

    @authorize_unary_unary(lambda r: _parse_instance_name(r.name))
    @track_request_id
    @DurationMetric(OPERATIONS_GET_OPERATION_TIME_METRIC_NAME)
    @handle_errors_unary_unary(Operation)
    def GetOperation(self, request: GetOperationRequest, context: grpc.ServicerContext) -> Operation:
        LOGGER.info(f"GetOperation request from [{context.peer()}]")

        instance_name = _parse_instance_name(request.name)
        instance = self.get_instance(instance_name)

        operation_name = _parse_operation_name(request.name)
        operation, metadata = instance.get_operation(operation_name)
        op = Operation()
        op.CopyFrom(operation)
        op.name = request.name

        if metadata is not None:
            metadata_entry = self._operation_request_metadata_entry(metadata)
            context.set_trailing_metadata([metadata_entry])  # type: ignore[arg-type]  # tricky covariance issue

        return op

    @authorize_unary_unary(lambda r: cast(str, r.name))
    @track_request_id
    @DurationMetric(OPERATIONS_LIST_OPERATIONS_TIME_METRIC_NAME)
    @handle_errors_unary_unary(ListOperationsResponse)
    def ListOperations(self, request: ListOperationsRequest, context: grpc.ServicerContext) -> ListOperationsResponse:
        LOGGER.info(f"ListOperations request from [{context.peer()}]")

        # The request name should be the collection name
        # In our case, this is just the instance name
        instance = self.get_instance(request.name)
        result = instance.list_operations(request.filter, request.page_size, request.page_token)

        for operation in result.operations:
            operation.name = f"{request.name}/{operation.name}"

        return result

    @authorize_unary_unary(lambda r: _parse_instance_name(r.name))
    @track_request_id
    @DurationMetric(OPERATIONS_DELETE_OPERATION_TIME_METRIC_NAME)
    @handle_errors_unary_unary(Empty)
    def DeleteOperation(self, request: DeleteOperationRequest, context: grpc.ServicerContext) -> Empty:
        LOGGER.info(f"DeleteOperation request from [{context.peer()}]")

        context.set_details("BuildGrid does not support DeleteOperation.")
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        return Empty()

    @authorize_unary_unary(lambda r: _parse_instance_name(r.name))
    @track_request_id
    @DurationMetric(OPERATIONS_CANCEL_OPERATION_TIME_METRIC_NAME)
    @handle_errors_unary_unary(Empty)
    def CancelOperation(self, request: CancelOperationRequest, context: grpc.ServicerContext) -> Empty:
        LOGGER.info(f"CancelOperation request from [{context.peer()}]")

        operation_name = _parse_operation_name(request.name)
        instance_name = _parse_instance_name(request.name)
        instance = self.get_instance(instance_name)
        instance.cancel_operation(operation_name)

        return Empty()

    # --- Private API ---

    def get_instance(self, instance_name: str) -> "OperationsInstance":
        try:
            return self.instances[instance_name]
        except KeyError:
            raise InvalidArgumentError(
                f"Instance doesn't exist on server: [{instance_name}] "
                '(operation ids have the form "instance_name/operation_uuid")'
            )

    @staticmethod
    def _operation_request_metadata_entry(operation_metadata: Dict[str, str]) -> Tuple[str, bytes]:
        request_metadata = request_metadata_from_scheduler_dict(operation_metadata)
        return REQUEST_METADATA_HEADER_NAME, request_metadata.SerializeToString()
