"""bollinger bands tests."""
# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
import math

from pure_ta import Quote, ta


# expected results.
# https://docs.google.com/spreadsheets/d/1ZpzvmYn2nw3VnzE_waOHE69ic7pt3F0UH33Y9RBa_5Y/edit?usp=sharing
def test_bb_returns_correct_number_of_results(get_default: list[Quote]):
    """Bollinger Bands results should have the correct length."""
    bb = ta.bb()
    results = [bb(q.close) for q in get_default]
    assert len(results) == 502


def test_bb_returns_correct_number_of_results_without_nan(get_default: list[Quote]):
    """Bollinger Bands results should have the correct number of results without nan."""
    bb = ta.bb()
    results = [bb(q.close) for q in get_default]

    upper = [r for r in results if not math.isnan(r.upper)]
    lower = [r for r in results if not math.isnan(r.lower)]
    middle = [r for r in results if not math.isnan(r.middle)]

    assert len(upper) == 483
    assert len(lower) == 483
    assert len(middle) == 483


def test_bb_returns_correct_values_for_upper_band_calculated(get_default: list[Quote]):
    """Bollinger Bands should return the correct values for upper band calculated."""
    bb = ta.bb()
    results = [bb(q.close) for q in get_default]

    assert round(results[249].upper, 4) == 259.5642
    assert round(results[249].lower, 4) == 251.5358
    assert round(results[249].middle, 4) == 255.5500

    assert round(results[501].upper, 4) == 273.7004
    assert round(results[501].lower, 4) == 230.0196
    assert round(results[501].middle, 4) == 251.8600

    assert round(results[372].upper, 2) == 271.58
    assert round(results[372].lower, 2) == 262.28
    assert round(results[372].middle, 2) == 266.93
