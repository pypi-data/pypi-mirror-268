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
StorageABC
==================

The abstract base class for storage providers.
"""

import abc
import io
import logging
from tempfile import TemporaryFile
from typing import IO, Any, Dict, List, Optional, Tuple, Type, TypeVar

from buildgrid._protos.build.bazel.remote.execution.v2 import remote_execution_pb2
from buildgrid._protos.build.bazel.remote.execution.v2.remote_execution_pb2 import (
    CacheCapabilities,
    Digest,
    SymlinkAbsolutePathStrategy,
)
from buildgrid._protos.google.rpc import code_pb2
from buildgrid._protos.google.rpc.status_pb2 import Status
from buildgrid._types import MessageType
from buildgrid.settings import HASH, MAX_IN_MEMORY_BLOB_SIZE_BYTES, MAX_REQUEST_SIZE
from buildgrid.utils import get_hash_type

LOGGER = logging.getLogger(__name__)

M = TypeVar("M", bound=MessageType)


def create_write_session(digest: Digest) -> IO[bytes]:
    """
    Return a file-like object to which a blob's contents could be written.

    For large files, to avoid excess memory usage, upload to temporary file.
    For small files we can work in memory for performance.
    """

    if digest.size_bytes > MAX_IN_MEMORY_BLOB_SIZE_BYTES:
        return TemporaryFile()
    return io.BytesIO()


T = TypeVar("T", bound="StorageABC")


class StorageABC(abc.ABC):
    def __enter__(self: T) -> T:
        self.start()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.stop()

    def start(self) -> None:
        pass

    def stop(self) -> None:
        pass

    @abc.abstractmethod
    def has_blob(self, digest: Digest) -> bool:
        """Return True if the blob with the given instance/digest exists."""
        raise NotImplementedError()

    @abc.abstractmethod
    def get_blob(self, digest: Digest) -> Optional[IO[bytes]]:
        """Return a file-like object containing the blob. Most implementations
        will read the entire file into memory and return a `BytesIO` object.
        Eventually this should be corrected to handle files which cannot fit
        into memory.

        The file-like object must be readable and seekable.

        If the blob isn't present in storage, return None.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def delete_blob(self, digest: Digest) -> None:
        """Delete the blob from storage if it's present."""

    @abc.abstractmethod
    def commit_write(self, digest: Digest, write_session: IO[bytes]) -> None:
        """Store the contents for a digest.

        The storage object is not responsible for verifying that the data
        written to the write_session actually matches the digest. The caller
        must do that.
        """
        raise NotImplementedError()

    def bulk_delete(self, digests: List[Digest]) -> List[str]:
        """Delete a list of blobs from storage."""
        failed_deletions = []
        for digest in digests:
            try:
                self.delete_blob(digest)
            except Exception:
                # If deletion threw an exception, assume deletion failed. More specific implementations
                # with more information can return if a blob was missing instead
                LOGGER.warning(f"Unable to clean up digest [{digest.hash}/{digest.size_bytes}]", exc_info=True)
                failed_deletions.append(f"{digest.hash}/{digest.size_bytes}")
        return failed_deletions

    def missing_blobs(self, digests: List[Digest]) -> List[Digest]:
        """Return a container containing the blobs not present in CAS."""
        result = []
        for digest in digests:
            if not self.has_blob(digest):
                result.append(digest)
        return result

    def bulk_update_blobs(self, blobs: List[Tuple[Digest, bytes]]) -> List[Status]:
        """Given a container of (digest, value) tuples, add all the blobs
        to CAS. Return a list of Status objects corresponding to the
        result of uploading each of the blobs.

        Unlike in `commit_write`, the storage object will verify that each of
        the digests matches the provided data.
        """
        result = []
        for digest, data in blobs:
            if len(data) != digest.size_bytes or HASH(data).hexdigest() != digest.hash:
                result.append(Status(code=code_pb2.INVALID_ARGUMENT, message="Data doesn't match hash"))
                continue
            try:
                with create_write_session(digest) as write_session:
                    write_session.write(data)
                    self.commit_write(digest, write_session)
                result.append(Status(code=code_pb2.OK))
            except IOError as ex:
                result.append(Status(code=code_pb2.UNKNOWN, message=str(ex)))
        return result

    def bulk_read_blobs(self, digests: List[Digest]) -> Dict[str, bytes]:
        """Given an iterable container of digests, return a
        {hash: file-like object} dictionary corresponding to the blobs
        represented by the input digests.

        Each file-like object must be readable and seekable.
        """

        blobmap = {}
        for digest in digests:
            blob = self.get_blob(digest)
            if blob is not None:
                with blob as b:
                    blobmap[digest.hash] = b.read()
        return blobmap

    def put_message(self, message: MessageType) -> Digest:
        """Store the given Protobuf message in CAS, returning its digest."""
        message_blob = message.SerializeToString()
        digest = Digest(hash=HASH(message_blob).hexdigest(), size_bytes=len(message_blob))
        with create_write_session(digest) as session:
            session.write(message_blob)
            self.commit_write(digest, session)
        return digest

    def get_message(self, digest: Digest, message_type: Type[M]) -> Optional[M]:
        """Retrieve the Protobuf message with the given digest and type from
        CAS. If the blob is not present, returns None.
        """
        message_blob = self.get_blob(digest)
        if message_blob is None:
            return None
        try:
            return message_type.FromString(message_blob.read())
        finally:
            message_blob.close()

    @property
    def instance_name(self) -> Optional[str]:
        if hasattr(self, "_instance_name"):
            return self._instance_name
        return None

    def set_instance_name(self, instance_name: str) -> None:
        # This method should always get called, so there's no benefit in
        # adding an __init__ to this abstract class (therefore adding the
        # need for subclasses to call `super()`) just to define a null
        # value for this.
        self._instance_name: Optional[str] = instance_name

    def hash_type(self) -> "remote_execution_pb2.DigestFunction.Value.ValueType":
        return get_hash_type()

    def max_batch_total_size_bytes(self) -> int:
        return MAX_REQUEST_SIZE

    def symlink_absolute_path_strategy(self) -> "SymlinkAbsolutePathStrategy.Value.ValueType":
        # Currently this strategy is hardcoded into BuildGrid
        # With no setting to reference
        return SymlinkAbsolutePathStrategy.DISALLOWED

    def get_capabilities(self) -> CacheCapabilities:
        capabilities = CacheCapabilities()
        capabilities.digest_functions.extend([self.hash_type()])
        capabilities.max_batch_total_size_bytes = self.max_batch_total_size_bytes()
        capabilities.symlink_absolute_path_strategy = self.symlink_absolute_path_strategy()
        return capabilities
