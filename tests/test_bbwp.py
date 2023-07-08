"""bbwp tests."""
# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from math import isclose, isnan

from pure_ta import Quote, Ta


def test_bbwp_results_have_correct_length(
    get_eth_bbwp: list[Quote],
):
    """Test that the result of the bbwp function has the correct length."""
    bbwp = Ta.bbwp()
    result = [bbwp(q.close) for q in get_eth_bbwp]
    assert len(result) == 700


def test_bbwp_returns_correct_number_of_results_without_nan(get_eth_bbwp: list[Quote]):
    """BBWP results should have the correct number of non-nan results."""
    bbwp = Ta.bbwp()
    results = [bbwp(q.close) for q in get_eth_bbwp]
    results_without_nan = [result for result in results if not isnan(result)]
    assert len(results_without_nan) == 448


def test_bbwp_returns_correct_calculation_results(get_eth_bbwp: list[Quote]):
    """BBWP should return the correct calculation results."""
    bbwp = Ta.bbwp()
    results = [bbwp(q.close) for q in get_eth_bbwp]

    assert isnan(results[18])
    assert isnan(results[87])

    # warmup period
    assert isclose(round(results[252], 5), 72.61905, rel_tol=2.4)
    # warmup period complete
    assert round(results[501], 6) == 5.952381

    assert round(results[589], 6) == 25.793651

    assert round(results[699], 6) == 55.158730
