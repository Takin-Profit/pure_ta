from pure_ta.ta import Ta
from pure_ta.types import Quote


def test_sma(get_default: list[Quote]):
    """sma results should have correct length."""
    sma = Ta.sma()
    results = [sma(q.close) for q in get_default]
    assert len(results) == 502
