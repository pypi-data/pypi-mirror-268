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
BotsInterface
=================

Instance of the Remote Workers interface.
"""
import logging
import threading
from contextlib import ExitStack
from typing import List, Optional, Tuple

from buildgrid._enums import BotStatus
from buildgrid._exceptions import InvalidArgumentError, RetriableError
from buildgrid._protos.google.devtools.remoteworkers.v1test2.bots_pb2 import DESCRIPTOR as BOTS_DESCRIPTOR
from buildgrid._protos.google.devtools.remoteworkers.v1test2.bots_pb2 import BotSession, Lease
from buildgrid.server.bots.job_assigner import JobAssigner
from buildgrid.server.metrics_names import (
    BOTS_CREATE_BOT_SESSION_EXCEPTION_COUNT_METRIC_NAME,
    BOTS_CREATE_BOT_SESSION_TIME_METRIC_NAME,
    BOTS_UPDATE_BOT_SESSION_EXCEPTION_COUNT_METRIC_NAME,
    BOTS_UPDATE_BOT_SESSION_TIME_METRIC_NAME,
)
from buildgrid.server.metrics_utils import DurationMetric, ExceptionCounter
from buildgrid.server.persistence.sql.impl import SQLDataStore
from buildgrid.server.servicer import Instance
from buildgrid.server.threading import ContextWorker
from buildgrid.server.utils.context import CancellationContext
from buildgrid.settings import MAX_WORKER_TTL, NETWORK_TIMEOUT

LOGGER = logging.getLogger(__name__)


class BotsInterface(Instance):
    SERVICE_NAME = BOTS_DESCRIPTOR.services_by_name["Bots"].full_name

    def __init__(
        self,
        scheduler: SQLDataStore,
        *,
        job_assignment_interval: float = 1.0,
    ) -> None:
        self._stack = ExitStack()

        self._job_assigner = JobAssigner(scheduler, job_assignment_interval=job_assignment_interval)
        self.scheduler = scheduler

        # Set the deadline event on worker stop to allow fast exit
        self.reaper = ContextWorker(self._reap_expired_sessions_loop, "BotReaper")

    def start(self) -> None:
        self._stack.enter_context(self.scheduler)
        self._stack.enter_context(self._job_assigner)
        self._stack.enter_context(self.reaper)

    def stop(self) -> None:
        self._stack.close()

    def set_instance_name(self, instance_name: str) -> None:
        super().set_instance_name(instance_name)
        self.scheduler.set_instance_name(instance_name)

    create_bot_session_ignored_exceptions = (RetriableError,)

    @DurationMetric(BOTS_CREATE_BOT_SESSION_TIME_METRIC_NAME, instanced=True)
    @ExceptionCounter(
        BOTS_CREATE_BOT_SESSION_EXCEPTION_COUNT_METRIC_NAME, ignored_exceptions=create_bot_session_ignored_exceptions
    )
    def create_bot_session(
        self, bot_session: BotSession, context: CancellationContext, deadline: Optional[float] = None
    ) -> BotSession:
        """Creates a new bot session. Server should assign a unique
        name to the session. If the bot_id already exists in the database
        then any leases already assigned to that id are requeued
        (via close_bot_session) and then the name previously associated with
        the bot_id is replaced with the new name in the database. If the bot_id
        is not in the database, a new record is created.
        """
        if not bot_session.bot_id:
            raise InvalidArgumentError("Bot's id must be set by client.")

        # Create new record
        bot_session.name = self.scheduler.add_bot_entry(
            bot_session_id=bot_session.bot_id, bot_session_status=bot_session.status
        )

        LOGGER.info(f"Opened BotSession name=[{bot_session.name}] for bot_id=[{bot_session.bot_id}].")

        self._request_leases(bot_session, context, deadline=deadline)

        leases = ",".join(lease.id[:8] for lease in bot_session.leases)
        LOGGER.debug(
            f"Leases assigned to newly opened BotSession name=[{bot_session.name}] "
            f"for bot_id=[{bot_session.bot_id}]: [{leases}]."
        )

        # Update status for bot session
        self._assign_deadline_for_botsession(bot_session)

        return bot_session

    update_bot_session_ignored_exceptions = (RetriableError,)

    @DurationMetric(BOTS_UPDATE_BOT_SESSION_TIME_METRIC_NAME, instanced=True)
    @ExceptionCounter(
        BOTS_UPDATE_BOT_SESSION_EXCEPTION_COUNT_METRIC_NAME, ignored_exceptions=update_bot_session_ignored_exceptions
    )
    def update_bot_session(
        self, bot_session: BotSession, context: CancellationContext, deadline: Optional[float] = None
    ) -> Tuple[BotSession, List[Tuple[str, bytes]]]:
        """Client updates the server. Any changes in state to the Lease should be
        registered server side. Assigns available leases with work.
        """

        orig_lease: Optional[Lease] = None
        if bot_session.leases:
            orig_lease = bot_session.leases.pop()
        if updated_lease := self.scheduler.synchronize_bot_lease(
            bot_session.name, bot_session.bot_id, bot_session.status, orig_lease
        ):
            bot_session.leases.append(updated_lease)

        # Don't request new leases if a lease was removed. This mitigates situations where the scheduler
        # is updated with the new state of the lease, but a fault thereafter causes the worker to retry
        # the old UpdateBotSession call
        if not orig_lease and not updated_lease:
            self._request_leases(bot_session, context, deadline=deadline)

        metadata = self.scheduler.get_metadata_for_leases(bot_session.leases)

        leases = ",".join(lease.id[:8] for lease in bot_session.leases)
        LOGGER.debug(
            f"Sending BotSession update for name=[{bot_session.name}], "
            f"bot_id=[{bot_session.bot_id}]: leases=[{leases}]."
        )

        self._assign_deadline_for_botsession(bot_session)

        return bot_session, metadata

    def count_bots(self) -> int:
        return self.scheduler.count_bots()

    def count_bots_by_status(self, status: BotStatus) -> int:
        return self.scheduler.count_bots_by_status(status)

    def _assign_deadline_for_botsession(self, bot_session: BotSession) -> None:
        bot_session.expire_time.FromDatetime(self.scheduler.get_bot_expiry_time(bot_session.name, bot_session.bot_id))

    def _request_leases(
        self,
        bot_session: BotSession,
        context: CancellationContext,
        deadline: Optional[float] = None,
    ) -> None:
        # Only send one lease at a time currently.
        if bot_session.status != BotStatus.OK.value or bot_session.leases:
            return

        # If no deadline is set default to the max we allow workers to
        # long-poll for work
        if deadline is None:
            deadline = MAX_WORKER_TTL

        # If the specified bot session keepalive timeout is greater than the
        # deadline it can result in active bot sessions being reaped
        deadline = min(deadline, self.scheduler.bot_session_keepalive_timeout)

        # Use 80% of the given deadline to give time to respond
        # but no less than NETWORK_TIMEOUT
        ttl = deadline * 0.8
        if ttl < NETWORK_TIMEOUT:
            LOGGER.info(
                f"BotSession name=[{bot_session.name}] expires in less time than "
                f"NETWORK_TIMEOUT=[{NETWORK_TIMEOUT}], no leases will be assigned"
            )
            return

        # Wait for an update to the bot session and then resynchronize the lease.
        with self._job_assigner.assignment_context(bot_session) as event:
            context.on_cancel(event.set)
            event.wait(ttl)

        # Synchronize the lease again to pick up db changes.
        if lease := self.scheduler.synchronize_bot_lease(
            bot_session.name, bot_session.bot_id, bot_session.status, None
        ):
            bot_session.leases.append(lease)

    def _reap_expired_sessions_loop(self, shutdown_requested: threading.Event) -> None:
        LOGGER.info(
            "Starting BotSession reaper, "
            f"bot_session_keepalive_timeout=[{self.scheduler.bot_session_keepalive_timeout}]"
        )
        while not shutdown_requested.is_set():
            try:
                while self.scheduler.reap_expired_sessions():
                    if shutdown_requested.is_set():
                        break
            except Exception as exception:
                LOGGER.exception(exception)
            shutdown_requested.wait(timeout=self.scheduler.poll_interval)
