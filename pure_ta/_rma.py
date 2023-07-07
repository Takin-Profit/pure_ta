import math
from collections.abc import Callable

from pure_ta._sma import get_sma


def get_rma(length: int = 14) -> Callable[[float], float]:
    """Return a function that calculates the RMA (Relative Moving Average)."""
    alpha = 1.0 / length
    sum_ = math.nan
    sma_func = get_sma(length)
    is_initial_sma_calculated = False

    def rma_func(data: float) -> float:
        nonlocal sum_, is_initial_sma_calculated
        sma = sma_func(data)
        if not is_initial_sma_calculated:
            # Try to calculate initial SMA
            if not math.isnan(sma):
                # If SMA calculation returned a number,
                # initial SMA is calculated
                sum_ = sma
                is_initial_sma_calculated = True
        else:
            # Apply RMA calculation
            sum_ = alpha * data + (1 - alpha) * sum_

        return sum_

    return rma_func
