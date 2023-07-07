"""expected results.
 * https://docs.google.com/spreadsheets/d/12IZyWjG485EHuOU__1sR0c0dw2VjvI3cW_5ERvhGm_k/edit?usp=sharing"""  # noqa: E501
import math
import os

from pure_ta.ta import Ta
from pure_ta.types import Quote


def test_sma_returns_correct_number_of_results(get_default: list[Quote]):
    """sma results should have the correct length."""
    sma = Ta.sma()
    results = [sma(q.close) for q in get_default]
    assert len(results) == 502


def test_number_of_results_without_nan(get_default: list[Quote]):
    """sma results should return the correct number of results without nan."""
    sma = Ta.sma()
    results = [sma(q.close) for q in get_default]
    result = [r for r in results if not math.isnan(r)]
    # sourcery skip: no-loop-in-tests
    for r in results:
        print(f"{r}{os.linesep}")
    assert len(result) == 483


def test_correct_calculation_results(get_default: list[Quote]):
    """sma results should return the correct calculation results."""
    sma = Ta.sma()
    results = [sma(q.close) for q in get_default]
    assert math.isnan(results[18])
    assert round(results[19], 4) == 214.5250
    assert round(results[24], 4) == 215.0310
    assert round(results[149], 4) == 234.9350
    assert round(results[249], 4) == 255.5500
    assert round(results[501], 4) == 251.8600


def test_open_tests(get_default: list[Quote]):
    """sma results for open prices should be correct."""
    sma = Ta.sma()
    results = [sma(q.open) for q in get_default]
    assert math.isnan(results[18])
    assert round(results[19], 4) == 214.3795
    assert round(results[24], 4) == 214.9535
    assert round(results[149], 4) == 234.8280
    assert round(results[249], 4) == 255.6915
    assert round(results[501], 4) == 253.1725


def test_volume_tests(get_default: list[Quote]):
    """sma results for volumes should be correct."""
    sma = Ta.sma()
    results = [sma(q.vol) for q in get_default]
    assert len(results) == 502
    not_nan = [r for r in results if not math.isnan(r)]
    assert len(not_nan) == 483
    assert round(results[24], 1) == 77293768.2
    assert round(results[290], 1) == 157958070.8
    assert round(results[501], 0) == 163695200