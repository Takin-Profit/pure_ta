"""phoenix ascending tests."""
# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from math import isclose, isnan

from pure_ta import Quote, ta

# expected results.
# https://docs.google.com/spreadsheets/d/1N7CzlqudWgHXad5UDaJzX93V06wZ2vdCgImugibhlQM/edit?usp=sharing
# data exported directly from tradingview.


def test_phx_results_have_correct_length(get_eur_usd_phx: list[Quote]):
    """Test that the results have the correct length."""
    phx = ta.phx()
    results = [phx(q) for q in get_eur_usd_phx]

    assert len(results) == 700


def test_phx_results_have_no_nan(get_eur_usd_phx: list[Quote]):
    """Test that the results have no NaNs."""
    phx = ta.phx()
    results = [phx(q) for q in get_eur_usd_phx]

    results_no_nan = [r for r in results if not isnan(r.fast)]

    assert len(results_no_nan) == 686


def test_phx_fast_results_are_correct(get_eur_usd_phx: list[Quote]):
    """Test that the fast results are correct."""
    phx = ta.phx()
    results = [phx(q) for q in get_eur_usd_phx]

    assert isnan(results[0].fast)
    assert isnan(results[7].fast)
    assert isclose(round(results[77].fast, 8), 50.36170598, abs_tol=0.00004)
    assert isclose(round(results[136].fast, 6), 43.541246)
    assert isclose(round(results[244].fast, 8), 66.99396323, abs_tol=0.023)
    assert isclose(round(results[478].fast, 8), 0.95802506)
    assert isclose(round(results[679].fast, 8), 51.81038019)


def test_phx_slow_results_are_correct(get_eur_usd_phx: list[Quote]):
    """Test that the slow results are correct."""
    phx = ta.phx()
    results = [phx(q) for q in get_eur_usd_phx]

    assert isnan(results[0].slow)
    assert isnan(results[7].slow)
    assert isclose(round(results[77].slow, 8), 79.74020294, abs_tol=0.001)
    assert isclose(round(results[136].slow, 8), 40.59035747)
    assert isclose(round(results[244].slow, 8), 33.94287088)
    assert isclose(round(results[478].slow, 8), 8.78840145)
    assert isclose(round(results[679].slow, 8), 68.04603741)


def test_phx_lsma_results_are_correct(get_eur_usd_phx: list[Quote]):
    """Test that the lsma results are correct."""
    phx = ta.phx()
    results = [phx(q) for q in get_eur_usd_phx]

    assert isnan(results[0].lsma)
    assert isnan(results[7].lsma)
    assert isclose(round(results[77].lsma, 8), 82.62484227, abs_tol=0.001)
    assert isclose(round(results[136].lsma, 8), 37.89349497)
    assert isclose(round(results[244].lsma, 8), 53.06003847)
    assert isclose(round(results[478].lsma, 8), 13.78061112)
    assert isclose(round(results[679].lsma, 8), 72.07285066)
