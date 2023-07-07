# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
"""Expected results.

* https://docs.google.com/spreadsheets/d/1bG_dLbUHhW07FRFH58p2A9ZSF5P5QskahsfMmhCQKkE/edit?usp=sharing
"""
from math import isnan

from pure_ta import Quote, Ta


def test_true_range_returns_correct_number_of_results(get_default: list[Quote]):
    """True Range results should have the correct length."""
    true_range = Ta.tr()
    results = [true_range(q.hlc) for q in get_default]
    assert len(results) == 502


def test_true_range_returns_no_nan_results_when_handle_na_is_true(
    get_default: list[Quote],
):
    """True Range should not return any nan results when handleNa is true."""
    true_range = Ta.tr()
    results = [true_range(q.hlc) for q in get_default]
    assert all(not isnan(result) for result in results)


def test_first_result_is_nan_when_handle_na_is_false(get_default: list[Quote]):
    """First result should be nan when handleNa is set to false."""
    true_range = Ta.tr(handle_na=False)
    results = [true_range(q.hlc) for q in get_default]
    assert isnan(results[0])
    assert all(not isnan(result) for result in results[1:])


def test_true_range_returns_correct_calculation_results(get_default: list[Quote]):
    """True Range should return the correct calculation results."""
    true_range = Ta.tr()
    results = [true_range(q.hlc) for q in get_default]
    assert round(results[1], 8) == 1.42
    assert round(results[12], 8) == 1.32


def test_true_range_returns_correct_tradingview_data(get_btc_tr: list[Quote]):
    """True Range should return the correct tradingview data."""
    true_range = Ta.tr()
    results = [true_range(q.hlc) for q in get_btc_tr]
    assert round(results[1], 1) == 1170.8
    assert round(results[12], 1) == 2497.3
    assert round(results[145], 1) == 873.3
    assert round(results[402], 1) == 404.9
