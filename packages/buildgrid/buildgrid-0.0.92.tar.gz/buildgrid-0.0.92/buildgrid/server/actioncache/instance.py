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
Action Cache
============

Implements an in-memory action Cache
"""

import logging

from buildgrid._exceptions import NotFoundError, RetriableError
from buildgrid._protos.build.bazel.remote.execution.v2.remote_execution_pb2 import DESCRIPTOR as RE_DESCRIPTOR
from buildgrid._protos.build.bazel.remote.execution.v2.remote_execution_pb2 import ActionResult, Digest, DigestFunction
from buildgrid.server.actioncache.caches.action_cache_abc import ActionCacheABC
from buildgrid.server.metrics_names import (
    AC_GET_ACTION_RESULT_EXCEPTION_COUNT_METRIC_NAME,
    AC_UPDATE_ACTION_RESULT_EXCEPTION_COUNT_METRIC_NAME,
)
from buildgrid.server.metrics_utils import ExceptionCounter
from buildgrid.server.servicer import Instance
from buildgrid.utils import get_hash_type

LOGGER = logging.getLogger(__name__)


class ActionCache(Instance):
    SERVICE_NAME = RE_DESCRIPTOR.services_by_name["ActionCache"].full_name

    def __init__(self, cache: ActionCacheABC) -> None:
        """Initialises a new ActionCache instance.

        Args:
            cache (ActionCacheABC): The cache to use to store results.

        """
        self._cache = cache

    # --- Public API ---

    def start(self) -> None:
        self._cache.start()

    def stop(self) -> None:
        self._cache.stop()

    @property
    def allow_updates(self) -> bool:
        return self._cache.allow_updates

    def hash_type(self) -> "DigestFunction.Value.ValueType":
        return get_hash_type()

    def set_instance_name(self, instance_name: str) -> None:
        super().set_instance_name(instance_name)
        self._cache.set_instance_name(instance_name)

    get_action_ignored_exceptions = (NotFoundError, RetriableError)

    @ExceptionCounter(
        AC_GET_ACTION_RESULT_EXCEPTION_COUNT_METRIC_NAME, ignored_exceptions=get_action_ignored_exceptions
    )
    def get_action_result(self, action_digest: Digest) -> ActionResult:
        """Retrieves the cached result for an Action.

        If there is no cached result found, returns None.

        Args:
            action_digest (Digest): The digest of the Action to retrieve the
                cached result of.

        """
        return self._cache.get_action_result(action_digest)

    update_action_ignored_exceptions = (NotFoundError, RetriableError)

    @ExceptionCounter(
        AC_UPDATE_ACTION_RESULT_EXCEPTION_COUNT_METRIC_NAME, ignored_exceptions=update_action_ignored_exceptions
    )
    def update_action_result(self, action_digest: Digest, action_result: ActionResult) -> None:
        """Stores a result for an Action in the cache.

        If the result has a non-zero exit code and `cache_failed_actions` is False
        for this cache, the result is not cached.

        Args:
            action_digest (Digest): The digest of the Action whose result is
                being cached.
            action_result (ActionResult): The result to cache for the given
                Action digest.

        """
        self._cache.update_action_result(action_digest, action_result)
