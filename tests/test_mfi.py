"""mfi tests."""
# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import math

from pure_ta import Quote, ta

# expected results.
# https://docs.google.com/spreadsheets/d/1gmcdd75dq0bZL1xmXYkb1oB_At3aA3q0iL2SMYtZoao/edit?usp=sharing


def test_mfi_results_have_correct_length(get_default: list[Quote]):
    """Test that the results have the correct length."""
    mfi = ta.mfi()
    results = [mfi(q.hlc3_with_vol) for q in get_default]

    assert len(results) == 502


def test_mfi_results_have_correct_number_of_non_nan_results(get_default: list[Quote]):
    """Test that MFI results have the correct number of non NaN results."""
    mfi = ta.mfi()
    results = [mfi(q.hlc3_with_vol) for q in get_default]
    non_nan_results = [result for result in results if not math.isnan(result)]

    assert len(non_nan_results) == 489


def test_should_return_the_correct_calculation_values(get_default: list[Quote]):
    """Test that the function should return the correct calculation values."""
    mfi = ta.mfi()
    results = [mfi(q.hlc3_with_vol) for q in get_default]

    assert round(results[439], 4) == 69.0622
    assert round(results[501], 4) == 39.9494
    assert round(results[473], 4) == 63.2747
    assert round(results[177], 4) == 74.7191
    assert round(results[325], 4) == 56.2805
