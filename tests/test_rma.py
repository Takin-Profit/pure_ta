# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

"""Expected results.

https://docs.google.com/spreadsheets/d/1aOTrwsM9hAi2Ps2FZdgC617PGZFsCzilv1pxfSP-3Cc/edit?usp=sharing
"""
from math import isclose

from pure_ta import Quote, Ta


def test_rma_returns_correct_number_of_results(get_eth_rma: list[Quote]):
    """Rma results should have the correct length."""
    rma = Ta.rma()
    results = [rma(q.close) for q in get_eth_rma]
    assert len(results) == 500


def test_rma_returns_correct_values_for_eth_rma(get_eth_rma: list[Quote]):
    """Rma results should return correct values for eth_rma.csv."""
    rma = Ta.rma()
    results = [rma(q.close) for q in get_eth_rma]

    assert isclose(round(results[200], 4), 1297.1244, rel_tol=1e-5, abs_tol=0.01)
    assert round(results[345], 4) == 1280.8835
    assert abs(results[80] - 2827.6204) <= 0.9
    assert abs(results[154] - 2493.5138) <= 0.02
    assert abs(results[271] - 1642.014873) <= 0.000002
    assert round(results[452], 6) == 1568.421575
    assert round(results[488], 5) == 1879.23033
