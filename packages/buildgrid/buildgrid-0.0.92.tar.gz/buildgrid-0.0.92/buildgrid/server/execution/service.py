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
ExecutionService
================

Serves remote execution requests.
"""

import logging
from typing import Iterable, Iterator, Union, cast

import grpc

from buildgrid._exceptions import CancelledError, RetriableError
from buildgrid._protos.build.bazel.remote.execution.v2.remote_execution_pb2 import DESCRIPTOR as RE_DESCRIPTOR
from buildgrid._protos.build.bazel.remote.execution.v2.remote_execution_pb2 import ExecuteRequest, WaitExecutionRequest
from buildgrid._protos.build.bazel.remote.execution.v2.remote_execution_pb2_grpc import (
    ExecutionServicer,
    add_ExecutionServicer_to_server,
)
from buildgrid._protos.google.longrunning import operations_pb2
from buildgrid.server.auth.manager import authorize_unary_stream
from buildgrid.server.execution.instance import ExecutionInstance
from buildgrid.server.metrics_names import (
    EXECUTE_EXCEPTION_COUNT_METRIC_NAME,
    EXECUTE_REQUEST_COUNT_METRIC_NAME,
    EXECUTE_SERVICER_TIME_METRIC_NAME,
    WAIT_EXECUTION_EXCEPTION_COUNT_METRIC_NAME,
    WAIT_EXECUTION_REQUEST_COUNT_METRIC_NAME,
    WAIT_EXECUTION_SERVICER_TIME_METRIC_NAME,
)
from buildgrid.server.metrics_utils import (
    Counter,
    generator_method_duration_metric,
    generator_method_exception_counter,
)
from buildgrid.server.request_metadata_utils import (
    extract_client_identity,
    extract_request_metadata,
    printable_client_identity,
    printable_request_metadata,
)
from buildgrid.server.servicer import InstancedServicer
from buildgrid.server.utils.context import CancellationContext
from buildgrid.server.utils.decorators import handle_errors_unary_stream, track_request_id_generator

LOGGER = logging.getLogger(__name__)


def _parse_instance_name(operation_name: str) -> str:
    names = operation_name.split("/")
    return "/".join(names[:-1])


class ExecutionService(ExecutionServicer, InstancedServicer[ExecutionInstance]):
    REGISTER_METHOD = add_ExecutionServicer_to_server
    FULL_NAME = RE_DESCRIPTOR.services_by_name["Execution"].full_name

    execute_ignored_exceptions = (RetriableError,)

    @authorize_unary_stream(lambda r: cast(str, r.instance_name))
    @track_request_id_generator
    @generator_method_duration_metric(EXECUTE_SERVICER_TIME_METRIC_NAME)
    @generator_method_exception_counter(
        EXECUTE_EXCEPTION_COUNT_METRIC_NAME,
        ignored_exceptions=execute_ignored_exceptions,
    )
    @handle_errors_unary_stream(operations_pb2.Operation)
    def Execute(self, request: ExecuteRequest, context: grpc.ServicerContext) -> Iterator[operations_pb2.Operation]:
        """Handles ExecuteRequest messages.

        Args:
            request (ExecuteRequest): The incoming RPC request.
            context (grpc.ServicerContext): Context for the RPC call.
        """
        LOGGER.info(
            f"Execute request from [{context.peer()}] "
            f"([{printable_request_metadata(context.invocation_metadata())}]) "
            f"([{printable_client_identity(request.instance_name, context.invocation_metadata())}])"
        )

        instance_name = request.instance_name

        with Counter(metric_name=EXECUTE_REQUEST_COUNT_METRIC_NAME, instance_name=instance_name) as num_requests:
            num_requests.increment(1)

        yield from self._handle_request(request, context, instance_name)

    wait_execution_ignored_exceptions = (RetriableError,)

    @authorize_unary_stream(lambda r: _parse_instance_name(r.name))
    @track_request_id_generator
    @generator_method_duration_metric(WAIT_EXECUTION_SERVICER_TIME_METRIC_NAME)
    @generator_method_exception_counter(
        WAIT_EXECUTION_EXCEPTION_COUNT_METRIC_NAME,
        ignored_exceptions=wait_execution_ignored_exceptions,
    )
    @handle_errors_unary_stream(operations_pb2.Operation)
    def WaitExecution(
        self, request: WaitExecutionRequest, context: grpc.ServicerContext
    ) -> Iterator[operations_pb2.Operation]:
        """Handles WaitExecutionRequest messages.

        Args:
            request (WaitExecutionRequest): The incoming RPC request.
            context (grpc.ServicerContext): Context for the RPC call.
        """
        LOGGER.info(
            f"WaitExecution request from [{context.peer()}] "
            f"([{printable_request_metadata(context.invocation_metadata())}])"
        )

        instance_name = _parse_instance_name(request.name)

        with Counter(
            metric_name=WAIT_EXECUTION_REQUEST_COUNT_METRIC_NAME, instance_name=instance_name
        ) as num_requests:
            num_requests.increment(1)

        yield from self._handle_request(request, context, instance_name)

    def query_n_clients(self) -> int:
        return sum(map(self.query_n_clients_for_instance, self.instances))

    def query_n_clients_for_instance(self, instance_name: str) -> int:
        if instance := self.instances.get(instance_name):
            return instance.scheduler.ops_notifier.listener_count()
        return 0

    def _handle_request(
        self,
        request: Union[ExecuteRequest, WaitExecutionRequest],
        context: grpc.ServicerContext,
        instance_name: str,
    ) -> Iterable[operations_pb2.Operation]:
        peer_uid = context.peer()

        try:
            instance = self.get_instance(instance_name)

            if isinstance(request, ExecuteRequest):
                request_metadata = extract_request_metadata(context.invocation_metadata())
                client_identity = extract_client_identity(instance_name, context.invocation_metadata())
                operation_name = instance.execute(
                    action_digest=request.action_digest,
                    skip_cache_lookup=request.skip_cache_lookup,
                    priority=request.execution_policy.priority,
                    request_metadata=request_metadata,
                    client_identity=client_identity,
                )
            else:  # isinstance(request, WaitExecutionRequest)"
                names = request.name.split("/")
                operation_name = names[-1]

            operation_full_name = f"{instance_name}/{operation_name}"

            for operation in instance.stream_operation_updates(operation_name, CancellationContext(context)):
                operation.name = operation_full_name
                yield operation

            if not context.is_active():
                LOGGER.info(
                    f"Peer peer_uid=[{peer_uid}] was holding up a thread for "
                    f"`stream_operation_updates()` for instance_name=[{instance_name}], "
                    f"operation_name=[{operation_name}], but the rpc context is not "
                    "active anymore; releasing thread."
                )

        except CancelledError as e:
            LOGGER.info(e)
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.CANCELLED)
            yield e.last_response  # type: ignore[misc]  # need a better signature
