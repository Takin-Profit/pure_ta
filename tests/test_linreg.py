"""linreg tests."""
# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

# expected results.
# https://docs.google.com/spreadsheets/d/1cn3vwgBhhNqkHDgg7JNSCBWFSaSPtZjxub1WQTvwA-Y/edit?usp=sharing
# data exported directly from tradingview.
from math import isnan

from pure_ta import Quote, ta


def test_linreg_results_have_correct_length(get_gold_lin_reg: list[Quote]):
    """Test that the results have the correct length."""
    linreg = ta.linreg(length=20)
    results = [linreg(q.close) for q in get_gold_lin_reg]

    assert len(results) == 900


def test_linreg_returns_correct_number_of_results_without_nan(
    get_gold_lin_reg: list[Quote],
):
    """Test that the function returns the correct number of results without NaN."""
    linreg = ta.linreg(length=20)
    results = [linreg(q.close) for q in get_gold_lin_reg]
    results_without_nan = [r for r in results if not isnan(r)]

    assert len(results_without_nan) == 881


def test_linreg_returns_correct_calculation_results(get_gold_lin_reg: list[Quote]):
    """Test that the function returns the correct calculation results."""
    linreg = ta.linreg(length=20)
    results = [linreg(q.close) for q in get_gold_lin_reg]

    assert round(results[249], 6) == 1935.009186
    assert round(results[482], 6) == 1784.800743


def test_linreg_returns_correct_calculation_results_at_high_precision(
    get_gold_lin_reg: list[Quote],
):
    """Function should return the correct calculation results at high precision."""
    linreg = ta.linreg(length=20)
    results = [linreg(q.close) for q in get_gold_lin_reg]

    assert round(results[55], 9) == 1466.118385714
    assert round(results[734], 9) == 1720.119642857
