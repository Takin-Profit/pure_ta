"""common types used throughout the library."""
from dataclasses import InitVar, dataclass
from datetime import datetime
from decimal import Decimal
from typing import Self, Union

from pure_ta._enum_types import CandlePart


@dataclass(frozen=True, slots=True)
class ErrMsg:
    """an error message."""

    msg: str


@dataclass(frozen=True, slots=True)
class Hlc:
    """Represents the high, low, and close prices of a financial asset."""

    high: float
    low: float
    close: float


# flake8: noqa


@dataclass(frozen=True, slots=True)
class PriceData:
    """Represents price data for a financial asset at the specified time."""

    time_stamp: str
    value: float


@dataclass(frozen=True, slots=True)
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

    def __post_init__(
        self, o: float, h: float, l: float, c: float, v: float
    ) -> None:  # noqa: E741
        # pylint: disable=invalid-name
        self._o = Decimal(o)
        self._h = Decimal(h)
        self._l = Decimal(l)
        self._c = Decimal(c)
        self._v = Decimal(v)

    @property
    def open(self) -> float:
        """Open price of the quote."""
        return float(self._o)

    @property
    def high(self) -> float:
        """High price of the quote."""
        return float(self._h)

    @property
    def low(self) -> float:
        """Low price of the quote."""
        return float(self._l)

    @property
    def close(self) -> float:
        """Close price of the quote."""
        return float(self._c)

    @property
    def vol(self) -> float:
        """Volume of the quote."""
        return float(self._v)

    @property
    def hl2(self) -> float:
        """The average of the high and low prices."""
        return float((self._h + self._l) / 2)

    @property
    def hlc3(self) -> float:
        """The average of the high, low, and close prices."""
        return float((self._h + self._l + self._c) / 3)

    @property
    def oc2(self) -> float:
        """The average of the open and close prices."""
        return float((self._o + self._c) / 2)

    @property
    def ohl3(self) -> float:
        """The average of the open, high, and low prices."""
        return float((self._o + self._h + self._l) / 3)

    @property
    def ohlc4(self) -> float:
        """The average of the open, high, low, and close prices."""
        return float((self._o + self._h + self._l + self._c) / 4)

    @property
    def hlc(self) -> Hlc:
        """The high, low, and close prices."""
        return Hlc(high=self.high, low=self.low, close=self.close)

    @property
    def open_with_vol(self) -> PriceDataWithVol:
        """The open price with volume."""
        return PriceDataWithVol(
            value=self.open, time_stamp=self.time.isoformat(), volume=self.vol
        )

    @property
    def high_with_vol(self) -> PriceDataWithVol:
        """The high price with volume."""
        return PriceDataWithVol(
            value=self.high, time_stamp=self.time.isoformat(), volume=self.vol
        )

    @property
    def low_with_vol(self) -> PriceDataWithVol:
        """The low price with volume."""
        return PriceDataWithVol(
            value=self.low, time_stamp=self.time.isoformat(), volume=self.vol
        )

    @property
    def close_with_vol(self) -> PriceDataWithVol:
        """The close price with volume."""
        return PriceDataWithVol(
            value=self.close, time_stamp=self.time.isoformat(), volume=self.vol
        )

    @property
    def hl2_with_vol(self) -> PriceDataWithVol:
        """The hl2 price with volume."""
        return PriceDataWithVol(
            value=self.hl2, time_stamp=self.time.isoformat(), volume=self.vol
        )

    @property
    def hlc3_with_vol(self) -> PriceDataWithVol:
        """The hlc3 price with volume."""
        return PriceDataWithVol(
            value=self.hlc3, time_stamp=self.time.isoformat(), volume=self.vol
        )

    @property
    def oc2_with_vol(self) -> PriceDataWithVol:
        """The oc2 price with volume."""
        return PriceDataWithVol(
            value=self.oc2, time_stamp=self.time.isoformat(), volume=self.vol
        )

    @property
    def ohl3_with_vol(self) -> PriceDataWithVol:
        """The ohl3 price with volume."""
        return PriceDataWithVol(
            value=self.ohl3, time_stamp=self.time.isoformat(), volume=self.vol
        )

    @property
    def ohlc4_with_vol(self) -> PriceDataWithVol:
        """The ohlc4 price with volume."""
        return PriceDataWithVol(
            value=self.ohlc4, time_stamp=self.time.isoformat(), volume=self.vol
        )

    @classmethod
    def empty(cls) -> Self:
        """Return an empty quote."""
        return cls(time=datetime.min, o=0, h=0, l=0, c=0, v=0)

    @property
    def is_empty(self) -> bool:
        """Whether or not the quote is empty."""
        return self.time == datetime.min

    def to_price_data(self, candle_part: CandlePart) -> PriceData:  # type: ignore
        """Convert the Quote to PriceData."""
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

    def to_price_data_with_vol(self, candle_part: CandlePart) -> PriceDataWithVol:
        """converts Quote to PriceDataWithVol"""
        price_data = self.to_price_data(candle_part)
        return PriceDataWithVol(
            value=price_data.value, time_stamp=price_data.time_stamp, volume=self.vol
        )

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
        """
        Attempt to create a quote from the given values.

        Return an ErrMsg if validation fails.
        """
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
