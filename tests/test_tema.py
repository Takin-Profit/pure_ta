"""tema tests."""
# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from math import isclose, isnan

from pure_ta import Quote, ta

# expected results.
# https://docs.google.com/spreadsheets/d/1vULEBa80HsutwepMzzLM340dWrKNcnAfwqYK0aduCw4/edit?usp=sharing


def test_tema_results_have_correct_length(get_default: list[Quote]):
    """Test that the tema results have the correct length."""
    tema = ta.tema()
    results = [tema(q.close) for q in get_default]

    assert len(results) == 502


def test_tema_results_should_have_correct_non_nan_length(get_default: list[Quote]):
    """Should return the correct number of results without nan."""
    tema = ta.tema()
    results = [tema(q.close) for q in get_default]
    non_nan_results = [r for r in results if not isnan(r)]

    assert len(non_nan_results) == 445


def test_tema_returns_correct_calculation_results(get_default: list[Quote]):
    """Should return the correct calculation results."""
    tema = ta.tema()
    results = [tema(q.close) for q in get_default]

    assert isnan(results[18])
    assert isnan(results[19])
    assert isclose(results[100], 228.4719, rel_tol=0.01)
    assert isclose(results[501], 238.0345, rel_tol=0.8)
