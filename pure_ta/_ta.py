"""Ta class which contains functions for calculating technical indicators."""
from collections.abc import Callable

from pure_ta._alma import get_alma
from pure_ta._atr import get_atr
from pure_ta._atr_sl import AtrSlResult, get_atr_sl
from pure_ta._bb import BollingerResult, get_bb
from pure_ta._bbw import get_bbw
from pure_ta._bbwp import get_bbwp
from pure_ta._dema import get_dema
from pure_ta._ema import get_ema
from pure_ta._enum_types import AtrSlMaType, StDevOf
from pure_ta._er import get_er
from pure_ta._hma import get_hma
from pure_ta._percent_rank import get_percent_rank
from pure_ta._rma import get_rma
from pure_ta._sma import get_sma
from pure_ta._std_dev import get_st_dev
from pure_ta._tr import get_tr
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

    @staticmethod
    def tr(handle_na: bool = True) -> Callable[[Hlc], float]:
        """Return a function that calculates the True Range."""
        return get_tr(handle_na)

    @staticmethod
    def atr_sl(
        length: int = 14, ma_type: AtrSlMaType = AtrSlMaType.RMA, multi: float = 1.5
    ) -> Callable[[Hlc], AtrSlResult]:
        """Return a function that calculates the Average True Range Stop Loss."""
        _validate_arg("ATR_SL (Average True Range, Stop Loss)", length)
        return get_atr_sl(length, ma_type, multi)

    @staticmethod
    def std_dev(
        len: int = 20, bias: StDevOf = StDevOf.POPULATION
    ) -> Callable[[float], float]:
        """Return a function that calculates the standard deviation."""
        _validate_arg("Standard Deviation", len)
        return get_st_dev(len, bias)

    @staticmethod
    def bb(len: int = 20, multi: int = 2) -> Callable[[float], BollingerResult]:
        """Return a function that calculates the Bollinger Bands."""
        _validate_arg("Bollinger Bands", len)
        return get_bb(len, multi)

    @staticmethod
    def bbw(len: int = 5, multi: int = 4) -> Callable[[float], float]:
        """Return a function that calculates the Bollinger Bands Width."""
        _validate_arg("Bollinger Bands Width", len)
        return get_bbw(len, multi)

    @staticmethod
    def percent_rank(len: int = 20) -> Callable[[float], float]:
        """Return a function that calculates the Percent Rank."""
        _validate_arg("Percent Rank", len)
        return get_percent_rank(len)

    @staticmethod
    def bbwp(length: int = 13) -> Callable[[float], float]:
        """Return a function that calculates the Bollinger Bands Width Percentile."""
        _validate_arg("Bollinger Bands Width Percentile", length)
        return get_bbwp(length)

    @staticmethod
    def dema(length: int = 20) -> Callable[[float], float]:
        """Return a function that calculates the double exponential moving average."""
        _validate_arg("DEMA (Double Exponential Moving Average)", length)
        return get_dema(length)

    @staticmethod
    def er(length: int = 10) -> Callable[[float], float]:
        """Return a function that calculates the efficiency ratio."""
        _validate_arg("ER (Efficiency Ratio)", length)
        return get_er(length)

    @staticmethod
    def hma(length: int = 16) -> Callable[[float], float]:
        """Return a function that calculates the Hull Moving Average."""
        _validate_arg("HMA (Hull Moving Average)", length)
        return get_hma(length)
