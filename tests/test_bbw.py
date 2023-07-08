"""bollinger bands width tests.""."""
# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import math

from pure_ta import Quote, ta

# expected results.
# https://docs.google.com/spreadsheets/d/1wRUEeAw5MeG50_zmDDt4CsFnqrsfxk5OHtjQtVSvavs/edit?usp=sharing
# data exported from tradingview.


def test_bbw_returns_correct_number_of_results(get_eth_bbw: list[Quote]):
    """BBW results should have the correct length."""
    bbw = ta.bbw()
    results = [bbw(q.close) for q in get_eth_bbw]
    assert len(results) == 630


def test_bbw_returns_correct_number_of_results_without_nan(get_eth_bbw: list[Quote]):
    """BBW results should exclude NaNs."""
    bbw = ta.bbw()
    results = [bbw(q.close) for q in get_eth_bbw]
    # Filter out NaN values
    results_without_nan = [r for r in results if not math.isnan(r)]
    assert len(results_without_nan) == 626


def test_bbw_returns_correct_calculation_results(get_eth_bbw: list[Quote]):
    """BBW results should match expected values."""
    bbw = ta.bbw()
    results = [bbw(q.close) for q in get_eth_bbw]

    assert round(results[6], 7) == 0.5883643
    assert round(results[29], 8) == 0.23415884
    assert round(results[247], 6) == 0.192808
    assert round(results[400], 4) == 0.1403
    assert round(results[501], 4) == 0.2590
    assert round(results[628], 7) == 0.0452276
