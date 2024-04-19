# Copyright (C) 2023 Bloomberg LP
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
A storage provider that uses redis to maintain existence and expiry metadata
for a storage.
"""

import logging
import time
from datetime import datetime, timedelta
from typing import IO, Dict, Iterator, List, Optional, Set, Tuple

import redis

from buildgrid._protos.build.bazel.remote.execution.v2.remote_execution_pb2 import Digest
from buildgrid._protos.google.rpc import code_pb2
from buildgrid._protos.google.rpc.status_pb2 import Status
from buildgrid.server.cas.storage.index.index_abc import IndexABC
from buildgrid.server.cas.storage.storage_abc import StorageABC
from buildgrid.server.metrics_names import (
    CLEANUP_BLOBS_DELETION_RATE_METRIC_NAME,
    CLEANUP_STORAGE_DELETION_FAILURES_METRIC_NAME,
)
from buildgrid.server.metrics_utils import publish_counter_metric, publish_gauge_metric
from buildgrid.server.redis.provider import RedisProvider
from buildgrid.utils import validate_digest_data

LOGGER = logging.getLogger(__name__)


class RedisIndex(IndexABC):
    def __init__(self, redis: RedisProvider, storage: StorageABC) -> None:
        self._redis = redis
        self._storage = storage
        # TODO: implement redis notification based cleanup, make this configurable, and lower the default
        self._ttl = timedelta(days=365)

    def start(self) -> None:
        self._storage.start()

    def stop(self) -> None:
        self._storage.stop()

    def _construct_key(self, digest: Digest) -> str:
        """Helper to get the redis key name for a particular digest"""
        # The tag prefix serves to distinguish between our keys and
        # actual blobs if the same redis is used for both index and storage
        return "A:" + digest.hash + "_" + str(digest.size_bytes)

    def _deconstruct_key(self, keystr: str) -> Optional[Digest]:
        """Helper to attempt to recover a Digest from a redis key"""

        try:
            tag, rest = keystr.split(":", 1)
            if tag != "A":
                return None
            hash, size_bytes = rest.rsplit("_", 1)
            return Digest(hash=hash, size_bytes=int(size_bytes))
        except ValueError:
            return None

    def has_blob(self, digest: Digest) -> bool:
        # Redis is authoritative for existence, no need to check storage.
        return bool(self._redis.execute_ro(lambda r: r.exists(self._construct_key(digest))))

    def get_blob(self, digest: Digest) -> Optional[IO[bytes]]:
        # If storage has the blob that's enough, no need to check the index.
        # We aren't expecting to typically "discover" blobs this way and a
        # get request does not extend the ttl so we don't update the index.
        return self._storage.get_blob(digest)

    def delete_blob(self, digest: Digest) -> None:
        # If the initial delete doesn't delete anything due to the key not existing
        # don't do anything else
        if self._redis.execute_rw(lambda r: r.delete(self._construct_key(digest))):
            self._storage.delete_blob(digest)

            # If we race with a blob being re-added we might have just deleted the
            # storage out from under it. We don't want the index to end up with
            # keys for things that are not present in storage since we consider
            # the index authoritative for existance. So we delete the keys again
            # after deleting from storage, this way if they do get out of sync it
            # will be in the direction of leaking objects in storage that the
            # index doesn't know about.
            def delete_from_index(r: "redis.Redis[bytes]") -> None:
                pipe = r.pipeline()
                pipe.delete(self._construct_key(digest))
                pipe.decrby("total_size", digest.size_bytes)
                pipe.execute()

            self._redis.execute_rw(delete_from_index)

    def commit_write(self, digest: Digest, write_session: IO[bytes]) -> None:
        self._storage.commit_write(digest, write_session)

        def set_ttl(r: "redis.Redis[bytes]") -> None:
            key = self._construct_key(digest)
            # Only increment total_size if this key is new
            # Use a dummy value of 1. We only care about existence and expiry
            if r.set(key, 1, ex=self._ttl, nx=True) is not None:
                r.incrby("total_size", digest.size_bytes)

        self._redis.execute_rw(set_ttl)

    def bulk_delete(self, digests: List[Digest]) -> List[str]:
        # Delete from the index and then delete from the backing storage.
        def delete_from_index(r: "redis.Redis[bytes]") -> List[Digest]:
            pipe = r.pipeline()
            bytes_deleted = 0
            for digest in digests:
                pipe.delete(self._construct_key(digest))
            results = pipe.execute()
            # Go through the delete calls and only decrement total_size for the keys
            # which were actually removed
            successful_deletes = []
            for result, digest in zip(results, digests):
                if result:
                    bytes_deleted += digest.size_bytes
                    successful_deletes.append(digest)
            r.decrby("total_size", bytes_deleted)
            return successful_deletes

        successful_deletes = self._redis.execute_rw(delete_from_index)
        failed_deletes = self._storage.bulk_delete(successful_deletes)
        return failed_deletes

    def missing_blobs(self, digests: List[Digest]) -> List[Digest]:
        # We hit the RW node for every FMB call to extend all the TTLs.
        # This could try to take advantage of RO replicas by only hitting the
        # RW node for blobs that do not have enough TTL left, if any.
        # We currently rely on the always-updated TTL to determine if a blob
        # should be protected in mark_n_bytes_as_deleted. If we allow some
        # slop before updating the RW node here we need to account for it
        # there too.
        def extend_ttls(r: "redis.Redis[bytes]") -> List[int]:
            pipe = r.pipeline(transaction=False)
            for digest in digests:
                pipe.expire(name=self._construct_key(digest), time=self._ttl)
            return pipe.execute()

        extend_results = self._redis.execute_rw(extend_ttls)

        return [digest for digest, result in zip(digests, extend_results) if result != 1]

    def bulk_update_blobs(self, blobs: List[Tuple[Digest, bytes]]) -> List[Status]:
        result_map: Dict[str, Status] = {}
        missing_blob_pairs: List[Tuple[Digest, bytes]] = []
        missing_blobs = self.missing_blobs([digest for digest, _ in blobs])
        for digest, blob in blobs:
            if digest not in missing_blobs:
                if validate_digest_data(digest, blob):
                    result_map[digest.hash] = Status(code=code_pb2.OK)
                else:
                    result_map[digest.hash] = Status(code=code_pb2.INVALID_ARGUMENT, message="Data doesn't match hash")
            else:
                missing_blob_pairs.append((digest, blob))
        results = self._storage.bulk_update_blobs(missing_blob_pairs)

        def set_ttls(r: "redis.Redis[bytes]") -> None:
            pipe = r.pipeline()
            bytes_added = 0
            for digest, result in zip(missing_blobs, results):
                result_map[digest.hash] = result
                if result.code == code_pb2.OK:
                    key = self._construct_key(digest)
                    # Use a dummy value of 1. We only care about existence and expiry
                    pipe.set(key, 1, ex=self._ttl, nx=True)
            redis_results = pipe.execute()
            # only update total_size for brand new keys
            for result, digest in zip(redis_results, missing_blobs):
                if result is not None:
                    bytes_added += digest.size_bytes
            r.incrby("total_size", bytes_added)

        self._redis.execute_rw(set_ttls)
        return [result_map[digest.hash] for digest, _ in blobs]

    def bulk_read_blobs(self, digests: List[Digest]) -> Dict[str, bytes]:
        # If storage has the blob that's enough, no need to check the index.
        # We aren't expecting to typically "discover" blobs this way and a
        # get request does not extend the ttl so we don't update the index.
        return self._storage.bulk_read_blobs(digests)

    def least_recent_digests(self) -> Iterator[Digest]:
        """Generator to iterate through the digests in LRU order"""
        # This is not a LRU index, this method is used only from tests.
        raise NotImplementedError()

    def get_total_size(self, include_marked: bool = True) -> int:
        """
        Return the sum of the size of all blobs within the index

        For the redis index, include_marked does not apply.
        """

        # The total_size represents what we have stored in the underlying
        # storage. However, if some redis notifications for expiring keys
        # are missed we won't actually have keys to account for all the size.
        # The expectation is that a "janitor" process will locate orphaned
        # blobs in storage eventually and when it does so it will call our
        # delete_blob which will finally decrby the total_size.
        total_size = self._redis.execute_ro(lambda r: r.get("total_size"))
        if total_size:
            return int(total_size)
        else:
            return 0

    def delete_n_bytes(
        self, n_bytes: int, dry_run: bool = False, protect_blobs_after: Optional[datetime] = None
    ) -> int:
        """
        Iterate through the Redis Index using 'SCAN' and delete any entries older than
        'protect_blobs_after'. The ordering of the deletes is undefined and can't be assumed
        to be LRU.
        """
        now = datetime.utcnow()

        if protect_blobs_after:
            threshold_time = protect_blobs_after
        else:
            threshold_time = now

        # Used for metric publishing
        delete_start_time = time.time()
        metadata = {}
        if self._instance_name:
            metadata["instance-name"] = self._instance_name

        seen: Set[str] = set()
        cursor = 0
        bytes_deleted = 0

        while n_bytes > 0:
            # Maybe count should be configurable or somehow self-tuning
            # based on how many deletable keys we're actually getting
            # back per-request.
            # We could also choose random prefixes for the scan so that
            # multiple cleanup process are less likely to contend
            rawkeys: List[bytes]
            cursor, rawkeys = self._redis.execute_ro(lambda r: r.scan(match="A:*", cursor=cursor, count=1000))
            keys = [key.decode() for key in rawkeys]

            def get_ttls(r: "redis.Redis[bytes]") -> List[bytes]:
                pipe = r.pipeline(transaction=False)
                for key in keys:
                    pipe.ttl(key)
                return pipe.execute()

            raw_ttls = self._redis.execute_ro(get_ttls)
            ttls = [int(x) for x in raw_ttls]

            LOGGER.debug(f"scan returned {len(ttls)} keys")
            digests_to_delete: List[Digest] = []
            for key, ttl in zip(keys, ttls):
                # Since FMB sets the ttl to self._ttl on every call we can
                # use the time remaining to figure out when the last FMB
                # call for that blob was.
                blob_time = now - (self._ttl - timedelta(seconds=ttl))
                if n_bytes <= 0:
                    break

                digest = self._deconstruct_key(key)
                if digest and (blob_time <= threshold_time) and (digest.hash not in seen):
                    n_bytes -= digest.size_bytes
                    digests_to_delete.append(digest)

            if digests_to_delete:
                failed_deletes = []
                if dry_run:
                    LOGGER.debug(f"Would delete {len(digests_to_delete)} digests")
                else:
                    LOGGER.debug(f"Deleting {len(digests_to_delete)} digests")
                    failed_deletes = self.bulk_delete(digests_to_delete)
                    publish_counter_metric(
                        CLEANUP_STORAGE_DELETION_FAILURES_METRIC_NAME, len(failed_deletes), metadata
                    )
                for digest in digests_to_delete:
                    if digest not in failed_deletes:
                        bytes_deleted += digest.size_bytes

            if cursor == 0:  # scan finished
                LOGGER.debug("cursor exhausted")
                break

        batch_duration = time.time() - delete_start_time
        blobs_deleted_per_second = (len(digests_to_delete) - len(failed_deletes)) / batch_duration
        if not dry_run:
            publish_gauge_metric(CLEANUP_BLOBS_DELETION_RATE_METRIC_NAME, blobs_deleted_per_second, metadata)
        return bytes_deleted
