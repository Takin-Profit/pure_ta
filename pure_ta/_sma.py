"""contains moving average functions."""
import math
from collections.abc import Callable
from statistics import mean

from pure_ta._circular_buf import CircularBuf


def get_sma(length: int = 20) -> Callable[[float], float]:
    """Returns a function that calculates the simple moving average."""
    buf = CircularBuf(size=length)

    def sma_func(data: float) -> float:
        buf.put(data)
        return mean(buf.values) if buf.is_full else math.nan

    return sma_func
