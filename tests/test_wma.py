"""wma tests."""
# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from math import isnan

from pure_ta import Quote, ta

# Expected results.
# https://docs.google.com/spreadsheets/d/1n3-bYh1V0JMStMBIJKE6CSJCLMMEP19tD7vGkRrtq6I/edit?usp=sharing.


def test_wma_returns_correct_number_of_results(get_default: list[Quote]):
    """Sma results should have the correct length."""
    wma = ta.wma()
    results = [wma(q.close) for q in get_default]
    assert len(results) == 502


def test_wma_returns_correct_number_of_results_without_nan(get_default: list[Quote]):
    """Wma results should have the correct number of results without NaN."""
    wma = ta.wma(length=20)
    results = [wma(q.close) for q in get_default]
    non_nan_results = [r for r in results if not isnan(r)]
    assert len(non_nan_results) == 483


def test_wma_returns_correct_calculation_results(get_default: list[Quote]):
    """Wma results should be accurate."""
    wma = ta.wma(length=20)
    results = [wma(q.close) for q in get_default]
    result149 = results[149]
    result501 = results[501]

    # toPrecision(4) in Dart equals round with 3 decimal places in Python
    assert round(result149, 4) == 235.5253
    assert round(result501, 3) == 246.511
