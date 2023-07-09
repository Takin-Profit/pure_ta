"""wpr tests."""
# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from math import isnan

import pytest

from pure_ta import Quote, ta

# expected results.
# https://docs.google.com/spreadsheets/d/10IKwaJybZHl1xNVBM72QHvIhA8ihjy7wUry9riQLHBw/edit?usp=sharing


def test_wpr_results_have_correct_length(get_default: list[Quote]):
    """Test that the results have the correct length."""
    wpr = ta.wpr()
    results = [wpr(q.hlc) for q in get_default]

    assert len(results) == 502


def test_wpr_correct_number_results_without_nan(get_default: list[Quote]):
    """Test that the correct number of results are returned without NaN."""
    wpr = ta.wpr()
    results = [wpr(q.hlc) for q in get_default]
    results_without_nan = [r for r in results if not isnan(r)]

    assert len(results_without_nan) == 489


def test_wpr_returns_correct_values(get_default: list[Quote]):
    """Test that the correct calculation values are returned."""
    wpr = ta.wpr()
    results = [wpr(q.hlc) for q in get_default]

    assert round(results[28], 2) == -4.40
    assert round(results[343], 4) == -19.8211
    assert round(results[501], 4) == -52.0121
    assert round(results[249], 4) == -12.4561
    assert round(results[173], 2) == -1.48


def test_wpr_throws_exception_with_too_small_lookback(get_default: list[Quote]):
    """Test that an exception is thrown if lookback is too small."""
    with pytest.raises(ValueError):
        wpr = ta.wpr(length=0)
        [wpr(q.hlc) for q in get_default]
