"""tci tests."""
from math import isnan

from _pytest.python_api import approx  # type: ignore

from pure_ta import Quote, ta

# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

# expected results.
# https://docs.google.com/spreadsheets/d/1r2jm-TEUPYJN3a2-7Htw0P95hZmryqv-u8XspmdbV40/edit?usp=sharing
# data exported directly from tradingview.


def test_tci_results_have_correct_length(get_gold_tci: list[Quote]):
    """Test that the tci results have the correct length."""
    tci = ta.tci()
    results = [tci(q.hlc3) for q in get_gold_tci]

    assert len(results) == 900


def test_tci_results_should_have_correct_non_nan_length(get_gold_tci: list[Quote]):
    """Should return the correct number of results without nan."""
    tci = ta.tci()
    results = [tci(q.hlc3) for q in get_gold_tci]

    non_nan_results = [r for r in results if not isnan(r)]
    assert len(non_nan_results) == 892


def test_tci_results_have_correct_values(get_gold_tci: list[Quote]):
    """Should return the correct calculation results."""
    tci = ta.tci()
    results = [tci(q.hlc3) for q in get_gold_tci]

    assert isnan(results[0])
    assert isnan(results[6])
    assert approx(round(results[29], 6), 0.5) == 99.510543
    assert round(results[249], 6) == 47.310191
    assert round(results[501], 6) == 19.429759
    assert round(results[614], 6) == 77.738827
    assert round(results[866], 6) == 30.642783
