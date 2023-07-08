"""ema tests."""  # noqa: E501
import math

from pure_ta import Quote, Ta

# expected results.
# https://docs.google.com/spreadsheets/d/1lg7Fbz-986auSClakX9RS-Y-zrcDZYP8gfYSHQhHP4E/edit?usp=sharing.


def test_ema_returns_correct_number_of_results(get_default: list[Quote]):
    """Ema results should have the correct length."""
    ema = Ta.ema()
    results = [ema(q.close) for q in get_default]
    assert len(results) == 502


def test_ema_returns_correct_number_of_results_without_nan(get_default: list[Quote]):
    """Ema results should return the correct number of results without nan."""
    ema = Ta.ema()
    results = [ema(q.close) for q in get_default]
    results_without_nan = [r for r in results if not math.isnan(r)]
    assert len(results_without_nan) == 483


def test_ema_returns_correct_calculation_results(get_default: list[Quote]):
    """Ema results should return the correct calculation results."""
    ema = Ta.ema()
    results = [ema(q.close) for q in get_default]
    assert math.isnan(results[0])
    assert math.isnan(results[6])
    assert round(results[29], 4) == 216.6228
    assert round(results[30], 4) == 217.1292
    assert round(results[249], 4) == 255.3873
    assert round(results[501], 4) == 249.3519
