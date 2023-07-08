"""std_dev tests."""
# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from pure_ta import StDevOf, ta
from tests.conftest import get_longish


# expected results.
# https://docs.google.com/spreadsheets/d/1WDhEJQASNBE1FgI-TIVwqw3QK_q3wiwNv4ltFmZFv6I/edit?usp=sharing
def test_std_dev_returns_correct_number_of_results():
    """StdDev results should have the correct length."""
    std_dev = ta.std_dev()
    results = [std_dev(q.close) for q in get_longish()]
    assert len(results) == 5285


def test_std_dev_population_5285():
    """StdDev population results should be correct for length 5285."""
    std_dev = ta.std_dev(len=5285, bias=StDevOf.POPULATION)
    results = [std_dev(q.close) for q in get_longish()]
    assert round(results[5284], 9) == 633.932098287


def test_std_dev_population_10():
    """StdDev population results should be correct for length 10."""
    std_dev = ta.std_dev(len=10, bias=StDevOf.POPULATION)
    results = [std_dev(q.close) for q in get_longish()]
    assert round(results[10], 2) == 13.82
    assert round(results[133], 8) == 28.15109818
    assert round(results[296], 6) == 25.679816


def test_std_dev_population_50():
    """StdDev population results should be correct for length 50."""
    std_dev = ta.std_dev(len=50, bias=StDevOf.POPULATION)
    results = [std_dev(q.close) for q in get_longish()]
    assert round(results[296], 2) == 49.87
    assert round(results[1454], 2) == 21.19
    assert round(results[4644], 6) == 69.287489


def test_std_dev_sample_10():
    """StdDev sample results should be correct for length 10."""
    std_dev = ta.std_dev(len=10, bias=StDevOf.SAMPLE)
    results = [std_dev(q.close) for q in get_longish()]
    assert round(results[15], 2) == 22.62
    assert round(results[569], 4) == 13.8537
    assert round(results[1441], 2) == 4.99
    assert round(results[2204], 6) == 23.154715


def test_std_dev_sample_50():
    """StdDev sample results should be correct for length 50."""
    std_dev = ta.std_dev(len=50, bias=StDevOf.SAMPLE)
    results = [std_dev(q.close) for q in get_longish()]
    assert round(results[2204], 6) == 24.663025
    assert round(results[4006], 5) == 19.87444
