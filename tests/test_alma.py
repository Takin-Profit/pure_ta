"""alma tests."""
import math

from pure_ta import Quote, Ta

# expected results.
# https://docs.google.com/spreadsheets/d/1T14VAhzM14Yqf4sjE7UEcl1yJUyS27TRLPf0Bg-n3BY/edit?usp=sharing.


def test_alma_returns_correct_number_of_results(get_default: list[Quote]):
    """Alma results should have the correct length."""
    alma = Ta.alma()
    results = [alma(q.close) for q in get_default]
    assert len(results) == 502


def test_alma_returns_correct_number_of_results_without_nan(get_default: list[Quote]):
    """Alma results should return the correct number of results without nan."""
    alma = Ta.alma(length=10)
    results = [alma(q.close) for q in get_default]
    results_without_nan = [r for r in results if not math.isnan(r)]
    assert len(results_without_nan) == 493


def test_alma_returns_correct_calculation_results(get_default: list[Quote]):
    """Alma results should return the correct calculation results."""
    alma = Ta.alma(length=10)
    results = [alma(q.close) for q in get_default]
    assert math.isnan(results[0])
    assert math.isnan(results[8])
    assert round(results[9], 4) == 214.1839
    assert round(results[24], 4) == 216.0619
    assert round(results[249], 4) == 257.5787
    assert round(results[501], 4) == 242.1871
