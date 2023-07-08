"""swma tests."""
# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from math import isnan

from pure_ta import Quote, ta

# expected results.
# https://docs.google.com/spreadsheets/d/1Jkh4spBAsw7i7IWa5tJXcAfrzL4mI9872HnRXhdWGAg/edit?usp=sharing


def test_swma_results_have_correct_length(get_eth_swma: list[Quote]):
    """Test that the results have the correct length."""
    swma = ta.swma()
    results = [swma(q.close) for q in get_eth_swma]

    assert len(results) == 600


def test_swma_correct_number_of_results_without_nan(get_eth_swma: list[Quote]):
    """Test that the results without NaN have the correct length."""
    swma = ta.swma()
    results = [swma(q.close) for q in get_eth_swma]
    non_nan_results = [r for r in results if not isnan(r)]

    assert len(non_nan_results) == 597


def test_swma_correct_calculation_results(get_eth_swma: list[Quote]):
    """Test that the calculation results are correct."""
    swma = ta.swma()
    results = [swma(q.close) for q in get_eth_swma]

    assert round(results[18], 6) == 2952.113333
    assert round(results[19], 6) == 2897.156667
    assert round(results[100], 6) == 3926.851667
    assert round(results[501], 6) == 1615.058333
