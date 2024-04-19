# Copyright (C) 2022 Bloomberg LP
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


import logging
import threading
import uuid
from contextlib import contextmanager
from itertools import chain, combinations
from threading import Event, Lock
from typing import Any, Dict, Iterable, Iterator, List, Set, TypeVar

from buildgrid._protos.google.devtools.remoteworkers.v1test2.bots_pb2 import BotSession
from buildgrid.server.persistence.sql.impl import SQLDataStore
from buildgrid.server.threading import ContextWorker
from buildgrid.utils import convert_values_to_sorted_lists, flatten_capabilities, hash_from_dict

LOGGER = logging.getLogger(__name__)


T = TypeVar("T", bound="JobAssigner")


class JobAssigner:
    def __init__(self, data_store: SQLDataStore, job_assignment_interval: float = 1.0):
        self._lock = Lock()
        # Dict[Hash, Dict[BotName, Dict[Key, Event]]]
        self._events: Dict[str, Dict[str, Dict[str, Event]]] = {}
        self._data_store = data_store
        # Here we allow immediately starting a new assignment if a bot is added to the lookup.
        self._new_bots_added = Event()
        self._job_assignment_worker = ContextWorker(
            target=self.begin, name="JobAssignment", on_shutdown_requested=self._new_bots_added.set
        )
        self._job_assignment_interval = job_assignment_interval

    def __enter__(self: T) -> T:
        self.start()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.stop()

    def start(self) -> None:
        self._job_assignment_worker.start()

    def stop(self) -> None:
        self._job_assignment_worker.stop()

    def listener_count(self) -> int:
        with self._lock:
            return len({bot_name for bot_events in self._events.values() for bot_name in bot_events})

    @contextmanager
    def assignment_context(self, bot_session: BotSession) -> Iterator[threading.Event]:
        key = str(uuid.uuid4())
        event = Event()
        worker_hashes = get_partial_capabilities_hashes(bot_capabilities(bot_session))
        try:
            with self._lock:
                for worker_hash in worker_hashes:
                    if worker_hash not in self._events:
                        self._events[worker_hash] = {}
                    if bot_session.name not in self._events[worker_hash]:
                        self._events[worker_hash][bot_session.name] = {}
                    self._events[worker_hash][bot_session.name][key] = event
            self._new_bots_added.set()
            yield event
        finally:
            with self._lock:
                for worker_hash in worker_hashes:
                    del self._events[worker_hash][bot_session.name][key]
                    if len(self._events[worker_hash][bot_session.name]) == 0:
                        del self._events[worker_hash][bot_session.name]
                    if len(self._events[worker_hash]) == 0:
                        del self._events[worker_hash]

    def assign_jobs(self, shutdown_requested: threading.Event) -> None:
        """Assign jobs to the currently connected workers

        This method iterates over the buckets of currently connected workers,
        and requests a number of job assignments from the data store to cover
        the number of workers in each bucket. Empty buckets are skipped.
        """

        with self._lock:
            worker_hashes = set(self._events)

        for worker_hash in worker_hashes:
            if shutdown_requested.is_set():
                return

            with self._lock:
                bot_names = list(self._events.get(worker_hash, {}))

            if bot_names:
                assigned_bot_names = self._data_store.assign_n_leases(capability_hash=worker_hash, bot_names=bot_names)
                with self._lock:
                    for name in assigned_bot_names:
                        for event in self._events.get(worker_hash, {}).get(name, {}).values():
                            event.set()

    def begin(self, shutdown_requested: threading.Event) -> None:
        while not shutdown_requested.is_set():
            try:
                self.assign_jobs(shutdown_requested)
            except Exception:
                LOGGER.exception("Error in job assignment thread", exc_info=True)
            self._new_bots_added.wait(timeout=self._job_assignment_interval)
            self._new_bots_added.clear()


def get_partial_capabilities(capabilities: Dict[str, List[str]]) -> Iterable[Dict[str, List[str]]]:
    """
    Given a capabilities dictionary with all values as lists, yield all partial capabilities dictionaries.
    """

    CAPABILITIES_WARNING_THRESHOLD = 10

    caps_flat = flatten_capabilities(capabilities)

    if len(caps_flat) > CAPABILITIES_WARNING_THRESHOLD:
        LOGGER.warning(
            "A worker with a large capabilities dictionary has been connected. "
            f"Processing its capabilities may take a while. Capabilities: {capabilities}"
        )

    # Using the itertools powerset recipe, construct the powerset of the tuples
    capabilities_powerset = chain.from_iterable(combinations(caps_flat, r) for r in range(len(caps_flat) + 1))
    for partial_capability_tuples in capabilities_powerset:
        partial_dict: Dict[str, List[str]] = {}

        for tup in partial_capability_tuples:
            partial_dict.setdefault(tup[0], []).append(tup[1])
        yield partial_dict


def get_partial_capabilities_hashes(capabilities: Dict[str, Set[str]]) -> List[str]:
    """
    Given a list of configurations, obtain each partial configuration for each configuration,
    obtain the hash of each partial configuration, compile these into a list, and return the result.
    """

    # Convert requirements values to sorted lists to make them json-serializable
    normalized_capabilities = convert_values_to_sorted_lists(capabilities)

    capabilities_list = []
    for partial_capability in get_partial_capabilities(normalized_capabilities):
        capabilities_list.append(hash_from_dict(partial_capability))
    return capabilities_list


def bot_capabilities(bot_session: BotSession) -> Dict[str, Set[str]]:
    worker_capabilities: Dict[str, Set[str]] = {}
    if bot_session.worker.devices:
        # According to the spec:
        #   "The first device in the worker is the "primary device" -
        #   that is, the device running a bot and which is
        #   responsible for actually executing commands."
        primary_device = bot_session.worker.devices[0]

        for device_property in primary_device.properties:
            if device_property.key not in worker_capabilities:
                worker_capabilities[device_property.key] = set()
            worker_capabilities[device_property.key].add(device_property.value)
    return worker_capabilities
