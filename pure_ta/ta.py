"""Ta class which contains functions for calculating technical indicators."""
from typing import Callable

from pure_ta.alma import get_alma
from pure_ta.ema import get_ema
from pure_ta.sma import get_sma


def _validate_arg(indicator: str, value: int, min_value: int = 1):
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
        _validate_arg("SMA (Simple Moving Average)", length)
        return get_sma(length)

    @staticmethod
    def ema(length: int = 20) -> Callable[[float], float]:
        """returns a function that calculates the exponential moving average"""
        _validate_arg("EMA (Exponential Moving Average)", length)
        return get_ema(length)

    @staticmethod
    def alma(
        length: int = 20, sigma: float = 6, offset: float = 0.85
    ) -> Callable[[float], float]:
        """returns a function that calculates the Arnaud Legoux Moving Average"""
        _validate_arg("ALMA (Arnaud Legoux Moving Average)", length)
        if sigma < 1:
            raise ValueError("Sigma must be greater than 1 to calculate the ALMA")
        if offset < 0 or offset > 1:
            raise ValueError("Offset must be between 0 and 1 to calculate the ALMA")
        return get_alma(length, sigma=sigma, offset=offset)
