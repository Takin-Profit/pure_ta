"""tsi tests."""
# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from math import isnan

from pure_ta import Quote, ta

# expected results.
# https://docs.google.com/spreadsheets/d/115y_SO41XPe9I-9d_Dhjq3CSfoTc0PiOSzKlAbWF72Y/edit?usp=sharing


def test_tsi_results_have_correct_length(get_default: list[Quote]):
    """Tsi results should have correct length."""
    tsi = ta.tsi()
    results = [tsi(q.close) for q in get_default]

    assert len(results) == 502


def test_tsi_result_should_have_correct_length_of_nan_results(get_default: list[Quote]):
    """TSI Result should have correct length of NaN results."""
    tsi = ta.tsi(signal_len=7)
    results = [tsi(q.close) for q in get_default]
    non_nan = [r for r in results if not isnan(r.tsi)]

    assert len(non_nan) == 465, "should be 465 non NaN results"


def test_tsi_signal_should_have_correct_length_of_nan_results(get_default: list[Quote]):
    """TSI Signal should have correct length of NaN results."""
    tsi = ta.tsi(signal_len=7)
    results = [tsi(q.close) for q in get_default]
    non_nan = [r for r in results if not isnan(r.signal)]

    assert len(non_nan) == 459, "should be 459 non NaN signal results"


def test_tsi_should_return_correct_results(get_default: list[Quote]):
    """TSI should return correct results."""
    tsi = ta.tsi(signal_len=7)
    results = [tsi(q.close) for q in get_default]

    assert abs(results[37].tsi - 53.1204) < 0.0001, "should be close to 53.1204"
    assert isnan(results[37].signal), "signal should be NaN"
    assert abs(results[43].tsi - 46.0960) < 0.6, "should be close to 46.0960"
    assert abs(results[43].signal - 51.6916) < 0.3, "signal should be close to 51.6916"
    assert abs(results[44].tsi - 42.5121) < 0.5, "should be close to 42.5121"
    assert abs(results[44].signal - 49.3967) < 0.06, "signal should be close to 49.3967"
    assert abs(results[149].tsi - 29.0936) < 0.0003, "should be close to 29.0936"
    assert (
        abs(results[149].signal - 28.0134) < 0.0002
    ), "signal should be close to 28.0134"
    assert round(results[249].tsi, 4) == 41.9232, "should be 41.9232"
    assert round(results[249].signal, 4) == 42.4063, "signal should be 42.4063"
    assert round(results[357].tsi, 4) == 14.8148, "should be 14.8148"
    assert round(results[357].signal, 4) == 13.6709, "should be 13.6709"
    assert round(results[501].tsi, 4) == -28.3513, "should be -28.3513"
    assert round(results[501].signal, 4) == -29.3597, "signal should be -29.3597"
