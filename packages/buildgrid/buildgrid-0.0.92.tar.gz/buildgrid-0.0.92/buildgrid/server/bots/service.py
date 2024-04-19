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
BotsService
=================

"""

import logging
from typing import cast

import grpc
from google.protobuf import empty_pb2

from buildgrid._enums import BotStatus
from buildgrid._exceptions import InvalidArgumentError
from buildgrid._protos.google.devtools.remoteworkers.v1test2.bots_pb2 import DESCRIPTOR as BOTS_DESCRIPTOR
from buildgrid._protos.google.devtools.remoteworkers.v1test2.bots_pb2 import (
    BotSession,
    CreateBotSessionRequest,
    PostBotEventTempRequest,
    UpdateBotSessionRequest,
)
from buildgrid._protos.google.devtools.remoteworkers.v1test2.bots_pb2_grpc import (
    BotsServicer,
    add_BotsServicer_to_server,
)
from buildgrid.server.auth.manager import authorize_unary_unary
from buildgrid.server.bots.instance import BotsInterface
from buildgrid.server.metrics_names import (
    BOTS_CREATE_BOT_SESSION_TIME_METRIC_NAME,
    BOTS_UPDATE_BOT_SESSION_TIME_METRIC_NAME,
)
from buildgrid.server.metrics_utils import DurationMetric
from buildgrid.server.servicer import InstancedServicer
from buildgrid.server.utils.context import CancellationContext
from buildgrid.server.utils.decorators import handle_errors_unary_unary, track_request_id

LOGGER = logging.getLogger(__name__)


def _instance_name_from_bot_name(name: str) -> str:
    names = name.split("/")
    return "/".join(names[:-1])


class BotsService(BotsServicer, InstancedServicer[BotsInterface]):
    REGISTER_METHOD = add_BotsServicer_to_server
    FULL_NAME = BOTS_DESCRIPTOR.services_by_name["Bots"].full_name

    # --- Public API: Servicer ---
    @authorize_unary_unary(lambda r: cast(str, r.parent))
    @track_request_id
    @DurationMetric(BOTS_CREATE_BOT_SESSION_TIME_METRIC_NAME)
    @handle_errors_unary_unary(BotSession)
    def CreateBotSession(self, request: CreateBotSessionRequest, context: grpc.ServicerContext) -> BotSession:
        """Handles CreateBotSessionRequest messages.

        Args:
            request (CreateBotSessionRequest): The incoming RPC request.
            context (grpc.ServicerContext): Context for the RPC call.
        """
        LOGGER.info(f"CreateBotSession request from [{context.peer()}]")

        instance_name = request.parent
        instance = self.get_instance(instance_name)
        bot_session = instance.create_bot_session(
            request.bot_session, CancellationContext(context), deadline=context.time_remaining()
        )
        return bot_session

    @authorize_unary_unary(lambda r: _instance_name_from_bot_name(r.name))
    @track_request_id
    @DurationMetric(BOTS_UPDATE_BOT_SESSION_TIME_METRIC_NAME)
    @handle_errors_unary_unary(BotSession)
    def UpdateBotSession(self, request: UpdateBotSessionRequest, context: grpc.ServicerContext) -> BotSession:
        """Handles UpdateBotSessionRequest messages.

        Args:
            request (UpdateBotSessionRequest): The incoming RPC request.
            context (grpc.ServicerContext): Context for the RPC call.
        """
        LOGGER.debug(f"UpdateBotSession request from [{context.peer()}]")

        if request.name != request.bot_session.name:
            raise InvalidArgumentError(
                "Name in UpdateBotSessionRequest does not match BotSession. "
                f" UpdateBotSessionRequest.name=[{request.name}] BotSession.name=[{request.bot_session.name}]"
            )

        instance_name = _instance_name_from_bot_name(request.name)
        instance = self.get_instance(instance_name)
        bot_session, metadata = instance.update_bot_session(
            request.bot_session, CancellationContext(context), deadline=context.time_remaining()
        )

        context.set_trailing_metadata(metadata)  # type: ignore[arg-type]  # tricky covariance issue.

        return bot_session

    @authorize_unary_unary(lambda r: _instance_name_from_bot_name(r.name))
    @track_request_id
    def PostBotEventTemp(self, request: PostBotEventTempRequest, context: grpc.ServicerContext) -> empty_pb2.Empty:
        """Handles PostBotEventTempRequest messages.

        Args:
            request (PostBotEventTempRequest): The incoming RPC request.
            context (grpc.ServicerContext): Context for the RPC call.
        """
        LOGGER.info(f"PostBotEventTemp request from [{context.peer()}]")

        context.set_code(grpc.StatusCode.UNIMPLEMENTED)

        return empty_pb2.Empty()

    def query_n_bots(self) -> int:
        return sum(map(self.query_n_bots_for_instance, self.instances))

    def query_n_bots_for_instance(self, instance_name: str) -> int:
        if instance := self.instances.get(instance_name):
            return instance.count_bots()
        return 0

    def query_n_bots_for_status(self, bot_status: BotStatus) -> int:
        return sum(self.query_n_bots_for_instance_for_status(instance, bot_status) for instance in self.instances)

    def query_n_bots_for_instance_for_status(self, instance_name: str, bot_status: BotStatus) -> int:
        if instance := self.instances.get(instance_name):
            return instance.count_bots_by_status(bot_status)
        return 0
