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

import functools
import logging
import threading
import time
from datetime import timedelta
from typing import Any, Callable, Dict, Optional, Tuple, Type, TypeVar, cast

from buildgrid._enums import MetricRecordType
from buildgrid._exceptions import BgdError
from buildgrid._protos.buildgrid.v2.monitoring_pb2 import MetricRecord
from buildgrid.server.monitoring import get_monitoring_bus


def create_counter_record(name: str, count: float, metadata: Optional[Dict[str, str]] = None) -> MetricRecord:
    counter_record = MetricRecord()

    counter_record.creation_timestamp.GetCurrentTime()
    counter_record.type = MetricRecordType.COUNTER.value
    counter_record.name = name
    counter_record.count = count
    if metadata is not None:
        counter_record.metadata.update(metadata)

    return counter_record


def create_gauge_record(name: str, value: float, metadata: Optional[Dict[str, str]] = None) -> MetricRecord:
    gauge_record = MetricRecord()

    gauge_record.creation_timestamp.GetCurrentTime()
    gauge_record.type = MetricRecordType.GAUGE.value
    gauge_record.name = name
    gauge_record.value = value
    if metadata is not None:
        gauge_record.metadata.update(metadata)

    return gauge_record


def create_timer_record(name: str, duration: timedelta, metadata: Optional[Dict[str, str]] = None) -> MetricRecord:
    timer_record = MetricRecord()

    timer_record.creation_timestamp.GetCurrentTime()
    timer_record.type = MetricRecordType.TIMER.value
    timer_record.name = name
    timer_record.duration.FromTimedelta(duration)
    if metadata is not None:
        timer_record.metadata.update(metadata)

    return timer_record


def create_distribution_record(name: str, value: float, metadata: Optional[Dict[str, str]] = None) -> MetricRecord:
    dist_record = MetricRecord()

    dist_record.creation_timestamp.GetCurrentTime()
    dist_record.type = MetricRecordType.DISTRIBUTION.value
    dist_record.name = name
    dist_record.count = value
    if metadata is not None:
        dist_record.metadata.update(metadata)

    return dist_record


def publish_counter_metric(name: str, count: float, metadata: Optional[Dict[str, str]] = None) -> None:
    record = create_counter_record(name, count, metadata)
    monitoring_bus = get_monitoring_bus()
    monitoring_bus.send_record_nowait(record)


def publish_gauge_metric(name: str, value: float, metadata: Optional[Dict[str, str]] = None) -> None:
    record = create_gauge_record(name, value, metadata)
    monitoring_bus = get_monitoring_bus()
    monitoring_bus.send_record_nowait(record)


def publish_timer_metric(name: str, duration: timedelta, metadata: Optional[Dict[str, str]] = None) -> None:
    record = create_timer_record(name, duration, metadata)
    monitoring_bus = get_monitoring_bus()
    monitoring_bus.send_record_nowait(record)


Func = TypeVar("Func", bound=Callable)  # type: ignore[type-arg]

LOGGER = logging.getLogger(__name__)


class DurationMetric:
    """Provides a decorator and a context manager to measure execution duration."""

    def __init__(self, metric_name: str, instance_name: str = "", instanced: bool = False) -> None:
        self._metric_name = metric_name
        self._instance_name = instance_name
        self._instanced = instanced

        self._start_time: Optional[float] = None

    @property
    def instanced(self) -> bool:
        return self._instanced

    @instanced.setter
    def instanced(self, value: bool) -> None:
        self._instanced = value

    @property
    def instance_name(self) -> str:
        return self._instance_name

    @instance_name.setter
    def instance_name(self, value: str) -> None:
        self._instance_name = value

    def __call__(self, func: Func) -> Func:
        @functools.wraps(func)
        def _timer_wrapper(obj: Any, *args: Any, **kwargs: Any) -> Any:
            if self._instanced:
                if obj._instance_name is not None:
                    self._instance_name = obj._instance_name
            try:
                start_time = time.perf_counter()
            except Exception:
                LOGGER.exception(f"Error raised while starting timing metric [{self._metric_name}]")

            value = func(obj, *args, **kwargs)

            try:
                self._stop_timer_and_submit(start_time)
            except Exception:
                LOGGER.exception(f"Error raised while timing metric [{self._metric_name}]")
            return value

        return cast(Func, _timer_wrapper)

    def __enter__(self) -> "DurationMetric":
        try:
            self._start_time = time.perf_counter()
        except Exception:
            LOGGER.exception(f"Error raised while entering timing metric [{self._metric_name}]")
        return self

    def __exit__(
        self, exception_type: Optional[Type[BaseException]], exception_value: Optional[BaseException], traceback: Any
    ) -> None:
        try:
            assert self._start_time
            self._stop_timer_and_submit(self._start_time)
        except Exception:
            LOGGER.exception(f"Error raised while stopping timing metric [{self._metric_name}] in exit")
        finally:
            self._start_time = None

    def _stop_timer_and_submit(self, start_time: float) -> None:
        monitoring_bus = get_monitoring_bus()
        if self._instanced and self._instance_name is None:
            self._instanced = False

        run_time = timedelta(seconds=time.perf_counter() - start_time)

        metadata = None
        if self._instanced:
            metadata = {"instance-name": self._instance_name}
        record = create_timer_record(self._metric_name, run_time, metadata)
        monitoring_bus.send_record_nowait(record)


def generator_method_duration_metric(name: str) -> Callable[[Func], Func]:
    """Helper function to publish a metric for the duration of a generator method.

    This returns a decorator which publishes a duration metric which measures the
    execution time of the decorated **generator method**.

    This is separate from the ``__call__`` method of ``DurationMetric`` to keep the
    code in that method a bit more readable whilst still having acceptable return
    values, as well as to make the difference between the two approaches clear.

    Usage example
        .. code:: python

            class ExampleInstance:

                @generator_method_duration_metric(EXAMPLE_METHOD_DURATION_NAME)
                def example_method(self, digests, context):
                    for digest in digests:
                        yield self._do_something(digests)

    Args:
        name (str): The metric name to publish the method duration under.

    """

    def decorator(func: Func) -> Func:
        @functools.wraps(func)
        def wrapped_generator_method(obj: Any, *args: Any, **kwargs: Any) -> Any:
            instance_name = getattr(obj, "_instance_name", None)
            with DurationMetric(name) as metric_recorder:
                if instance_name is not None:
                    metric_recorder.instanced = True
                    metric_recorder.instance_name = instance_name
                yield from func(obj, *args, **kwargs)

        return cast(Func, wrapped_generator_method)

    return decorator


class Counter:
    """Provides a generic metric counter. Optionally/Ideally used as a context manager.
    Example Usage:

    with Counter("count-size") as size_counter:
        for i in range(10):
            size_counter.increment(i)
    """

    def __init__(self, metric_name: str, instance_name: Optional[str] = None) -> None:
        self._metric_name = metric_name
        self._instance_name = instance_name
        self._count = 0.0
        self._counter_lock = threading.Lock()

    @property
    def count(self) -> float:
        return self._count

    @count.setter
    def count(self, value: float) -> None:
        with self._counter_lock:
            self._count = value

    @property
    def metric_name(self) -> str:
        return self._metric_name

    @property
    def instance_name(self) -> Optional[str]:
        return self._instance_name

    @instance_name.setter
    def instance_name(self, name: str) -> None:
        with self._counter_lock:
            self._instance_name = name

    def __enter__(self) -> "Counter":
        return self

    def __exit__(
        self, exception_type: Optional[Type[BaseException]], exception_value: Optional[BaseException], traceback: Any
    ) -> None:
        if exception_type is None:
            with self._counter_lock:
                self.publish()

    def increment(self, value: float = 1.0) -> None:
        with self._counter_lock:
            self._count += value

    def publish(self, reset_counter: bool = True) -> None:
        monitoring_bus = get_monitoring_bus()

        metadata = None
        if self._instance_name is not None:
            metadata = {"instance-name": self._instance_name}

        record = create_counter_record(self._metric_name, self._count, metadata)
        monitoring_bus.send_record_nowait(record)
        if reset_counter:
            self._count = 0.0


class ExceptionCounter(Counter):
    """Provides a decorator and context manager in order to count exceptions thrown in a function/method body.
    This class inherits from Counter, publishing a value of 1, using the base classes methods.
    Example Usage:

    with ExceptionCounter("test", exceptions=(RuntimeError,), ignored_exceptions=(NotFoundError,)) as ec:
        ret_val = do_work()
    """

    def __init__(
        self,
        metric_name: str,
        *args: Any,
        exceptions: Tuple[Type[Exception], ...] = (BgdError,),
        ignored_exceptions: Optional[Tuple[Type[Exception], ...]] = None,
        **kwargs: Any,
    ):
        super().__init__(metric_name, *args, **kwargs)

        self._exceptions = exceptions
        self._ignored_exceptions: Tuple[Type[Exception], ...] = ()

        if ignored_exceptions:
            self._ignored_exceptions = ignored_exceptions

        # Increment the counter to 1, publishing will occur on every exception caught.
        self.increment()

    def __exit__(
        self, exception_type: Optional[Type[BaseException]], exception_value: Optional[BaseException], traceback: Any
    ) -> None:
        if exception_value is not None:
            for ignored_exception in self._ignored_exceptions:
                if isinstance(exception_value, ignored_exception):
                    return
            for exception in self._exceptions:
                if isinstance(exception_value, exception):
                    self.publish()
                    return

    def __call__(self, func: Func) -> Func:
        @functools.wraps(func)
        def _exception_wrapper(obj: Any, *args: Any, **kwargs: Any) -> Any:
            try:
                return func(obj, *args, **kwargs)
            except self._ignored_exceptions as e:
                raise e
            except self._exceptions as e:
                with self._counter_lock:
                    if hasattr(obj, "_instance_name"):
                        self._instance_name = obj._instance_name
                    try:
                        self.publish(reset_counter=False)
                    except Exception:
                        LOGGER.exception(
                            f"Expection raised when publishing \
                                                exception metric of type: {type(e)}."
                        )
                raise e

        return cast(Func, _exception_wrapper)


def generator_method_exception_counter(
    name: str,
    exceptions: Tuple[Type[Exception]] = (BgdError,),
    ignored_exceptions: Optional[Tuple[Type[Exception], ...]] = None,
) -> Callable[[Func], Func]:
    """Helper function to publish a counter when an exception is raised by a generator method.

    This returns a decorator which publishes a counter metric which measures the
    number of exceptions raised by the decorated **generator method**.

    This is separate from the ``__call__`` method of ``ExceptionCounter`` to keep the
    code in that method a bit more readable whilst still having acceptable return
    values, as well as to make the difference between the two approaches clear.

    Usage example
        .. code:: python

            class ExampleInstance:

                @generator_method_exception_counter(EXAMPLE_METHOD_EXCEPTION_COUNT_NAME)
                def example_method(self, digests, context):
                    for digest in digests:
                        yield self._do_something(digests)

    Args:
        name (str): The metric name to publish the exception count under.
        exceptions (tuple): Tuple of Exception types to count. Defaults to ``BgdError``.
        ignored_exceptions (tuple): Tuple of Exception types to ignore counting of. Defaults to ``None``.

    """

    def decorator(func: Func) -> Func:
        @functools.wraps(func)
        def wrapped_generator_method(obj: Any, *args: Any, **kwargs: Any) -> Any:
            with ExceptionCounter(name, exceptions=exceptions, ignored_exceptions=ignored_exceptions):
                yield from func(obj, *args, **kwargs)

        return cast(Func, wrapped_generator_method)

    return decorator


class Distribution(Counter):
    """Provides a generic metric using Distribution semantics"""

    def __init__(self, metric_name: str, instance_name: str = "") -> None:
        super().__init__(metric_name, instance_name)

    def publish(self, reset_counter: bool = True) -> None:
        monitoring_bus = get_monitoring_bus()

        metadata = {"instance-name": self._instance_name} if self._instance_name else None
        record = create_distribution_record(self._metric_name, self._count, metadata)
        monitoring_bus.send_record_nowait(record)
        if reset_counter:
            self._count = 0.0
