from typing import Callable

from pure_ta.moving_averages import get_sma


class Ta:
    """contains functions that return functions that
    calculate technical indicators"""

    @staticmethod
    def sma(length: int = 20) -> Callable[[float], float]:
        """returns a function that calculates the simple moving average"""
        return get_sma(length)
