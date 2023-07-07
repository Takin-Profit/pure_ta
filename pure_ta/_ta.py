"""Ta class which contains functions for calculating technical indicators."""
from collections.abc import Callable

from pure_ta._alma import get_alma
from pure_ta._atr import get_atr
from pure_ta._ema import get_ema
from pure_ta._rma import get_rma
from pure_ta._sma import get_sma
from pure_ta._types import Hlc
from pure_ta._wma import get_wma


def _validate_arg(indicator: str, value: int, min_value: int = 1):
    if value < min_value:
        raise ValueError(
            f"""LookBack must be greater than {min_value}
            to calculate the {indicator}"""
        )


class Ta:
    """contains functions that calculate technical indicators."""

    @staticmethod
    def sma(length: int = 20) -> Callable[[float], float]:
        """Return a function that calculates the simple moving average."""
        _validate_arg("SMA (Simple Moving Average)", length)
        return get_sma(length)

    @staticmethod
    def ema(length: int = 20) -> Callable[[float], float]:
        """Return a function that calculates the exponential moving average."""
        _validate_arg("EMA (Exponential Moving Average)", length)
        return get_ema(length)

    @staticmethod
    def alma(
        length: int = 20, sigma: float = 6, offset: float = 0.85
    ) -> Callable[[float], float]:
        """Return a function to calculates the Arnaud Legoux Moving Average."""
        _validate_arg("ALMA (Arnaud Legoux Moving Average)", length)
        if sigma < 1:
            raise ValueError("Sigma must be greater than 1 to use the ALMA")
        if offset < 0 or offset > 1:
            raise ValueError("Offset must be between 0 and 1 to use the ALMA")
        return get_alma(length, sigma=sigma, offset=offset)

    @staticmethod
    def rma(length: int = 14) -> Callable[[float], float]:
        """Return a function that calculates the Relative Moving Average."""
        _validate_arg("RMA (Relative Moving Average)", length)
        return get_rma(length)

    @staticmethod
    def atr(length: int = 14) -> Callable[[Hlc], float]:
        """Return a function that calculates the Average True Range."""
        _validate_arg("ATR (Average True Range)", length)
        return get_atr(length)

    @staticmethod
    def wma(length: int = 15) -> Callable[[float], float]:
        """Return a function that calculates the Weighted Moving Average."""
        _validate_arg("WMA (Weighted Moving Average)", length)
        return get_wma(length)
