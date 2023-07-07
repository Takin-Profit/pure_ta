"""The Arnaud Legoux Moving Average (ALMA) is a moving average that
attempts to filter out noise and lag, while improving signal sensitivity.
It achieves this by using a variable window size, and
applying a Gaussian function to the weights of the moving average.
The Gaussian function allows the weights to be further away from the
current price, while still having a significant impact on
the moving average. This allows the ALMA to be more responsive
to price movements, while still filtering out noise."""
import math
from math import exp
from typing import Callable

from pure_ta.circular_buf import CircularBuf


def get_alma(
    length: int = 20, offset: float = 0.85, sigma: float = 6
) -> Callable[[float], float]:
    """returns a function that calculates the Arnaud Legoux Moving Average"""
    window = CircularBuf(size=length)
    window_size = length
    m = offset * (window_size - 1)
    s = window_size / sigma

    def alma_function(data: float):
        nonlocal window, window_size, m, s

        window.put(data)

        if window.filled_size < length:
            return math.nan

        norm = 0.0
        _sum = 0.0
        weights = [0.0 for _ in range(window_size)]
        for i in range(window_size):
            weights[i] = exp(-0.5 * pow((i - m) / s, 2))
            norm += weights[i]

        buf_values = list(window.ordered_values)
        for i in range(window_size):
            _sum += buf_values[i] * weights[i]

        return _sum / norm

    return alma_function
