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
#


"""
Simple test to show multithreads throwing exceptions,
will record one count per exception using the ExceptionCounter class.
"""

import itertools
from unittest import mock

import pytest

from buildgrid.server.metrics_utils import ExceptionCounter
from buildgrid.server.monitoring import get_monitoring_bus, set_monitoring_bus
from buildgrid.server.threading import ContextThread
from tests.utils.metrics import mock_create_counter_record


class Wrapped:
    def __init__(self):
        pass

    @ExceptionCounter("test", exceptions=(RuntimeError,))
    def test_throw(self, should_raise=False):
        if should_raise:
            raise RuntimeError


def run_multiple_times(obj, num_threads=10, throw=True):
    thread_list = []
    for _ in range(num_threads):
        thread = ContextThread(target=obj.test_throw, kwargs={"should_raise": throw})
        thread.start()
        thread_list.append(thread)

    for thread in thread_list:
        thread.join()


@pytest.mark.filterwarnings("ignore::_pytest.warning_types.PytestUnhandledThreadExceptionWarning")
@mock.patch("buildgrid.server.metrics_utils.create_counter_record", new=mock_create_counter_record)
def test_multiple_threads_throw():
    set_monitoring_bus(mock.Mock())
    num_threads = 100
    record_list = list(itertools.repeat(mock.call(mock_create_counter_record("test")), num_threads))
    obj = Wrapped()
    run_multiple_times(obj, num_threads)
    get_monitoring_bus().send_record_nowait.assert_has_calls(record_list, any_order=True)
