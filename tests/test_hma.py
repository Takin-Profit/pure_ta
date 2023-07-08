"""hma tests."""
# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
import math

from pure_ta import Quote, Ta

# expected results.
# https://docs.google.com/spreadsheets/d/1JPLgPpKkOfr8hGDOzlO3sVGI4GsP-4wJ6pWMEPkbXxo/edit?usp=sharing


def test_hma_results_have_correct_length(get_default: list[Quote]):
    """Test hma results have correct length."""
    hma = Ta.hma()
    results = [hma(q.close) for q in get_default]

    assert len(results) == 502


def test_hma_results_without_nan_have_correct_length(get_default: list[Quote]):
    """Test that the correct number of hma results do not have NaN."""
    hma = Ta.hma(length=20)
    results = [hma(q.close) for q in get_default]
    results_without_nan = [r for r in results if not math.isnan(r)]

    assert len(results_without_nan) == 480


def test_hma_returns_correct_calculation_results(get_default: list[Quote]):
    """Test that hma returns the correct calculation results."""
    hma = Ta.hma(length=20)
    results = [hma(q.close) for q in get_default]

    result149 = results[149]
    result501 = results[501]

    assert round(result149, 4) == 236.0835
    assert round(result501, 4) == 235.6972
