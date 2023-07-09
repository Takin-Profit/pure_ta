"""vwma tests."""
# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from math import isnan

from pure_ta import Quote, ta

# expected results.
# https://docs.google.com/spreadsheets/d/1FhE3RHgoEguLQgZN48trNTmL1i-7aifQitNO7tBxmOs/edit?usp=sharing


def test_vwma_results_have_correct_length(get_default: list[Quote]):
    """Test that the results have the correct length."""
    vwma = ta.vwma()
    results = [vwma(q.close_with_vol) for q in get_default]

    assert len(results) == 502


def test_vwma_correct_number_of_results_without_nan(get_default: list[Quote]):
    """Test that the correct number of results without nan is returned."""
    vwma = ta.vwma(length=10)
    results = [vwma(q.close_with_vol) for q in get_default]
    result = [r for r in results if not isnan(r)]

    assert len(result) == 493


def test_vwma_correct_calculation_results(get_default: list[Quote]):
    """Test that the correct calculation results are returned."""
    vwma = ta.vwma(length=10)
    results = [vwma(q.close_with_vol) for q in get_default]

    result8 = results[8]
    result9 = results[9]
    result24 = results[24]
    result99 = results[99]
    result249 = results[249]
    result501 = results[501]

    assert isnan(result8)
    assert round(result9, 6) == 213.981942
    assert round(result24, 6) == 215.899211
    assert round(result99, 6) == 226.302760
    assert round(result249, 6) == 257.053654
    assert round(result501, 6) == 242.101548
