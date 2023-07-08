# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
"""atr_sl tests."""
import math

from pytest import approx  # type: ignore

from pure_ta import AtrSlMaType, Quote, Ta

# AtrSl RMA Expected results.
# https://docs.google.com/spreadsheets/d/1pNv37IY18LyaHxf9XmdFAOAIj_iByq7Q_jwGSAv5ce0/edit?usp=sharing
# data exported from tradingview.com


def test_atr_sl_rma_returns_correct_number_of_results(get_atr_sl_rma: list[Quote]):
    """AtrSl results should have the correct length."""
    atr_sl = Ta.atr_sl()
    results = [atr_sl(q.hlc) for q in get_atr_sl_rma]
    assert len(results) == 800


def test_atr_sl_returns_correct_number_of_results_without_nan(
    get_atr_sl_rma: list[Quote],
):
    """ATRSL should return the correct number of results without NaN."""
    atr_sl = Ta.atr_sl()
    results = [atr_sl(q.hlc) for q in get_atr_sl_rma]
    results_without_nan = [r for r in results if not math.isnan(r.short_sl)]
    assert len(results_without_nan) == 787


def test_atr_sl_returns_correct_short_stop_loss_with_ma_type_rma(
    get_atr_sl_rma: list[Quote],
):
    """ATRSL should return the correct SHORT stop loss with maType RMA."""
    atr_sl = Ta.atr_sl()
    results = [atr_sl(q.hlc) for q in get_atr_sl_rma]

    assert math.isnan(results[0].short_sl)
    assert math.isnan(results[6].short_sl)

    # Warmup period
    assert results[29].short_sl == approx(9.774366, abs=0.02)

    # Warmup period
    assert results[120].short_sl == approx(22.07725, abs=0.00002)

    assert results[249].short_sl == approx(243.55780, abs=0.00001)
    assert results[501].short_sl == approx(585.41605, abs=0.00001)
    assert results[744].short_sl == approx(140.30701, abs=0.00001)


def test_atr_sl_returns_correct_long_stop_loss_with_ma_type_rma(
    get_atr_sl_rma: list[Quote],
):
    """ATRSL should return the correct LONG stop loss with maType RMA."""
    atr_sl = Ta.atr_sl()
    results = [atr_sl(q.hlc) for q in get_atr_sl_rma]

    assert math.isnan(results[0].long_sl)
    assert math.isnan(results[6].long_sl)

    # Warmup period
    assert results[29].long_sl == approx(6.87553, abs=0.02)

    # Warmup period
    assert results[120].long_sl == approx(13.58122, abs=0.00002)

    assert results[249].long_sl == approx(100.44220, abs=0.00001)
    assert results[501].long_sl == approx(352.31395, abs=0.00001)
    assert results[744].long_sl == approx(77.27299, abs=0.00001)


# Atr_Sl Sma expected results.
# https://docs.google.com/spreadsheets/d/1c-CDMm-vKh1M18LDtNvfXYjlYCMV6lI8tdfl-exMi_k/edit?usp=sharing
# data exported from tradingview.com"""


def test_atr_sl_returns_correct_short_stop_loss_with_ma_type_sma(
    get_atr_sl_sma: list[Quote],
):
    """ATRSL should return the correct SHORT stop loss with maType SMA."""
    atr_sl = Ta.atr_sl(ma_type=AtrSlMaType.SMA)
    results = [atr_sl(q.hlc) for q in get_atr_sl_sma]

    assert math.isnan(results[0].short_sl)
    assert math.isnan(results[6].short_sl)

    # Warmup period
    assert round(results[29].short_sl, 5) == approx(9.86079, abs=0.04)

    # Warmup period
    assert round(results[120].short_sl, 5) == approx(22.72193, abs=0.00002)

    assert round(results[249].short_sl, 5) == approx(236.50711, abs=0.00001)
    assert round(results[501].short_sl, 5) == approx(585.58214, abs=0.00001)
    assert round(results[744].short_sl, 5) == approx(144.35536, abs=0.00001)


def test_atr_sl_returns_correct_long_stop_loss_with_ma_type_sma(
    get_atr_sl_sma: list[Quote],
):
    """ATRSL should return the correct LONG stop loss with maType SMA."""
    atr_sl = Ta.atr_sl(ma_type=AtrSlMaType.SMA)
    results = [atr_sl(q.hlc) for q in get_atr_sl_sma]

    assert math.isnan(results[0].long_sl)
    assert math.isnan(results[6].long_sl)

    # Warmup period
    assert round(results[29].long_sl, 5) == approx(5.98522, abs=0.8)

    # Warmup period
    assert round(results[120].long_sl, 5) == approx(12.93654, abs=0.00002)

    assert round(results[249].long_sl, 5) == approx(107.49289, abs=0.00001)
    assert round(results[501].long_sl, 5) == approx(352.14786, abs=0.00001)
    assert round(results[744].long_sl, 5) == approx(73.22464, abs=0.00001)


# AtrSl EMA expected results.
# https://docs.google.com/spreadsheets/d/1Hvtw3hfWLSdl1k2pnme_6bSogxMSDN_SiWQYMU_2mYs/edit?usp=sharing
# data exported from tradingview.com"""


def test_atr_sl_returns_correct_short_stop_loss_with_ma_type_ema(
    get_atr_sl_ema: list[Quote],
):
    """ATRSL should return the correct SHORT stop loss with maType EMA."""
    atr_sl = Ta.atr_sl(ma_type=AtrSlMaType.EMA)
    results = [atr_sl(q.hlc) for q in get_atr_sl_ema]

    assert math.isnan(results[0].short_sl)
    assert math.isnan(results[6].short_sl)

    # Warmup period
    assert round(results[29].short_sl, 5) == approx(9.94067, abs=0.04)

    # Warmup period
    assert round(results[120].short_sl, 5) == approx(22.78104, abs=0.00002)

    assert round(results[249].short_sl, 5) == approx(241.81609, abs=0.00001)
    assert round(results[501].short_sl, 5) == approx(574.70469, abs=0.00001)
    assert round(results[744].short_sl, 4) == approx(143.5418, abs=0.0001)


def test_atr_sl_returns_correct_long_stop_loss_with_ma_type_ema(
    get_atr_sl_ema: list[Quote],
):
    """ATRSL should return the correct LONG stop loss with maType EMA."""
    atr_sl = Ta.atr_sl(ma_type=AtrSlMaType.EMA)
    results = [atr_sl(q.hlc) for q in get_atr_sl_ema]

    assert math.isnan(results[0].long_sl)
    assert math.isnan(results[6].long_sl)

    # Warmup period
    assert round(results[29].long_sl, 5) == approx(6.70923, abs=0.008)

    # Warmup period
    assert round(results[120].long_sl, 5) == approx(12.87743, abs=0.00002)

    assert round(results[249].long_sl, 5) == approx(102.18391, abs=0.00001)
    assert round(results[501].long_sl, 5) == approx(363.02531, abs=0.00001)
    assert round(results[744].long_sl, 5) == approx(74.03820, abs=0.00001)


# AtrSl WMA expected results.
# https://docs.google.com/spreadsheets/d/1ccz9yLxlnvuweh7mwXOMXuKxPkX1OpskDf1hLLH2b1Q/edit?usp=sharing
# data exported from tradingview.com"""


def test_atr_sl_returns_correct_short_stop_loss_with_ma_type_wma(
    get_atr_sl_wma: list[Quote],
):
    """ATRSL should return the correct SHORT stop loss with maType WMA."""
    atr_sl = Ta.atr_sl(ma_type=AtrSlMaType.WMA)
    results = [atr_sl(q.hlc) for q in get_atr_sl_wma]

    assert math.isnan(results[0].short_sl)
    assert math.isnan(results[6].short_sl)

    # Warmup period
    assert round(results[29].short_sl, 6) == approx(10.040728, abs=0.04)

    # Warmup period
    assert round(results[120].short_sl, 5) == approx(23.11802, abs=0.00002)

    assert round(results[249].short_sl, 4) == approx(240.6705, abs=0.0001)
    assert round(results[501].short_sl, 5) == approx(572.31357, abs=0.00001)
    assert round(results[744].short_sl, 5) == approx(145.79343, abs=0.00001)


def test_atr_sl_returns_correct_long_stop_loss_with_ma_type_wma(
    get_atr_sl_wma: list[Quote],
):
    """ATRSL should return the correct LONG stop loss with maType WMA."""
    atr_sl = Ta.atr_sl(ma_type=AtrSlMaType.WMA)
    results = [atr_sl(q.hlc) for q in get_atr_sl_wma]

    assert math.isnan(results[0].long_sl)
    assert math.isnan(results[6].long_sl)

    # Warmup period
    assert round(results[29].long_sl, 5) == approx(6.60917, abs=0.008)

    # Warmup period
    assert round(results[120].long_sl, 5) == approx(12.54045, abs=0.00002)

    assert round(results[249].long_sl, 4) == approx(103.3295, abs=0.0001)
    assert round(results[501].long_sl, 5) == approx(365.41643, abs=0.00001)
    assert round(results[744].long_sl, 6) == approx(71.786571, abs=0.000001)
