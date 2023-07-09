"""willy tests."""
# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from math import isnan

from pure_ta import Quote, ta

# expected results.
# https://docs.google.com/spreadsheets/d/1Nio9ujRna5xJ3AhAHJS_BZLWp_xRGedwbxTGiuR_9dc/edit?usp=sharing
# data exported directly from tradingview.


def test_willy_results_have_correct_length(get_gold_willy: list[Quote]):
    """Test that the results have the correct length."""
    willy = ta.willy()
    results = [willy(q.close) for q in get_gold_willy]
    assert len(results) == 1000


def test_willy_results_have_correct_number_without_nan(get_gold_willy: list[Quote]):
    """Test that the results have the correct number of results without nan."""
    willy = ta.willy()
    results = [willy(q.close) for q in get_gold_willy]
    non_nan_results = [result for result in results if not isnan(result)]
    assert len(non_nan_results) == 995


def test_willy_returns_correct_calculation_results(get_gold_willy: list[Quote]):
    """Test that the willy function returns the correct calculation results."""
    willy = ta.willy()
    results = [willy(q.hlc3) for q in get_gold_willy]

    assert isnan(results[0])

    assert round(results[7], 6) == 64.315574

    assert results[218] == 80

    assert results[223] == 20

    assert round(results[562], 5) == 64.15503

    assert round(results[731], 6) == 21.756124

    assert round(results[972], 8) == 69.90551288
