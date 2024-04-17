"""
Information
---------------------------------------------------------------------
Name        : test_profiler.py
Location    : ~/tests
Author      : Tom Eleff
Published   : 2024-03-19
Revised on  : 2024-03-24

Description
---------------------------------------------------------------------
Tests methods within `pytensils.profiler`.
"""

import time
from pytensils import profiler


@profiler.run_time
def test_run_time_success():
    time.sleep(1)
