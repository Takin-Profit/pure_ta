"""mom tests."""
# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from math import isnan

from pure_ta import Quote, ta

# expected results.
# https://docs.google.com/spreadsheets/d/1SpgDEXj961o-8m7zhfEebKArWi2uVshBVnLKtDx52G8/edit?usp=sharing
# data exported from tradingview.


def test_mom_results_have_correct_length(get_btc_mom: list[Quote]):
    """Test that the results have the correct length."""
    mom = ta.mom()
    results = [mom(q.close) for q in get_btc_mom]

    assert len(results) == 800


def test_mom_correct_num_results_without_nan(get_btc_mom: list[Quote]):
    """Test the correct number of results without nan."""
    mom = ta.mom()
    results = [mom(q.close) for q in get_btc_mom if not isnan(mom(q.close))]

    assert len(results) == 780


def test_mom_correct_calculation_results(get_btc_mom: list[Quote]):
    """Test that the correct calculation results are returned."""
    mom = ta.mom()
    results = [mom(q.close) for q in get_btc_mom]

    assert round(results[28], 1) == 1682.1
    assert round(results[100], 1) == 1789.3
    assert round(results[218], 1) == 4884.4
    assert round(results[457], 1) == -5082.8
    assert round(results[756], 1) == -9419.7
