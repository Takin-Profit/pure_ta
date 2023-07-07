"""Ta class which contains functions for calculating technical indicators."""
from typing import Callable

from pure_ta.sma import get_sma


class Ta:
    """contains functions that return functions that
    calculate technical indicators"""

    @staticmethod
    def sma(length: int = 20) -> Callable[[float], float]:
        """returns a function that calculates the simple moving average"""
        return get_sma(length)
