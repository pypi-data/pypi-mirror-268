# Copyright (C) 2020 Bloomberg LP
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
from abc import ABC, abstractmethod
from typing import Any, Optional, TypeVar

from buildgrid._protos.build.bazel.remote.execution.v2.remote_execution_pb2 import DESCRIPTOR as RE_DESCRIPTOR
from buildgrid._protos.build.bazel.remote.execution.v2.remote_execution_pb2 import (
    ActionResult,
    Digest,
    DigestFunction,
    Directory,
    Tree,
)
from buildgrid.server.cas.instance import EMPTY_BLOB_DIGEST
from buildgrid.server.cas.storage.storage_abc import StorageABC
from buildgrid.server.servicer import Instance
from buildgrid.utils import get_hash_type

LOGGER = logging.getLogger(__name__)


T = TypeVar("T", bound="ActionCacheABC")


class ActionCacheABC(Instance, ABC):
    SERVICE_NAME = RE_DESCRIPTOR.services_by_name["ActionCache"].full_name

    def __init__(self, allow_updates: bool = False, storage: Optional[StorageABC] = None):
        self._allow_updates = allow_updates
        self._storage = storage

    @property
    def allow_updates(self) -> bool:
        return self._allow_updates

    def hash_type(self) -> "DigestFunction.Value.ValueType":
        return get_hash_type()

    def __enter__(self: T) -> T:
        self.start()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.stop()

    def start(self) -> None:
        if self._storage is not None:
            self._storage.start()

    def stop(self) -> None:
        if self._storage is not None:
            self._storage.stop()

    # NOTE: This method exists for compatibility reasons. Ideally it should never
    # be used with an up-to-date configuration.
    def set_instance_name(self, instance_name: str) -> None:
        LOGGER.warning(
            "Cache instances should be defined in a 'caches' list and passed "
            "to an ActionCache service, rather than defined in the 'services' "
            "list themselves."
        )
        super().set_instance_name(instance_name)

    @abstractmethod
    def get_action_result(self, action_digest: Digest) -> ActionResult:
        raise NotImplementedError()

    @abstractmethod
    def update_action_result(self, action_digest: Digest, action_result: ActionResult) -> None:
        raise NotImplementedError()

    def _action_result_blobs_still_exist(self, action_result: ActionResult) -> bool:
        """Checks CAS for ActionResult output blobs existence.

        Args:
            action_result (ActionResult): ActionResult to search referenced
            output blobs for.

        Returns:
            True if all referenced blobs are present in CAS, False otherwise.
        """
        if not self._storage:
            return True
        blobs_needed = []

        for output_file in action_result.output_files:
            blobs_needed.append(output_file.digest)

        for output_directory in action_result.output_directories:
            if output_directory.HasField("tree_digest"):
                blobs_needed.append(output_directory.tree_digest)
                tree = self._storage.get_message(output_directory.tree_digest, Tree)
                if tree is None:
                    return False

                for file_node in tree.root.files:
                    blobs_needed.append(file_node.digest)

                for child in tree.children:
                    for file_node in child.files:
                        blobs_needed.append(file_node.digest)
            elif output_directory.HasField("root_directory_digest"):
                # GetTree would be more efficient but that is not part of StorageABC
                queue = [output_directory.root_directory_digest]
                while queue:
                    directory_blobs = self._storage.bulk_read_blobs(queue)
                    if len(directory_blobs) < len(queue):
                        # At least one directory is missing
                        return False

                    directories = [Directory.FromString(b) for b in directory_blobs.values()]
                    blobs_needed.extend([file_node.digest for d in directories for file_node in d.files])
                    queue = [subdir.digest for d in directories for subdir in d.directories]

        if action_result.stdout_digest.hash and not action_result.stdout_raw:
            blobs_needed.append(action_result.stdout_digest)

        if action_result.stderr_digest.hash and not action_result.stderr_raw:
            blobs_needed.append(action_result.stderr_digest)

        # No need to check the underlying storage for the empty blob as it is a special case blob which always exists
        # It is possible that the empty blob is not actually present in the underlying storage
        blobs_to_check = [blob for blob in blobs_needed if blob != EMPTY_BLOB_DIGEST]

        missing = self._storage.missing_blobs(blobs_to_check)
        if len(missing) != 0:
            LOGGER.debug(f"Missing {len(missing)}/{len(blobs_needed)} blobs")
            return False
        return True
