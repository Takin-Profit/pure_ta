from collections.abc import Callable
from math import isnan


def get_ema(length: int = 20) -> Callable[[float], float]:
    """Returns a function that calculates the exponential moving average."""
    ema = float("nan")
    alpha = 2 / (length + 1)
    counter = 0

    _sum: float = 0
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
