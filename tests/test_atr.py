"""atr tests."""
# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from math import isclose, isnan

from pure_ta import Quote, ta


# Expected results.
# https://docs.google.com/spreadsheets/d/1r4SE-GvhgRTV_etW1B1HIsfwiqZ2DANhTZfXXJV4EyE/edit?usp=sharing
# data exported from tradingview.com
def test_atr_returns_correct_number_of_results(get_gold_atr: list[Quote]):
    """Atr results should have the correct length."""
    atr = ta.atr()
    results = [atr(q.hlc) for q in get_gold_atr]
    assert len(results) == 750


def test_atr_returns_correct_number_of_results_without_nan(get_gold_atr: list[Quote]):
    """Atr results should have the correct number of non-NaN results."""
    atr = ta.atr()
    results = [atr(q.hlc) for q in get_gold_atr]
    non_nan_results = [r for r in results if not isnan(r)]
    assert len(non_nan_results) == 737


def test_atr_returns_correct_calculation_results(get_gold_atr: list[Quote]):
    """Atr results should be correctly calculated."""
    atr = ta.atr()
    results = [atr(q.hlc) for q in get_gold_atr]

    assert isnan(results[0])
    assert isnan(results[6])
    # warmup period
    assert isclose(round(results[29], 6), 33.534839, rel_tol=0.54)
    # warmup period
    assert isclose(round(results[120], 6), 28.173596, rel_tol=0.001)
    # warmup period complete
    assert round(results[249], 6) == 26.339388
    assert round(results[501], 6) == 23.935408
    assert round(results[744], 6) == 27.673529
