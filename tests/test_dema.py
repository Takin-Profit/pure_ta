"""dema tests."""
# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from math import isnan

from pure_ta import Quote, ta

# expected results.
# https://docs.google.com/spreadsheets/d/122N433yTEEv3uIn2EkucAbO7IId3nddAqQl5JVYamaI/edit?usp=sharing


def test_dema_results_have_correct_length(get_default: list[Quote]):
    """Test that the dema results have the correct length."""
    dema = ta.dema()
    results = [dema(q.close) for q in get_default]

    assert len(results) == 502


def test_dema_returns_correct_number_of_results_without_nan(get_default: list[Quote]):
    """DEMA results should have the correct number of results without nan."""
    dema = ta.dema()
    results = [dema(q.close) for q in get_default]
    # filter out nan values
    results_without_nan = [r for r in results if not isnan(r)]

    assert len(results_without_nan) == 464


def test_dema_returns_correct_calculation_results(get_default: list[Quote]):
    """DEMA results should return the correct calculation results."""
    dema = ta.dema()
    results = [dema(q.close) for q in get_default]

    assert round(results[249], 4) == 258.4452
    assert round(results[501], 4) == 241.1677
