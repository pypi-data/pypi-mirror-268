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


import unittest
from datetime import timedelta

import pytest

from buildgrid.server.metrics_utils import (
    Counter,
    DurationMetric,
    ExceptionCounter,
    create_timer_record,
    publish_timer_metric,
)
from buildgrid.server.monitoring import get_monitoring_bus, set_monitoring_bus
from tests.utils.metrics import mock_create_counter_record, mock_create_timer_record


@pytest.fixture()
def mock_monitoring_bus():
    set_monitoring_bus(unittest.mock.Mock())


class NoInstanceNameObject:
    """This class has no self._instance_name"""

    def __init__(self):
        pass

    @DurationMetric("test")
    def test(self):
        pass

    @DurationMetric("test", instanced=True)
    def test_instanced(self):
        pass

    @ExceptionCounter("test", exceptions=(RuntimeError, AttributeError))
    def test_exception(self, should_raise):
        if should_raise:
            raise RuntimeError

    @ExceptionCounter("test", exceptions=(RuntimeError,), ignored_exceptions=(AttributeError, ImportError))
    def test_ignored_exception(self, should_raise):
        if should_raise:
            raise AttributeError

    @ExceptionCounter("test", exceptions=(RuntimeError, AttributeError))
    def test_different_exception(self):
        """Raise different exceptions than expecting for metrics."""
        raise AssertionError

    @DurationMetric("test")
    @ExceptionCounter("test", exceptions=(RuntimeError,))
    def test_multiple_decorators(self, should_raise):
        if should_raise:
            raise RuntimeError
        else:
            pass


def test_no_instance_object(mock_monitoring_bus):
    """The lack of a self._instance_name field throws an AttributeError
    when passing instanced=True in the decorator."""
    obj = NoInstanceNameObject()
    obj.test()
    get_monitoring_bus().send_record_nowait.assert_called_once()
    with pytest.raises(AttributeError):
        obj.test_instanced()


class UnsetInstanceNameObject:
    """This class has a self.instance_name but it's not set."""

    def __init__(self):
        self._instance_name = None

    @DurationMetric("test")
    def test(self):
        pass

    @DurationMetric("test", instanced=True)
    def test_instanced(self):
        pass


def test_unset_instance_name_object(mock_monitoring_bus):
    """If an instance name isn't specified but is_instanced is set,
    the default empty instance name is used"""
    obj = UnsetInstanceNameObject()
    obj.test()
    get_monitoring_bus().send_record_nowait.assert_called_once()
    obj.test_instanced()


class NormalObject:
    """This class has self._instance_name set."""

    def __init__(self):
        self._instance_name = "foo"

    @DurationMetric("test")
    def test_return_5(self):
        return 5

    @DurationMetric("test", instanced=True)
    def test_instanced_return_6(self):
        return 6

    @DurationMetric("test")
    def test_raises_exception(self):
        raise ValueError

    @DurationMetric("test", instanced=True)
    def test_instanced_raises_exception(self):
        raise ValueError


def check_record_sent_and_reset():
    get_monitoring_bus().send_record_nowait.assert_called_once()
    get_monitoring_bus().reset_mock()


def test_normal_object(mock_monitoring_bus):
    """For a properly specified object, the methods that run without
    throwing an error publish metrics. The methods that throw an error
    do not."""
    obj = NormalObject()
    assert obj.test_return_5() == 5
    check_record_sent_and_reset()
    assert obj.test_instanced_return_6() == 6
    check_record_sent_and_reset()
    with pytest.raises(ValueError):
        obj.test_raises_exception()
    with pytest.raises(ValueError):
        obj.test_instanced_raises_exception()
    get_monitoring_bus().send_record_nowait.assert_not_called()


@unittest.mock.patch("buildgrid.server.metrics_utils.time")
def test_decorator_raises_exception(mock_time):
    """Make sure that if the decorator raises an exceptions, the value
    is still returned."""
    mock_time.perf_counter = unittest.mock.Mock()
    mock_time.perf_counter.side_effect = ValueError()
    obj = NormalObject()
    assert obj.test_return_5() == 5
    assert obj.test_instanced_return_6() == 6


def test_simple_counter(mock_monitoring_bus):
    """Validate counter in context manager"""
    with Counter("test") as c:
        c.increment()
        assert c.count == 1.0
        c.increment()
        assert c.count == 2.0
        c.count = 55.1
        assert c.count == 55.1

    get_monitoring_bus().send_record_nowait.assert_called_once()


def test_simple_exception_counter(mock_monitoring_bus):
    """Validate exceptions counter in context manager"""
    with pytest.raises(RuntimeError):
        with ExceptionCounter("test", exceptions=(RuntimeError,)) as ec:
            assert ec.count == 1.0
            assert ec.instance_name is None
            raise RuntimeError

    get_monitoring_bus().send_record_nowait.assert_called_once()


def test_simple_ignored__exception_counter(mock_monitoring_bus):
    """Validate exceptions counter in context manager for ignored exceptions"""
    with pytest.raises(AssertionError):
        with ExceptionCounter(
            "test", exceptions=(RuntimeError,), ignored_exceptions=(AssertionError, ImportError)
        ) as ec:
            assert ec.count == 1.0
            assert ec.instance_name is None
            raise AssertionError

    get_monitoring_bus().send_record_nowait.assert_not_called()

    with pytest.raises(RuntimeError):
        with ExceptionCounter(
            "test", exceptions=(RuntimeError,), ignored_exceptions=(AssertionError, ImportError)
        ) as ec:
            assert ec.count == 1.0
            assert ec.instance_name is None
            raise RuntimeError

    get_monitoring_bus().send_record_nowait.assert_called_once()


def test_no_publish_exception_counter(mock_monitoring_bus):
    """Validate exceptions counter doesn't publish."""
    with ExceptionCounter("test", exceptions=(RuntimeError,)) as ec:
        assert ec.count == 1.0

    get_monitoring_bus().send_record_nowait.assert_not_called()


def test_no_publish_different_exception_counter(mock_monitoring_bus):
    """Validate exceptions counter doesn't publish for different exceptions."""
    obj = NoInstanceNameObject()

    with pytest.raises(AssertionError):
        obj.test_different_exception()

    get_monitoring_bus().send_record_nowait.assert_not_called()


def test_exception_decorator_counter(mock_monitoring_bus):
    """Validate exceptions counter decorator."""
    obj = NoInstanceNameObject()
    with pytest.raises(RuntimeError):
        obj.test_exception(should_raise=True)
    get_monitoring_bus().send_record_nowait.assert_called_once()


def test_no_throw_decorator_counter(mock_monitoring_bus):
    """Validate exceptions counter decorator."""
    obj = NoInstanceNameObject()
    obj.test_exception(should_raise=False)
    get_monitoring_bus().send_record_nowait.assert_not_called()


def test_ignored_exceptions_decorator_counter(mock_monitoring_bus):
    """Validate exceptions counter decorator doesn't publish ignored exception."""
    obj = NoInstanceNameObject()
    with pytest.raises(AttributeError):
        obj.test_ignored_exception(should_raise=True)
    get_monitoring_bus().send_record_nowait.assert_not_called()


def test_counter_no_monitoring_bus():
    """Test no exceptions is raised when counter publishes without monitoring bus."""
    with Counter("test"):
        pass


def test_counter_exception_publish(mock_monitoring_bus):
    """Test not publishing when exceptions thrown in context manager"""

    with pytest.raises(RuntimeError):
        with Counter("test") as c:
            c.increment(76.0)
            assert c.count == 76.0
            raise RuntimeError

    get_monitoring_bus().send_record_nowait.assert_not_called()


@unittest.mock.patch("buildgrid.server.metrics_utils.create_timer_record", new=mock_create_timer_record)
@unittest.mock.patch("buildgrid.server.metrics_utils.create_counter_record", new=mock_create_counter_record)
def test_multiple_decorators(mock_monitoring_bus):
    """Test monitor called with multiple decorators."""
    obj = NoInstanceNameObject()
    obj.test_multiple_decorators(should_raise=False)
    get_monitoring_bus().send_record_nowait.assert_called_once()

    timer_record = mock_create_timer_record("test")

    call_list = [unittest.mock.call(timer_record)]
    get_monitoring_bus().send_record_nowait.assert_has_calls(call_list)

    get_monitoring_bus().reset_mock()
    with pytest.raises(RuntimeError):
        obj.test_multiple_decorators(should_raise=True)
    get_monitoring_bus().send_record_nowait.assert_called_once()

    counter_record = mock_create_counter_record("test")

    call_list = [unittest.mock.call(counter_record)]
    get_monitoring_bus().send_record_nowait.assert_has_calls(call_list)


@unittest.mock.patch("buildgrid.server.metrics_utils.create_timer_record", new=mock_create_timer_record)
def test_publish_timer_metric(mock_monitoring_bus):
    """Test publish_timer_metric method"""
    expected_timer_record = mock_create_timer_record("test")
    # Convert from the mock `Duration` back to a timedelta object
    test_timedelta = timedelta(
        seconds=expected_timer_record.duration.seconds, microseconds=expected_timer_record.duration.nanos * 1000
    )
    publish_timer_metric("test", test_timedelta)
    get_monitoring_bus().send_record_nowait.assert_called_once_with(expected_timer_record)


def test_timer_metric_clock():
    # Since we record timers in fractional seconds ensure that timedelta handles these correctly
    # when converting to duration
    a = 0.123
    b = 2.345

    d = timedelta(seconds=b - a)
    assert d.total_seconds() == 2.222
    duration = create_timer_record("test", d).duration
    assert duration.seconds == 2
    assert duration.nanos == 222000000


class Clock:
    def __init__(self):
        self._value = 0
        pass

    def __call__(self):
        self._value += 1
        return self._value


@DurationMetric("bar")
def nested_duration_metric_test_function(a):
    a += 1
    if a == 1:
        a = nested_duration_metric_test_function(a)
    return a


@unittest.mock.patch("buildgrid.server.metrics_utils.time")
def test_multiple_timer_decorators(mock_time, mock_monitoring_bus):
    mock_time.perf_counter = unittest.mock.Mock()
    c = Clock()
    mock_time.perf_counter.side_effect = c

    assert nested_duration_metric_test_function(0) == 2
    assert get_monitoring_bus().send_record_nowait.call_count == 2

    # The first call to bar will have start at 1, second call to bar will have a start time of 2
    # then the second call finishes with an end time of 3: running time of second call = 1. End
    # of first call to bar 4 leaves a running time of 3.
    _, first_call_args, _ = get_monitoring_bus().send_record_nowait.mock_calls[0]
    assert first_call_args[0].duration.seconds == 1

    _, second_call_args, _ = get_monitoring_bus().send_record_nowait.mock_calls[1]
    assert second_call_args[0].duration.seconds == 3


@unittest.mock.patch("buildgrid.server.metrics_utils.time")
def test_multiple_context_managers(mock_time, mock_monitoring_bus):
    mock_time.perf_counter = unittest.mock.Mock()
    c = Clock()
    mock_time.perf_counter.side_effect = c

    with DurationMetric("foo"):
        with DurationMetric("bar"):
            pass
    assert get_monitoring_bus().send_record_nowait.call_count == 2

    _, first_call_args, _ = get_monitoring_bus().send_record_nowait.mock_calls[0]
    assert first_call_args[0].duration.seconds == 1

    _, second_call_args, _ = get_monitoring_bus().send_record_nowait.mock_calls[1]
    assert second_call_args[0].duration.seconds == 3
