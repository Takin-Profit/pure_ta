"""rsi tests."""
# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from math import isnan

from pytest import approx, raises  # type: ignore

from pure_ta import Quote, ta

# expected results.
# https://docs.google.com/spreadsheets/d/1gmNLo1zB5jjFvgl_KDbs4QX5xSHw86SiSgJlMWM94XU/edit?usp=sharing


def test_rsi_results_have_correct_length(get_default: list[Quote]):
    """Test that the results have the correct length."""
    rsi = ta.rsi()
    results = [rsi(q.close) for q in get_default]

    assert len(results) == 502


def test_rsi_returns_correct_number_of_results_without_nan(get_default: list[Quote]):
    """Test that the results have the correct number of non-NaN results."""
    rsi = ta.rsi()
    results = [rsi(q.close) for q in get_default]

    # Filter the results to exclude NaN values
    results_without_nan = [res for res in results if not isnan(res)]

    assert len(results_without_nan) == 489


def test_rsi_returns_correct_calculation_values(get_default: list[Quote]):
    """Test that the results have the correct calculation values."""
    rsi = ta.rsi()
    results = [rsi(q.close) for q in get_default]

    assert isnan(results[12])
    # warmup
    assert approx(round(results[14], 4), 0.5) == 62.0541
    # warmup
    assert approx(round(results[104], 4), 0.5) == 70.4399
    assert round(results[223], 4) == 58.6021
    assert round(results[249], 4) == 70.9368
    assert round(results[501], 4) == 42.0773


def test_rsi_throws_exception_with_too_small_lookback(get_default: list[Quote]):
    """Test that rsi function throws an exception when lookback is less than 2."""
    with raises(ValueError):
        rsi = ta.rsi(length=1)
        _ = [rsi(q.close) for q in get_default]

    with raises(ValueError):
        rsi = ta.rsi(length=0)
        _ = [rsi(q.close) for q in get_default]
