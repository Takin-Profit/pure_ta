"""kama tests."""
# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from math import isnan

from pure_ta import Quote, ta

# expected results.
# https://docs.google.com/spreadsheets/d/1N1QmE53TOTb4ejipyg3O5rZpoSBErOx84eE7y_qaSnE/edit?usp=sharing


def test_kama_results_have_correct_length(get_eth_kama: list[Quote]):
    """Test that the results have the correct length."""
    kama = ta.kama()
    results = [kama(q.close) for q in get_eth_kama]

    assert len(results) == 600


def test_kama_returns_correct_number_of_results_without_nan(get_eth_kama: list[Quote]):
    """Test that the kama returns the correct number of results without NaN."""
    kama = ta.kama()
    results = [kama(q.close) for q in get_eth_kama]
    results_without_nan = [r for r in results if not isnan(r)]

    assert len(results_without_nan) == 590


def test_kama_returns_correct_calculation_results(get_eth_kama: list[Quote]):
    """Test that the kama returns the correct calculation results."""
    kama = ta.kama()
    results = [kama(q.close) for q in get_eth_kama]

    assert abs(results[218] - 3213.655685) < 0.00001
    assert abs(results[457] - 1255.504734) < 0.00001
    assert abs(results[598] - 1924.649009) < 0.00001
