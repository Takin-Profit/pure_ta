from dataclasses import InitVar, dataclass
from datetime import datetime
from decimal import Decimal
from typing import Self, Union

from pure_ta.enum_types import CandlePart
from pure_ta.err_msg import ErrMsg


@dataclass(frozen=True)
class Hlc:
    """Represents the high, low, and close prices of a financial asset."""

    high: float
    low: float
    close: float


# flake8: noqa


@dataclass(frozen=True)
class PriceData:
    """Represents price data for a financial asset.
    at the specified time."""

    time_stamp: str
    value: float


@dataclass(frozen=True)
class PriceDataWithVol:
    """Represents price and volume data for a financial asset.
    at the specified time."""

    time_stamp: str
    value: float
    volume: float


@dataclass
class Quote:
    """Represents a quote for a financial asset."""

    time: datetime
    o: InitVar[float]
    h: InitVar[float]
    l: InitVar[float]
    c: InitVar[float]
    v: InitVar[float]

    @property
    def open(self) -> float:
        """the open price of the quote."""
        return float(self._o)

    @property
    def high(self) -> float:
        """the high price of the quote."""
        return float(self._h)

    @property
    def low(self) -> float:
        """the low price of the quote."""
        return float(self._l)

    @property
    def close(self) -> float:
        """the close price of the quote."""
        return float(self._c)

    @property
    def vol(self) -> float:
        """the volume of the quote."""

        return float(self._v)

    @property
    def hl2(self) -> float:
        """"""
        return float((self._h + self._l) / 2)

    @property
    def hlc3(self) -> float:
        return float((self._h + self._l + self._c) / 3)

    @property
    def oc2(self) -> float:
        return float((self._o + self._c) / 2)

    @property
    def ohl3(self) -> float:
        return float((self._o + self._h + self._l) / 3)

    @property
    def ohlc4(self) -> float:
        return float((self._o + self._h + self._l + self._c) / 4)

    @classmethod
    def empty(cls) -> Self:
        """an empty quote."""
        return Quote(time=datetime.min, o=0, h=0, l=0, c=0, v=0)

    @property
    def is_empty(self) -> bool:
        """whether or not the quote is empty"""
        return self.time == datetime.min

    def to_price_data(self, candle_part: CandlePart) -> PriceData:
        """converts Quote to PriceData"""
        match candle_part:
            case candle_part.HIGH:
                return PriceData(time_stamp=self.time.isoformat(), value=self.high)
            case candle_part.LOW:
                return PriceData(time_stamp=self.time.isoformat(), value=self.low)
            case candle_part.CLOSE:
                return PriceData(time_stamp=self.time.isoformat(), value=self.close)
            case candle_part.OPEN:
                return PriceData(time_stamp=self.time.isoformat(), value=self.open)
            case candle_part.VOLUME:
                return PriceData(time_stamp=self.time.isoformat(), value=self.vol)
            case candle_part.HL2:
                return PriceData(time_stamp=self.time.isoformat(), value=self.hl2)
            case candle_part.HLC3:
                return PriceData(time_stamp=self.time.isoformat(), value=self.hlc3)
            case candle_part.OC2:
                return PriceData(time_stamp=self.time.isoformat(), value=self.oc2)
            case candle_part.OHL3:
                return PriceData(time_stamp=self.time.isoformat(), value=self.ohl3)
            case candle_part.OHLC4:
                return PriceData(time_stamp=self.time.isoformat(), value=self.ohlc4)

    def __post_init__(
        self, o: float, h: float, l: float, c: float, v: float  # noqa: E741
    ) -> None:  # noqa: E741
        self._o = Decimal(o)
        self._h = Decimal(h)
        self._l = Decimal(l)
        self._c = Decimal(c)
        self._v = Decimal(v)

    @classmethod
    def create(
        cls,
        time: datetime,
        open_: float,
        high: float,
        low: float,
        close: float,
        volume: float,
    ) -> Union[Self, ErrMsg]:
        """attempt to create a quote from the given values. return an
        ErrMsg if validation fails"""
        if low > open_ or low > close or low > high:
            return ErrMsg(
                msg=f"""low: {low}, cannot be greater than open: {open_},
                high: {high}, or close: {close} price"""
            )
        if high < close or high < open_:
            return ErrMsg(
                f"""high: {high} cannot be less than open: {open_},
                low: {low}, or close: {close} price"""
            )
        return cls(time, open_, high, low, close, volume)
