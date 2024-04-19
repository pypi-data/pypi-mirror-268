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
CAS services
==================

Implements the Content Addressable Storage API and ByteStream API.
"""

import itertools
import logging
import re
from typing import Any, Dict, Iterator, Tuple, cast

import grpc

import buildgrid.server.context as context_module
from buildgrid._enums import ByteStreamResourceType
from buildgrid._exceptions import InvalidArgumentError
from buildgrid._protos.build.bazel.remote.execution.v2.remote_execution_pb2 import DESCRIPTOR as RE_DESCRIPTOR
from buildgrid._protos.build.bazel.remote.execution.v2.remote_execution_pb2 import (
    BatchReadBlobsRequest,
    BatchReadBlobsResponse,
    BatchUpdateBlobsRequest,
    BatchUpdateBlobsResponse,
    FindMissingBlobsRequest,
    FindMissingBlobsResponse,
    GetTreeRequest,
    GetTreeResponse,
)
from buildgrid._protos.build.bazel.remote.execution.v2.remote_execution_pb2_grpc import (
    ContentAddressableStorageServicer,
    add_ContentAddressableStorageServicer_to_server,
)
from buildgrid._protos.google.bytestream import bytestream_pb2, bytestream_pb2_grpc
from buildgrid._protos.google.bytestream.bytestream_pb2 import (
    QueryWriteStatusRequest,
    QueryWriteStatusResponse,
    ReadRequest,
    ReadResponse,
    WriteRequest,
    WriteResponse,
)
from buildgrid._protos.google.rpc import code_pb2, status_pb2
from buildgrid.server.auth.manager import authorize_stream_unary, authorize_unary_stream, authorize_unary_unary
from buildgrid.server.cas.instance import (
    EMPTY_BLOB,
    EMPTY_BLOB_DIGEST,
    ByteStreamInstance,
    ContentAddressableStorageInstance,
)
from buildgrid.server.metrics_names import (
    CAS_BATCH_READ_BLOBS_TIME_METRIC_NAME,
    CAS_BATCH_UPDATE_BLOBS_TIME_METRIC_NAME,
    CAS_BYTESTREAM_READ_TIME_METRIC_NAME,
    CAS_BYTESTREAM_WRITE_TIME_METRIC_NAME,
    CAS_FIND_MISSING_BLOBS_TIME_METRIC_NAME,
    CAS_GET_TREE_TIME_METRIC_NAME,
)
from buildgrid.server.metrics_utils import DurationMetric, generator_method_duration_metric
from buildgrid.server.request_metadata_utils import printable_request_metadata
from buildgrid.server.servicer import InstancedServicer
from buildgrid.server.utils.decorators import (
    handle_errors_stream_unary,
    handle_errors_unary_stream,
    handle_errors_unary_unary,
    track_request_id,
    track_request_id_generator,
)

LOGGER = logging.getLogger(__name__)


def _printable_batch_update_blobs_request(request: BatchUpdateBlobsRequest) -> Dict[str, Any]:
    # Log the digests but not the data
    return {
        "instance_name": request.instance_name,
        "digests": [r.digest for r in request.requests],
    }


class ContentAddressableStorageService(
    ContentAddressableStorageServicer, InstancedServicer[ContentAddressableStorageInstance]
):
    REGISTER_METHOD = add_ContentAddressableStorageServicer_to_server
    FULL_NAME = RE_DESCRIPTOR.services_by_name["ContentAddressableStorage"].full_name

    @authorize_unary_unary(lambda r: cast(str, r.instance_name))
    @context_module.metadatacontext()
    @track_request_id
    @DurationMetric(CAS_FIND_MISSING_BLOBS_TIME_METRIC_NAME)
    @handle_errors_unary_unary(FindMissingBlobsResponse)
    def FindMissingBlobs(
        self, request: FindMissingBlobsRequest, context: grpc.ServicerContext
    ) -> FindMissingBlobsResponse:
        LOGGER.info(
            f"FindMissingBlobs request from [{context.peer()}] "
            f"([{printable_request_metadata(context.invocation_metadata())}])"
        )

        instance = self.get_instance(request.instance_name)
        # No need to find the empty blob in the cas because the empty blob cannot be missing
        digests_to_find = [digest for digest in request.blob_digests if digest != EMPTY_BLOB_DIGEST]
        response = instance.find_missing_blobs(digests_to_find)
        return response

    @authorize_unary_unary(lambda r: cast(str, r.instance_name))
    @context_module.metadatacontext()
    @track_request_id
    @DurationMetric(CAS_BATCH_UPDATE_BLOBS_TIME_METRIC_NAME)
    @handle_errors_unary_unary(BatchUpdateBlobsResponse, get_printable_request=_printable_batch_update_blobs_request)
    def BatchUpdateBlobs(
        self, request: BatchUpdateBlobsRequest, context: grpc.ServicerContext
    ) -> BatchUpdateBlobsResponse:
        LOGGER.info(
            f"BatchUpdateBlobs request from [{context.peer()}] "
            f"([{printable_request_metadata(context.invocation_metadata())}])"
        )

        instance = self.get_instance(request.instance_name)
        return instance.batch_update_blobs(request.requests)

    @authorize_unary_unary(lambda r: cast(str, r.instance_name))
    @context_module.metadatacontext()
    @track_request_id
    @DurationMetric(CAS_BATCH_READ_BLOBS_TIME_METRIC_NAME)
    @handle_errors_unary_unary(BatchReadBlobsResponse)
    def BatchReadBlobs(self, request: BatchReadBlobsRequest, context: grpc.ServicerContext) -> BatchReadBlobsResponse:
        LOGGER.info(
            f"BatchReadBlobs request from [{context.peer()}] "
            f"([{printable_request_metadata(context.invocation_metadata())}])"
        )
        # No need to actually read the empty blob in the cas as it is always present
        digests_to_read = [digest for digest in request.digests if digest != EMPTY_BLOB_DIGEST]
        empty_digest_count = len(request.digests) - len(digests_to_read)

        instance = self.get_instance(request.instance_name)
        response = instance.batch_read_blobs(digests_to_read)

        # Append the empty blobs to the response
        for _ in range(empty_digest_count):
            response_proto = response.responses.add()
            response_proto.data = EMPTY_BLOB
            response_proto.digest.CopyFrom(EMPTY_BLOB_DIGEST)
            status_code = code_pb2.OK
            response_proto.status.CopyFrom(status_pb2.Status(code=status_code))

        return response

    @authorize_unary_stream(lambda r: cast(str, r.instance_name))
    @track_request_id_generator
    @DurationMetric(CAS_GET_TREE_TIME_METRIC_NAME)
    @handle_errors_unary_stream(GetTreeResponse)
    def GetTree(self, request: GetTreeRequest, context: grpc.ServicerContext) -> Iterator[GetTreeResponse]:
        LOGGER.info(
            f"GetTree request from [{context.peer()}] "
            f"([{printable_request_metadata(context.invocation_metadata())}])"
        )

        instance = self.get_instance(request.instance_name)
        yield from instance.get_tree(request)


class ResourceNameRegex:
    # CAS read name format: "{instance_name}/blobs/{hash}/{size}"
    READ = "^(.*?)/?(blobs/.*/[0-9]*)$"

    # CAS write name format: "{instance_name}/uploads/{uuid}/blobs/{hash}/{size}[optional arbitrary extra content]"
    WRITE = "^(.*?)/?(uploads/.*/blobs/.*/[0-9]*)"


def _parse_resource_name(resource_name: str, regex: str) -> Tuple[str, str, "ByteStreamResourceType"]:
    cas_match = re.match(regex, resource_name)
    if cas_match:
        return cas_match[1], cas_match[2], ByteStreamResourceType.CAS
    else:
        raise InvalidArgumentError(f"Invalid resource name: [{resource_name}]")


def _printable_write_request(request: WriteRequest) -> Dict[str, Any]:
    # Log all the fields except `data`:
    return {
        "resource_name": request.resource_name,
        "write_offset": request.write_offset,
        "finish_write": request.finish_write,
    }


class ByteStreamService(bytestream_pb2_grpc.ByteStreamServicer, InstancedServicer[ByteStreamInstance]):
    REGISTER_METHOD = bytestream_pb2_grpc.add_ByteStreamServicer_to_server
    FULL_NAME = bytestream_pb2.DESCRIPTOR.services_by_name["ByteStream"].full_name

    @authorize_unary_stream(lambda r: _parse_resource_name(r.resource_name, ResourceNameRegex.READ)[0])
    @context_module.metadatacontext()
    @track_request_id_generator
    @generator_method_duration_metric(CAS_BYTESTREAM_READ_TIME_METRIC_NAME)
    @handle_errors_unary_stream(ReadResponse)
    def Read(self, request: ReadRequest, context: grpc.ServicerContext) -> Iterator[ReadResponse]:
        LOGGER.info(
            f"Read request from [{context.peer()}] " f"([{printable_request_metadata(context.invocation_metadata())}])"
        )
        instance_name, resource_name, resource_type = _parse_resource_name(
            request.resource_name, ResourceNameRegex.READ
        )
        instance = self.get_instance(instance_name)
        if resource_type == ByteStreamResourceType.CAS:
            blob_details = resource_name.split("/")
            hash_, size_bytes = blob_details[1], blob_details[2]
            if size_bytes == "0":
                if hash_ != EMPTY_BLOB_DIGEST.hash:
                    raise InvalidArgumentError(f"Invalid digest [{hash_}/{size_bytes}]")
                yield bytestream_pb2.ReadResponse(data=EMPTY_BLOB)
            else:
                yield from instance.read_cas_blob(hash_, size_bytes, request.read_offset, request.read_limit)

    @authorize_stream_unary(lambda r: _parse_resource_name(r.resource_name, ResourceNameRegex.WRITE)[0])
    @context_module.metadatacontext()
    @track_request_id
    @DurationMetric(CAS_BYTESTREAM_WRITE_TIME_METRIC_NAME)
    @handle_errors_stream_unary(WriteResponse, get_printable_request=_printable_write_request)
    def Write(self, request_iterator: Iterator[WriteRequest], context: grpc.ServicerContext) -> WriteResponse:
        LOGGER.info(
            f"Write request from [{context.peer()}] "
            f"([{printable_request_metadata(context.invocation_metadata())}])"
        )

        request = next(request_iterator)
        instance_name, resource_name, resource_type = _parse_resource_name(
            request.resource_name,
            ResourceNameRegex.WRITE,
        )
        instance = self.get_instance(instance_name)
        if resource_type == ByteStreamResourceType.CAS:
            blob_details = resource_name.split("/")
            _, hash_, size_bytes = blob_details[1], blob_details[3], blob_details[4]
            return instance.write_cas_blob(hash_, size_bytes, itertools.chain([request], request_iterator))
        return bytestream_pb2.WriteResponse()

    @authorize_unary_unary(lambda r: _parse_resource_name(r.resource_name, ResourceNameRegex.WRITE)[0])
    @track_request_id
    @handle_errors_unary_unary(QueryWriteStatusResponse)
    def QueryWriteStatus(
        self, request: QueryWriteStatusRequest, context: grpc.ServicerContext
    ) -> QueryWriteStatusResponse:
        LOGGER.info(f"QueryWriteStatus request from [{context.peer()}]")
        context.abort(grpc.StatusCode.UNIMPLEMENTED, "Method not implemented!")
