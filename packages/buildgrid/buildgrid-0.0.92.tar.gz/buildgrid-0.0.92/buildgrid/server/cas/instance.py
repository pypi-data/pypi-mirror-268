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
Storage Instances
=================
Instances of CAS and ByteStream
"""

import logging
from datetime import timedelta
from typing import Iterable, Iterator, Optional, Sequence, Tuple

from cachetools import TTLCache
from grpc import RpcError

from buildgrid._exceptions import (
    InvalidArgumentError,
    NotFoundError,
    OutOfRangeError,
    PermissionDeniedError,
    RetriableError,
)
from buildgrid._protos.build.bazel.remote.execution.v2.remote_execution_pb2 import DESCRIPTOR as RE_DESCRIPTOR
from buildgrid._protos.build.bazel.remote.execution.v2.remote_execution_pb2 import (
    BatchReadBlobsResponse,
    BatchUpdateBlobsRequest,
    BatchUpdateBlobsResponse,
    Digest,
    DigestFunction,
    Directory,
    FindMissingBlobsResponse,
    GetTreeRequest,
    GetTreeResponse,
    SymlinkAbsolutePathStrategy,
    Tree,
)
from buildgrid._protos.google.bytestream import bytestream_pb2 as bs_pb2
from buildgrid._protos.google.rpc import code_pb2, status_pb2
from buildgrid.server.cas.storage.storage_abc import StorageABC, create_write_session
from buildgrid.server.metrics_names import (
    CAS_BATCH_READ_BLOBS_EXCEPTION_COUNT_METRIC_NAME,
    CAS_BATCH_READ_BLOBS_SIZE_BYTES,
    CAS_BATCH_READ_BLOBS_TIME_METRIC_NAME,
    CAS_BATCH_UPDATE_BLOBS_EXCEPTION_COUNT_METRIC_NAME,
    CAS_BATCH_UPDATE_BLOBS_SIZE_BYTES,
    CAS_BATCH_UPDATE_BLOBS_TIME_METRIC_NAME,
    CAS_BYTESTREAM_READ_EXCEPTION_COUNT_METRIC_NAME,
    CAS_BYTESTREAM_READ_SIZE_BYTES,
    CAS_BYTESTREAM_READ_TIME_METRIC_NAME,
    CAS_BYTESTREAM_WRITE_EXCEPTION_COUNT_METRIC_NAME,
    CAS_BYTESTREAM_WRITE_SIZE_BYTES,
    CAS_BYTESTREAM_WRITE_TIME_METRIC_NAME,
    CAS_DOWNLOADED_BYTES_METRIC_NAME,
    CAS_EXCEPTION_COUNT_METRIC_NAME,
    CAS_FIND_MISSING_BLOBS_EXCEPTION_COUNT_METRIC_NAME,
    CAS_FIND_MISSING_BLOBS_NUM_MISSING_METRIC_NAME,
    CAS_FIND_MISSING_BLOBS_NUM_REQUESTED_METRIC_NAME,
    CAS_FIND_MISSING_BLOBS_PERCENT_MISSING_METRIC_NAME,
    CAS_FIND_MISSING_BLOBS_SIZE_BYTES_MISSING_METRIC_NAME,
    CAS_FIND_MISSING_BLOBS_SIZE_BYTES_REQUESTED_METRIC_NAME,
    CAS_FIND_MISSING_BLOBS_TIME_METRIC_NAME,
    CAS_GET_TREE_CACHE_HIT,
    CAS_GET_TREE_CACHE_MISS,
    CAS_GET_TREE_EXCEPTION_COUNT_METRIC_NAME,
    CAS_GET_TREE_TIME_METRIC_NAME,
    CAS_UPLOADED_BYTES_METRIC_NAME,
)
from buildgrid.server.metrics_utils import (
    Counter,
    Distribution,
    DurationMetric,
    ExceptionCounter,
    generator_method_duration_metric,
    generator_method_exception_counter,
)
from buildgrid.server.servicer import Instance
from buildgrid.settings import HASH, HASH_LENGTH, MAX_REQUEST_COUNT, STREAM_ERROR_RETRY_PERIOD
from buildgrid.utils import create_digest, get_unique_objects_by_attribute

LOGGER = logging.getLogger(__name__)

EMPTY_BLOB = b""
EMPTY_BLOB_DIGEST: Digest = create_digest(EMPTY_BLOB)


class ContentAddressableStorageInstance(Instance):
    SERVICE_NAME = RE_DESCRIPTOR.services_by_name["ContentAddressableStorage"].full_name

    def __init__(
        self,
        storage: StorageABC,
        read_only: bool = False,
        tree_cache_size: Optional[int] = None,
        tree_cache_ttl_minutes: float = 60,
    ) -> None:
        self._storage = storage
        self.__read_only = read_only

        self._tree_cache: Optional[TTLCache[Tuple[str, int], Digest]] = None
        if tree_cache_size:
            self._tree_cache = TTLCache(tree_cache_size, tree_cache_ttl_minutes * 60)

    # --- Public API ---

    @ExceptionCounter(CAS_EXCEPTION_COUNT_METRIC_NAME)
    def set_instance_name(self, instance_name: str) -> None:
        super().set_instance_name(instance_name)
        self._storage.set_instance_name(instance_name)

    def start(self) -> None:
        self._storage.start()

    def stop(self) -> None:
        self._storage.stop()

    def hash_type(self) -> "DigestFunction.Value.ValueType":
        return self._storage.hash_type()

    def max_batch_total_size_bytes(self) -> int:
        return self._storage.max_batch_total_size_bytes()

    def symlink_absolute_path_strategy(self) -> "SymlinkAbsolutePathStrategy.Value.ValueType":
        return self._storage.symlink_absolute_path_strategy()

    find_missing_blobs_ignored_exceptions = (RetriableError,)

    @DurationMetric(CAS_FIND_MISSING_BLOBS_TIME_METRIC_NAME, instanced=True)
    @ExceptionCounter(
        CAS_FIND_MISSING_BLOBS_EXCEPTION_COUNT_METRIC_NAME,
        ignored_exceptions=find_missing_blobs_ignored_exceptions,
    )
    def find_missing_blobs(self, blob_digests: Sequence[Digest]) -> FindMissingBlobsResponse:
        storage = self._storage
        blob_digests = list(get_unique_objects_by_attribute(blob_digests, "hash"))
        missing_blobs = storage.missing_blobs(blob_digests)

        num_blobs_in_request = len(blob_digests)
        if num_blobs_in_request > 0:
            num_blobs_missing = len(missing_blobs)
            percent_missing = float((num_blobs_missing / num_blobs_in_request) * 100)

            with Distribution(
                CAS_FIND_MISSING_BLOBS_NUM_REQUESTED_METRIC_NAME, instance_name=self._instance_name
            ) as metric_num_requested:
                metric_num_requested.count = float(num_blobs_in_request)

            with Distribution(
                CAS_FIND_MISSING_BLOBS_NUM_MISSING_METRIC_NAME, instance_name=self._instance_name
            ) as metric_num_missing:
                metric_num_missing.count = float(num_blobs_missing)

            with Distribution(
                CAS_FIND_MISSING_BLOBS_PERCENT_MISSING_METRIC_NAME, instance_name=self._instance_name
            ) as metric_percent_missing:
                metric_percent_missing.count = percent_missing

        for digest in blob_digests:
            with Distribution(
                CAS_FIND_MISSING_BLOBS_SIZE_BYTES_REQUESTED_METRIC_NAME, instance_name=self._instance_name
            ) as metric_requested_blob_size:
                metric_requested_blob_size.count = float(digest.size_bytes)

        for digest in missing_blobs:
            with Distribution(
                CAS_FIND_MISSING_BLOBS_SIZE_BYTES_MISSING_METRIC_NAME, instance_name=self._instance_name
            ) as metric_missing_blob_size:
                metric_missing_blob_size.count = float(digest.size_bytes)

        return FindMissingBlobsResponse(missing_blob_digests=missing_blobs)

    batch_update_blobs_ignored_exceptions = (RetriableError,)

    @DurationMetric(CAS_BATCH_UPDATE_BLOBS_TIME_METRIC_NAME, instanced=True)
    @ExceptionCounter(
        CAS_BATCH_UPDATE_BLOBS_EXCEPTION_COUNT_METRIC_NAME,
        ignored_exceptions=batch_update_blobs_ignored_exceptions,
    )
    def batch_update_blobs(self, requests: Sequence[BatchUpdateBlobsRequest.Request]) -> BatchUpdateBlobsResponse:
        if self.__read_only:
            raise PermissionDeniedError(f"CAS instance {self._instance_name} is read-only")

        storage = self._storage
        store = []
        for request_proto in get_unique_objects_by_attribute(requests, "digest.hash"):
            store.append((request_proto.digest, request_proto.data))

            with Distribution(
                CAS_BATCH_UPDATE_BLOBS_SIZE_BYTES, instance_name=self._instance_name
            ) as metric_blob_size:
                metric_blob_size.count = float(request_proto.digest.size_bytes)

        response = BatchUpdateBlobsResponse()
        statuses = storage.bulk_update_blobs(store)

        with Counter(metric_name=CAS_UPLOADED_BYTES_METRIC_NAME, instance_name=self._instance_name) as bytes_counter:
            for (digest, _), status in zip(store, statuses):
                response_proto = response.responses.add()
                response_proto.digest.CopyFrom(digest)
                response_proto.status.CopyFrom(status)
                if response_proto.status.code == 0:
                    bytes_counter.increment(response_proto.digest.size_bytes)

        return response

    batch_read_blobs_ignored_exceptions = (RetriableError,)

    @DurationMetric(CAS_BATCH_READ_BLOBS_TIME_METRIC_NAME, instanced=True)
    @ExceptionCounter(
        CAS_BATCH_READ_BLOBS_EXCEPTION_COUNT_METRIC_NAME,
        ignored_exceptions=batch_read_blobs_ignored_exceptions,
    )
    def batch_read_blobs(self, digests: Sequence[Digest]) -> BatchReadBlobsResponse:
        storage = self._storage

        max_batch_size = storage.max_batch_total_size_bytes()

        # Only process unique digests
        good_digests = []
        bad_digests = []
        requested_bytes = 0
        for digest in get_unique_objects_by_attribute(digests, "hash"):
            if len(digest.hash) != HASH_LENGTH:
                bad_digests.append(digest)
            else:
                good_digests.append(digest)
                requested_bytes += digest.size_bytes

        if requested_bytes > max_batch_size:
            raise InvalidArgumentError(
                "Combined total size of blobs exceeds "
                "server limit. "
                f"({requested_bytes} > {max_batch_size} [byte])"
            )

        if len(good_digests) > 0:
            blobs_read = storage.bulk_read_blobs(good_digests)
        else:
            blobs_read = {}

        response = BatchReadBlobsResponse()

        with Counter(metric_name=CAS_DOWNLOADED_BYTES_METRIC_NAME, instance_name=self._instance_name) as bytes_counter:
            for digest in good_digests:
                response_proto = response.responses.add()
                response_proto.digest.CopyFrom(digest)

                if digest.hash in blobs_read and blobs_read[digest.hash] is not None:
                    response_proto.data = blobs_read[digest.hash]
                    status_code = code_pb2.OK
                    bytes_counter.increment(digest.size_bytes)

                    with Distribution(
                        CAS_BATCH_READ_BLOBS_SIZE_BYTES, instance_name=self._instance_name
                    ) as metric_blob_size:
                        metric_blob_size.count = float(digest.size_bytes)
                else:
                    status_code = code_pb2.NOT_FOUND

                response_proto.status.CopyFrom(status_pb2.Status(code=status_code))

        for digest in bad_digests:
            response_proto = response.responses.add()
            response_proto.digest.CopyFrom(digest)
            status_code = code_pb2.INVALID_ARGUMENT
            response_proto.status.CopyFrom(status_pb2.Status(code=status_code))

        return response

    def lookup_tree_cache(self, root_digest: Digest) -> Optional[Tree]:
        """Find full Tree from cache"""
        if self._tree_cache is None:
            return None
        tree = None
        if response_digest := self._tree_cache.get((root_digest.hash, root_digest.size_bytes)):
            tree = self._storage.get_message(response_digest, Tree)
            if tree is None:
                self._tree_cache.pop((root_digest.hash, root_digest.size_bytes))

        metric = CAS_GET_TREE_CACHE_HIT if tree is not None else CAS_GET_TREE_CACHE_MISS
        with Counter(metric) as counter:
            counter.increment(1)
        return tree

    def put_tree_cache(self, root_digest: Digest, root: Directory, children: Iterable[Directory]) -> None:
        """Put Tree with a full list of directories into CAS"""
        if self._tree_cache is None:
            return
        tree = Tree(root=root, children=children)
        tree_digest = self._storage.put_message(tree)
        self._tree_cache[(root_digest.hash, root_digest.size_bytes)] = tree_digest

    get_tree_ignored_exceptions = (NotFoundError, RetriableError)

    @DurationMetric(CAS_GET_TREE_TIME_METRIC_NAME, instanced=True)
    @generator_method_exception_counter(
        CAS_GET_TREE_EXCEPTION_COUNT_METRIC_NAME,
        ignored_exceptions=get_tree_ignored_exceptions,
    )
    def get_tree(self, request: GetTreeRequest) -> Iterator[GetTreeResponse]:
        storage = self._storage

        if not request.page_size:
            request.page_size = MAX_REQUEST_COUNT

        if tree := self.lookup_tree_cache(request.root_digest):
            # Cache hit, yield responses based on page size
            directories = [tree.root]
            directories.extend(tree.children)
            yield from (
                GetTreeResponse(directories=directories[start : start + request.page_size])
                for start in range(0, len(directories), request.page_size)
            )
            return

        with Counter(metric_name=CAS_DOWNLOADED_BYTES_METRIC_NAME, instance_name=self._instance_name) as bytes_counter:
            # From the spec, a NotFound response only occurs if the root directory is missing.
            root_directory = storage.get_message(request.root_digest, Directory)
            if not root_directory:
                raise NotFoundError(
                    f"Root digest not found: {request.root_digest.hash}/{request.root_digest.size_bytes}"
                )

            bytes_counter.increment(request.root_digest.size_bytes)

            results = [root_directory]
            offset = 0
            queue = [subdir.digest for subdir in root_directory.directories]
            while queue:
                bytes_counter.increment(sum(d.size_bytes for d in queue))
                blobs = storage.bulk_read_blobs(queue)

                directories = [Directory.FromString(b) for b in blobs.values()]
                queue = [subdir.digest for d in directories for subdir in d.directories]

                results.extend(directories)
                while len(results) - offset >= request.page_size:
                    yield GetTreeResponse(directories=results[offset : offset + request.page_size])
                    offset += request.page_size

            if len(results) - offset > 0:
                yield GetTreeResponse(directories=results[offset:])
            if results:
                self.put_tree_cache(request.root_digest, results[0], results[1:])


class ByteStreamInstance(Instance):
    SERVICE_NAME = bs_pb2.DESCRIPTOR.services_by_name["ByteStream"].full_name

    BLOCK_SIZE = 1 * 1024 * 1024  # 1 MB block size

    def __init__(
        self,
        storage: StorageABC,
        read_only: bool = False,
        disable_overwrite_early_return: bool = False,
    ) -> None:
        self._storage = storage
        self._query_activity_timeout = 30

        self.__read_only = read_only

        # If set, prevents `ByteStream.Write()` from returning without
        # reading all the client's `WriteRequests` for a digest that is
        # already in storage (i.e. not follow the REAPI-specified
        # behavior).
        self.__disable_overwrite_early_return = disable_overwrite_early_return
        # (Should only be used to work around issues with implementations
        # that treat the server half-closing its end of the gRPC stream
        # as a HTTP/2 stream error.)

    # --- Public API ---

    def start(self) -> None:
        self._storage.start()

    @ExceptionCounter(CAS_EXCEPTION_COUNT_METRIC_NAME)
    def set_instance_name(self, instance_name: str) -> None:
        super().set_instance_name(instance_name)
        self._storage.set_instance_name(instance_name)

    bytestream_read_ignored_exceptions = (NotFoundError, RetriableError)

    @generator_method_duration_metric(CAS_BYTESTREAM_READ_TIME_METRIC_NAME)
    @generator_method_exception_counter(
        CAS_BYTESTREAM_READ_EXCEPTION_COUNT_METRIC_NAME,
        ignored_exceptions=bytestream_read_ignored_exceptions,
    )
    def read_cas_blob(
        self, digest_hash: str, digest_size: str, read_offset: int, read_limit: int
    ) -> Iterator[bs_pb2.ReadResponse]:
        if len(digest_hash) != HASH_LENGTH or not digest_size.isdigit():
            raise InvalidArgumentError(f"Invalid digest [{digest_hash}/{digest_size}]")

        digest = Digest(hash=digest_hash, size_bytes=int(digest_size))

        # Check the given read offset and limit.
        if read_offset < 0 or read_offset > digest.size_bytes:
            raise OutOfRangeError("Read offset out of range")

        elif read_limit == 0:
            bytes_remaining = digest.size_bytes - read_offset

        elif read_limit > 0:
            bytes_remaining = read_limit

        else:
            raise InvalidArgumentError("Negative read_limit is invalid")

        # Read the blob from storage and send its contents to the client.
        result = self._storage.get_blob(digest)
        if result is None:
            raise NotFoundError("Blob not found")

        try:
            if read_offset > 0:
                result.seek(read_offset)

            with Distribution(
                metric_name=CAS_BYTESTREAM_READ_SIZE_BYTES, instance_name=self._instance_name
            ) as metric_blob_size:
                metric_blob_size.count = float(digest.size_bytes)

            with Counter(
                metric_name=CAS_DOWNLOADED_BYTES_METRIC_NAME, instance_name=self._instance_name
            ) as bytes_counter:
                while bytes_remaining > 0:
                    block_data = result.read(min(self.BLOCK_SIZE, bytes_remaining))
                    yield bs_pb2.ReadResponse(data=block_data)
                    bytes_counter.increment(len(block_data))
                    bytes_remaining -= self.BLOCK_SIZE
        finally:
            result.close()

    bytestream_write_ignored_exceptions = (NotFoundError, RetriableError)

    @DurationMetric(CAS_BYTESTREAM_WRITE_TIME_METRIC_NAME, instanced=True)
    @ExceptionCounter(
        CAS_BYTESTREAM_WRITE_EXCEPTION_COUNT_METRIC_NAME,
        ignored_exceptions=bytestream_write_ignored_exceptions,
    )
    def write_cas_blob(
        self, digest_hash: str, digest_size: str, requests: Iterator[bs_pb2.WriteRequest]
    ) -> bs_pb2.WriteResponse:
        if self.__read_only:
            raise PermissionDeniedError(f"ByteStream instance {self._instance_name} is read-only")

        if len(digest_hash) != HASH_LENGTH or not digest_size.isdigit():
            raise InvalidArgumentError(f"Invalid digest [{digest_hash}/{digest_size}]")

        digest = Digest(hash=digest_hash, size_bytes=int(digest_size))

        with Distribution(
            metric_name=CAS_BYTESTREAM_WRITE_SIZE_BYTES, instance_name=self._instance_name
        ) as metric_blob_size:
            metric_blob_size.count = float(digest.size_bytes)

        if self._storage.has_blob(digest):
            # According to the REAPI specification:
            # "When attempting an upload, if another client has already
            # completed the upload (which may occur in the middle of a single
            # upload if another client uploads the same blob concurrently),
            # the request will terminate immediately [...]".
            #
            # However, half-closing the stream can be problematic with some
            # intermediaries like HAProxy.
            # (https://github.com/haproxy/haproxy/issues/1219)
            #
            # If half-closing the stream is not allowed, we read and drop
            # all the client's messages before returning, still saving
            # the cost of a write to storage.
            if self.__disable_overwrite_early_return:
                try:
                    for request in requests:
                        if request.finish_write:
                            break
                        continue
                except RpcError:
                    msg = "ByteStream client disconnected whilst streaming requests, upload cancelled."
                    LOGGER.debug(msg)
                    raise RetriableError(msg, retry_period=timedelta(seconds=STREAM_ERROR_RETRY_PERIOD))

            return bs_pb2.WriteResponse(committed_size=digest.size_bytes)

        # Start the write session and write the first request's data.
        bytes_counter = Counter(metric_name=CAS_UPLOADED_BYTES_METRIC_NAME, instance_name=self._instance_name)
        write_session = create_write_session(digest)
        with bytes_counter, write_session:
            computed_hash = HASH()

            # Handle subsequent write requests.
            try:
                for request in requests:
                    write_session.write(request.data)

                    computed_hash.update(request.data)
                    bytes_counter.increment(len(request.data))

                    if request.finish_write:
                        break
            except RpcError:
                write_session.close()
                msg = "ByteStream client disconnected whilst streaming requests, upload cancelled."
                LOGGER.debug(msg)
                raise RetriableError(msg, retry_period=timedelta(seconds=STREAM_ERROR_RETRY_PERIOD))

            # Check that the data matches the provided digest.
            if bytes_counter.count != digest.size_bytes:
                raise NotImplementedError(
                    "Cannot close stream before finishing write, "
                    f"got {bytes_counter.count} bytes but expected {digest.size_bytes}"
                )

            if computed_hash.hexdigest() != digest.hash:
                raise InvalidArgumentError("Data does not match hash")

            self._storage.commit_write(digest, write_session)
            return bs_pb2.WriteResponse(committed_size=int(bytes_counter.count))
