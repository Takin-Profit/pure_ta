"""contains moving average functions"""
from math import exp, isnan
from statistics import mean
from typing import Callable

from pure_ta.circular_buf import CircularBuf


def get_sma(length: int = 20) -> Callable[[float], float]:
    """returns a function that calculates the simple moving average"""
    buf = CircularBuf(size=length)

    def sma_func(data: float) -> float:
        buf.put(data)
        return mean(buf.values) if buf.is_full else float("nan")

    return sma_func


def get_ema(length: int = 20) -> Callable[[float], float]:
    """returns a function that calculates the exponential moving average"""
    ema = float("nan")
    alpha = 2 / (length + 1)
    counter = 0

    _sum = 0
    sma_calculated = False

    def ema_function(data: float):
        nonlocal ema, counter, _sum, sma_calculated

        if not sma_calculated and not isnan(data):
            counter += 1
            _sum += data

        if isnan(data):
            return data

        if not sma_calculated and counter == length:
            sma = _sum / length
            if not isnan(sma):
                ema = sma
                sma_calculated = True
        elif sma_calculated and not isnan(data):
            ema = (data - ema) * alpha + ema

        return ema

    return ema_function


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
            return float("nan")

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
