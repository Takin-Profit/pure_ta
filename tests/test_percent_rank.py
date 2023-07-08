"""percent_rank tests."""
# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from math import isnan

from pure_ta import Quote, Ta

# expected results.
# https://docs.google.com/spreadsheets/d/1N9QbNyhS8a8sndj2mBMdC_fSfzJ-gTiR0zhnpHUemdQ/edit?usp=sharing
#
# data exported from tradingview.


def test_percent_rank_results_have_correct_length(
    get_crude_percent_rank: list[Quote],
):
    """Test that the result of the percent_rank function has the correct length."""
    percent_rank = Ta.percent_rank()
    result = [percent_rank(q.close) for q in get_crude_percent_rank]
    assert len(result) == 630


def test_percent_rank_returns_correct_number_of_results_without_nan(
    get_crude_percent_rank: list[Quote],
):
    """Percent Rank results without NaN should have correct length."""
    percent_rank = Ta.percent_rank()
    results = [percent_rank(q.close) for q in get_crude_percent_rank]
    valid_results = [r for r in results if not isnan(r)]
    assert len(valid_results) == 610


def test_percent_rank_returns_correct_calculation_results(
    get_crude_percent_rank: list[Quote],
):
    """Percent Rank should return correct calculation results."""
    percent_rank = Ta.percent_rank()
    results = [percent_rank(q.close) for q in get_crude_percent_rank]

    assert isnan(results[6])
    assert results[29] == 80
    assert results[247] == 0
    assert results[400] == 20
    assert results[501] == 50
    assert results[628] == 15
