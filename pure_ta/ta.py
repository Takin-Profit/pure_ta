"""functions for calculating technical indicators."""
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
from pure_ta._kama import get_kama
from pure_ta._linreg import get_linreg
from pure_ta._mfi import get_mfi
from pure_ta._mom import get_mom
from pure_ta._percent_rank import get_percent_rank
from pure_ta._rma import get_rma
from pure_ta._rsi import get_rsi
from pure_ta._sma import get_sma
from pure_ta._smma import get_smma
from pure_ta._std_dev import get_st_dev
from pure_ta._swma import get_swma
from pure_ta._tci import get_tci
from pure_ta._tema import get_tema
from pure_ta._tr import get_tr
from pure_ta._tsi import TsiResult, get_tsi
from pure_ta._types import Hlc, PriceDataWithVol
from pure_ta._vwma import get_vwma
from pure_ta._willy import get_willy
from pure_ta._wma import get_wma
from pure_ta._wpr import get_wpr


def _validate_arg(indicator: str, value: int, min_value: int = 1):
    if value < min_value:
        raise ValueError(
            f"""LookBack must be greater than {min_value}
            to calculate the {indicator}"""
        )


def sma(length: int = 20) -> Callable[[float], float]:
    """Return a function that calculates the simple moving average."""
    _validate_arg("SMA (Simple Moving Average)", length)
    return get_sma(length)


def ema(length: int = 20) -> Callable[[float], float]:
    """Return a function that calculates the exponential moving average."""
    _validate_arg("EMA (Exponential Moving Average)", length)
    return get_ema(length)


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


def rma(length: int = 14) -> Callable[[float], float]:
    """Return a function that calculates the Relative Moving Average."""
    _validate_arg("RMA (Relative Moving Average)", length)
    return get_rma(length)


def atr(length: int = 14) -> Callable[[Hlc], float]:
    """Return a function that calculates the Average True Range."""
    _validate_arg("ATR (Average True Range)", length)
    return get_atr(length)


def wma(length: int = 15) -> Callable[[float], float]:
    """Return a function that calculates the Weighted Moving Average."""
    _validate_arg("WMA (Weighted Moving Average)", length)
    return get_wma(length)


def tr(handle_na: bool = True) -> Callable[[Hlc], float]:
    """Return a function that calculates the True Range."""
    return get_tr(handle_na)


def atr_sl(
    length: int = 14, ma_type: AtrSlMaType = AtrSlMaType.RMA, multi: float = 1.5
) -> Callable[[Hlc], AtrSlResult]:
    """Return a function that calculates the Average True Range Stop Loss."""
    _validate_arg("ATR_SL (Average True Range, Stop Loss)", length)
    return get_atr_sl(length, ma_type, multi)


def std_dev(
    len: int = 20, bias: StDevOf = StDevOf.POPULATION
) -> Callable[[float], float]:
    """Return a function that calculates the standard deviation."""
    _validate_arg("Standard Deviation", len)
    return get_st_dev(len, bias)


def bb(len: int = 20, multi: int = 2) -> Callable[[float], BollingerResult]:
    """Return a function that calculates the Bollinger Bands."""
    _validate_arg("Bollinger Bands", len)
    return get_bb(len, multi)


def bbw(len: int = 5, multi: int = 4) -> Callable[[float], float]:
    """Return a function that calculates the Bollinger Bands Width."""
    _validate_arg("Bollinger Bands Width", len)
    return get_bbw(len, multi)


def percent_rank(len: int = 20) -> Callable[[float], float]:
    """Return a function that calculates the Percent Rank."""
    _validate_arg("Percent Rank", len)
    return get_percent_rank(len)


def bbwp(length: int = 13) -> Callable[[float], float]:
    """Return a function that calculates the Bollinger Bands Width Percentile."""
    _validate_arg("Bollinger Bands Width Percentile", length)
    return get_bbwp(length)


def dema(length: int = 20) -> Callable[[float], float]:
    """Return a function that calculates the double exponential moving average."""
    _validate_arg("DEMA (Double Exponential Moving Average)", length)
    return get_dema(length)


def er(length: int = 10) -> Callable[[float], float]:
    """Return a function that calculates the efficiency ratio."""
    _validate_arg("ER (Efficiency Ratio)", length)
    return get_er(length)


def hma(length: int = 16) -> Callable[[float], float]:
    """Return a function that calculates the Hull Moving Average."""
    _validate_arg("HMA (Hull Moving Average)", length)
    return get_hma(length)


def kama(length: int = 10) -> Callable[[float], float]:
    """Return a function that calculates the Kaufman's Adaptive Moving Average."""
    _validate_arg("KAMA (Kaufman's Adaptive Moving Average)", length)
    return get_kama(length)


def linreg(length: int = 9) -> Callable[[float], float]:
    """Return a function that calculates the Linear Regression."""
    _validate_arg("Linear Regression", length)
    return get_linreg(length)


def mfi(length: int = 14) -> Callable[[PriceDataWithVol], float]:
    """Return a function that calculates the Money Flow Index."""
    _validate_arg("MFI (Money Flow Index)", length)
    return get_mfi(length)


def mom(length: int = 20) -> Callable[[float], float]:
    """Return a function that calculates the Momentum."""
    _validate_arg("Momentum", length)
    return get_mom(length)


def rsi(length: int = 14) -> Callable[[float], float]:
    """Return a function that calculates the Relative Strength Index."""
    _validate_arg("RSI (Relative Strength Index)", length, 2)
    return get_rsi(length)


def swma() -> Callable[[float], float]:
    """Return a function that calculates the Symmetrically Weighted Moving Average."""
    return get_swma()


def smma(length: int = 20) -> Callable[[float], float]:
    """Return a function that calculates the Smoothed Moving Average."""
    _validate_arg("SMMA (Smoothed Moving Average)", length)
    return get_smma(length)


def tci(length: int = 9) -> Callable[[float], float]:
    """Return a function that calculates the Trend Confidence Index."""
    _validate_arg("TCI (Trend Confidence Index)", length)
    return get_tci(length)


def tema(length: int = 20) -> Callable[[float], float]:
    """Return a function that calculates the Triple Exponential Moving Average."""
    _validate_arg("TEMA (Triple Exponential Moving Average)", length)
    return get_tema(length)


def tsi(
    length: int = 25, smooth_len: int = 13, signal_len: int = 13
) -> Callable[[float], TsiResult]:
    """Return a function that calculates the True Strength Index."""
    _validate_arg("TSI (True Strength Index)", length)
    return get_tsi(length, smooth_len, signal_len)


def vwma(length: int = 20) -> Callable[[PriceDataWithVol], float]:
    """Return a function that calculates the Volume Weighted Moving Average."""
    _validate_arg("VWMA (Volume Weighted Moving Average)", length)
    return get_vwma(length)


def willy(length: int = 6) -> Callable[[float], float]:
    """Return a function that calculates the Willy (A specialized Williams %R)."""
    _validate_arg("WILLY (Williams %R)", length)
    return get_willy(length)


def wpr(length: int = 20) -> Callable[[Hlc], float]:
    """Return a function that calculates the Williams %R."""
    _validate_arg("WPR (Williams %R)", length)
    return get_wpr(length)
