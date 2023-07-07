"""Ta class which contains functions for calculating technical indicators."""
from typing import Callable

from pure_ta.ema import get_ema
from pure_ta.sma import get_sma


def _validate_arg(indicator: str, value: int, min_value: int):
    if value < min_value:
        raise ValueError(
            f"""LookBack must be greater than {min_value}
            to calculate the {indicator}"""
        )


class Ta:
    """contains functions that return functions that
    calculate technical indicators"""

    @staticmethod
    def sma(length: int = 20) -> Callable[[float], float]:
        """returns a function that calculates the simple moving average"""
        _validate_arg("SMA (Simple Moving Average)", length, 1)
        return get_sma(length)

    @staticmethod
    def ema(length: int = 20) -> Callable[[float], float]:
        """returns a function that calculates the exponential moving average"""
        _validate_arg("EMA (Exponential Moving Average)", length, 1)
        return get_ema(length)
