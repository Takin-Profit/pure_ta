"""efficiency ratio tests."""
# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from math import isnan

from pure_ta import Quote, ta

# expected results.
# https://docs.google.com/spreadsheets/d/1XZBYAfBKpqNu_nylnlu0od2A0z526ds9YknBln1CCpk/edit?usp=sharing
# data exported from tradingview.


def test_er_results_have_correct_length(get_eth_er: list[Quote]) -> None:
    """Test that the results have the correct length."""
    er = ta.er(length=5)
    results = [er(q.close) for q in get_eth_er]
    assert len(results) == 600


def test_er_returns_correct_number_of_results_without_nan(
    get_eth_er: list[Quote],
) -> None:
    """Test that the correct number of results are returned without nan."""
    er = ta.er(length=5)
    results = [er(q.close) for q in get_eth_er if not isnan(er(q.close))]
    assert len(results) == 595


def test_er_returns_correct_calculation_results(get_eth_er: list[Quote]) -> None:
    """Test that the correct calculation results are returned."""
    er = ta.er(length=5)
    results = [er(q.close) for q in get_eth_er]

    assert round(results[10], 7) == 12.5591680
    assert round(results[92], 6) == 19.972991
    assert round(results[313], 5) == 81.92721
    assert round(results[438], 5) == 53.67261
