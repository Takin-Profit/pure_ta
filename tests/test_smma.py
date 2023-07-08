"""smma tests."""
# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from math import isnan

from pure_ta import Quote, ta

# expected results.
# https://docs.google.com/spreadsheets/d/1hvrP1LDE-yjr6z5h7pvT5t4aV38nwQwDlTU2pUX_6Ss/edit?usp=sharing


def test_smma_results_have_correct_length(get_default: list[Quote]):
    """Test that the results have the correct length."""
    smma = ta.smma()
    results = [smma(q.close) for q in get_default]

    assert len(results) == 502


def test_smma_correct_number_of_results_without_nan(get_default: list[Quote]):
    """Test that the correct number of results does not contain NaN values."""
    smma = ta.smma()
    results = [smma(q.close) for q in get_default]

    filtered_results = [r for r in results if not isnan(r)]
    assert len(filtered_results) == 483


def test_smma_correct_calculation_results(get_default: list[Quote]):
    """Test that the calculations are correct."""
    smma = ta.smma()
    results = [smma(q.close) for q in get_default]

    result18, result19 = results[18], results[19]

    assert isnan(result18)
    assert round(result19, 4) == 214.5250
    assert round(results[20], 4) == 214.5512
    assert round(results[21], 4) == 214.5832
    assert round(results[100], 4) == 225.7807
    assert round(results[501], 4) == 255.6746
