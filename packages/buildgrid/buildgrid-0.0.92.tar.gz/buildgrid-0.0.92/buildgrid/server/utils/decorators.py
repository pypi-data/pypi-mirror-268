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


import itertools
import logging
import uuid
from functools import wraps
from typing import Any, Callable, Iterator, Type, TypeVar, cast

import grpc
from google.protobuf.message import Message

from buildgrid._exceptions import (
    BotSessionCancelledError,
    BotSessionClosedError,
    BotSessionMismatchError,
    DuplicateBotSessionError,
    FailedPreconditionError,
    InvalidArgumentError,
    NotFoundError,
    PermissionDeniedError,
    RetriableError,
    StorageFullError,
    UnknownBotSessionError,
)
from buildgrid.server.context import ctx_grpc_request_id

_Res = TypeVar("_Res")
_Self = TypeVar("_Self")
_Req = TypeVar("_Req")
_Ctx = TypeVar("_Ctx")


LOGGER = logging.getLogger(__name__)


def track_request_id(f: Callable[[_Self, _Req, _Ctx], _Res]) -> Callable[[_Self, _Req, _Ctx], _Res]:
    """Decorator to set the request ID ContextVar.

    This decorator sets the ``ctx_grpc_request_id`` ContextVar to a UUID
    for the duration of the decorated function. This ContextVar is used
    in logging output to allow log lines for the same request to be
    identified.

    """

    @wraps(f)
    def wrapper(*args: Any, **kwargs: Any) -> _Res:
        ctx_grpc_request_id.set(str(uuid.uuid4()))
        try:
            return f(*args, **kwargs)
        finally:
            ctx_grpc_request_id.set(None)

    return wrapper


def track_request_id_generator(
    f: Callable[[_Self, _Req, _Ctx], Iterator[_Res]]
) -> Callable[[_Self, _Req, _Ctx], Iterator[_Res]]:
    """Decorator to set the request ID ContextVar.

    This is similar to ``track_request_id``, except aimed at wrapping
    generator functions.

    """

    @wraps(f)
    def wrapper(*args: Any, **kwargs: Any) -> Iterator[_Res]:
        ctx_grpc_request_id.set(str(uuid.uuid4()))
        try:
            yield from f(*args, **kwargs)
        finally:
            ctx_grpc_request_id.set(None)

    return wrapper


Func = TypeVar("Func", bound=Callable)  # type: ignore[type-arg]


def handle_errors_unary_unary(
    fallback_return_type: Type[Message], get_printable_request: Callable[[Any], Any] = lambda r: str(r)
) -> Callable[[Func], Func]:
    def decorator(f: Func) -> Func:
        @wraps(f)
        def wrapper(self: _Self, request: _Req, context: grpc.ServicerContext) -> Any:
            try:
                return f(self, request, context)

            except BotSessionCancelledError as e:
                LOGGER.info(e)
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.CANCELLED)

            except BotSessionClosedError as e:
                LOGGER.debug(e)
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.DATA_LOSS)

            except ConnectionError as e:
                LOGGER.exception(e)
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.UNAVAILABLE)

            except DuplicateBotSessionError as e:
                LOGGER.info(e)
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.ABORTED)

            except FailedPreconditionError as e:
                LOGGER.error(e)
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.FAILED_PRECONDITION)

            except (InvalidArgumentError, BotSessionMismatchError, UnknownBotSessionError) as e:
                LOGGER.info(e)
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)

            except NotFoundError as e:
                LOGGER.debug(e)
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.NOT_FOUND)

            except NotImplementedError as e:
                LOGGER.info(e)
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.UNIMPLEMENTED)

            except PermissionDeniedError as e:
                LOGGER.exception(e)
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.PERMISSION_DENIED)

            except RetriableError as e:
                LOGGER.info(f"Retriable error, client should retry in: {e.retry_info.retry_delay}")
                context.abort_with_status(e.error_status)

            except StorageFullError as e:
                LOGGER.exception(e)
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.RESOURCE_EXHAUSTED)

            except Exception as e:
                LOGGER.exception(f"Unexpected error in {f.__name__}; request=[{get_printable_request(request)}]")
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.INTERNAL)

            return fallback_return_type()

        return cast(Func, wrapper)

    return decorator


def handle_errors_stream_unary(
    fallback_return_type: Type[Message], get_printable_request: Callable[[Any], Any] = lambda r: str(r)
) -> Callable[[Func], Func]:
    def decorator(f: Func) -> Func:
        @wraps(f)
        def wrapper(self: _Self, request: Iterator[_Req], context: grpc.ServicerContext) -> Any:
            try:
                initial_request = next(request)
                return f(self, itertools.chain([initial_request], request), context)

            except BotSessionCancelledError as e:
                LOGGER.info(e)
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.CANCELLED)

            except BotSessionClosedError as e:
                LOGGER.debug(e)
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.DATA_LOSS)

            except ConnectionError as e:
                LOGGER.exception(e)
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.UNAVAILABLE)

            except DuplicateBotSessionError as e:
                LOGGER.info(e)
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.ABORTED)

            except FailedPreconditionError as e:
                LOGGER.error(e)
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.FAILED_PRECONDITION)

            except (InvalidArgumentError, BotSessionMismatchError, UnknownBotSessionError) as e:
                LOGGER.info(e)
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)

            except NotFoundError as e:
                LOGGER.debug(e)
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.NOT_FOUND)

            except NotImplementedError as e:
                LOGGER.info(e)
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.UNIMPLEMENTED)

            except PermissionDeniedError as e:
                LOGGER.exception(e)
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.PERMISSION_DENIED)

            except RetriableError as e:
                LOGGER.info(f"Retriable error, client should retry in: {e.retry_info.retry_delay}")
                context.abort_with_status(e.error_status)

            except StorageFullError as e:
                LOGGER.exception(e)
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.RESOURCE_EXHAUSTED)

            except Exception as e:
                LOGGER.exception(
                    f"Unexpected error in {f.__name__}; request=[{get_printable_request(initial_request)}]"
                )
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.INTERNAL)

            return fallback_return_type()

        return cast(Func, wrapper)

    return decorator


def handle_errors_unary_stream(
    fallback_return_type: Type[Message],
) -> Callable[[Func], Func]:
    def decorator(f: Func) -> Func:
        @wraps(f)
        def wrapper(self: _Self, request: _Req, context: grpc.ServicerContext) -> Iterator[Any]:
            try:
                yield from f(self, request, context)

            except ConnectionError as e:
                LOGGER.exception(e)
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.UNAVAILABLE)
                yield fallback_return_type()

            except FailedPreconditionError as e:
                LOGGER.error(e)
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.FAILED_PRECONDITION)
                yield fallback_return_type()

            except InvalidArgumentError as e:
                LOGGER.info(e)
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                yield fallback_return_type()

            except NotFoundError as e:
                LOGGER.debug(e)
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.NOT_FOUND)
                yield fallback_return_type()

            except NotImplementedError as e:
                LOGGER.info(e)
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.UNIMPLEMENTED)
                yield fallback_return_type()

            except PermissionDeniedError as e:
                LOGGER.exception(e)
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.PERMISSION_DENIED)
                yield fallback_return_type()

            except RetriableError as e:
                LOGGER.info(f"Retriable error, client should retry in: {e.retry_info.retry_delay}")
                context.abort_with_status(e.error_status)

            except StorageFullError as e:
                LOGGER.exception(e)
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.RESOURCE_EXHAUSTED)
                yield fallback_return_type()

            except Exception as e:
                LOGGER.exception(f"Unexpected error in {f.__name__}; request=[{request}]")
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.INTERNAL)
                yield fallback_return_type()

        return cast(Func, wrapper)

    return decorator
