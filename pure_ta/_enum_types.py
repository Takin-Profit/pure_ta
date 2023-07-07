"""common enum types used throughout the library."""
from datetime import timedelta
from enum import Enum, StrEnum


class StDevOf(StrEnum):
    """the type of standard deviation to calculate."""

    POPULATION = "Population"
    SAMPLE = "Sample"


class CandlePart(StrEnum):
    """the part of the candle to calculate indicators for."""

    OPEN = "Open"
    HIGH = "High"
    LOW = "Low"
    CLOSE = "Close"
    VOLUME = "Volume"
    HL2 = "Hl2"
    HLC3 = "Hlc3"
    OC2 = "Oc2"
    OHL3 = "Ohl3"
    OHLC4 = "Ohlc4"


class EndType(StrEnum):
    """the type of end to calculate indicators for."""

    CLOSE = "Close"
    HIGH_LOW = "HighLow"


class Match(Enum):
    """matches trend direction."""

    BEAR_CONFIRMED = -200
    BEAR_SIGNAL = -100
    BEAR_BASIS = -10
    NONE = 0
    NEUTRAL = 1
    BULL_BASIS = 10
    BULL_SIGNAL = 100
    BULL_CONFIRMED = 200


class AtrSlMaType(StrEnum):
    """the moving average type to use for the atr stop loss."""

    RMA = "Rma"
    SMA = "Sma"
    EMA = "Ema"
    WMA = "Wma"


class MaType(StrEnum):
    """moving average type to use for certain indicators."""

    ALMA = "Alma"
    DEMA = "Dema"
    LSMA = "Lsma"
    EMA = "Ema"
    HMA = "Hma"
    KAMA = "Kama"
    RMA = "Rma"
    SMA = "Sma"
    SWMA = "Swma"
    SMMA = "Smma"
    TEMA = "Tema"
    VWMA = "Vwma"
    WMA = "Wma"


class TimeFrame(StrEnum):
    """represents a time frame to calculate indicators for."""

    MONTH = "MONTH"
    THREE_WEEKS = "THREE_WEEKS"
    TWO_WEEKS = "TWO_WEEKS"
    WEEK = "WEEK"
    THIRTY_DAYS = "THIRTY_DAYS"
    TWENTY_DAYS = "TWENTY_DAYS"
    FIFTEEN_DAYS = "FIFTEEN_DAYS"
    TEN_DAYS = "TEN_DAYS"
    FIVE_DAYS = "FIVE_DAYS"
    FOUR_DAYS = "FOUR_DAYS"
    THREE_DAYS = "THREE_DAYS"
    TWO_DAYS = "TWO_DAYS"
    ONE_DAY = "ONE_DAY"
    TWENTY_HOURS = "TWENTY_HOURS"
    EIGHTEEN_HOURS = "EIGHTEEN_HOURS"
    SIXTEEN_HOURS = "SIXTEEN_HOURS"
    FOURTEEN_HOURS = "FOURTEEN_HOURS"
    TWELVE_HOURS = "TWELVE_HOURS"
    EIGHT_HOURS = "EIGHT_HOURS"
    TEN_HOURS = "TEN_HOURS"
    SIX_HOURS = "SIX_HOURS"
    FOUR_HOURS = "FOUR_HOURS"
    THREE_HOURS = "THREE_HOURS"
    TWO_HOURS = "TWO_HOURS"
    ONE_HOUR = "ONE_HOUR"
    THREE_HUNDRED_NINETY_MIN = "THREE_HUNDRED_NINETY_MIN"
    TWO_HUNDRED_SIXTY_MIN = "TWO_HUNDRED_SIXTY_MIN"
    ONE_HUNDRED_THIRTY_MIN = "ONE_HUNDRED_THIRTY_MIN"
    SIXTY_FIVE_MIN = "SIXTY_FIVE_MIN"
    FORTY_FIVE_MIN = "FORTY_FIVE_MIN"
    THIRTY_MIN = "THIRTY_MIN"
    TWENTY_FOUR_MIN = "TWENTY_FOUR_MIN"
    FIFTEEN_MIN = "FIFTEEN_MIN"
    TWELVE_MIN = "TWELVE_MIN"
    FIVE_MIN = "FIVE_MIN"
    THREE_MIN = "THREE_MIN"
    ONE_MIN = "ONE_MIN"

    def to_time_delta(self) -> timedelta:
        """Converts a TimeFrame to a timedelta."""
        match self:
            case TimeFrame.MONTH:
                # this will never get used
                # here to satisfy mypy
                return timedelta(days=30)
            case TimeFrame.THREE_WEEKS:
                return timedelta(days=21)
            case TimeFrame.TWO_WEEKS:
                return timedelta(days=14)
            case TimeFrame.WEEK:
                return timedelta(days=7)
            case TimeFrame.THIRTY_DAYS:
                return timedelta(days=30)
            case TimeFrame.TWENTY_DAYS:
                return timedelta(days=20)
            case TimeFrame.FIFTEEN_DAYS:
                return timedelta(days=15)
            case TimeFrame.TEN_DAYS:
                return timedelta(days=10)
            case TimeFrame.FIVE_DAYS:
                return timedelta(days=5)
            case TimeFrame.FOUR_DAYS:
                return timedelta(days=4)
            case TimeFrame.THREE_DAYS:
                return timedelta(days=3)
            case TimeFrame.TWO_DAYS:
                return timedelta(days=2)
            case TimeFrame.ONE_DAY:
                return timedelta(days=1)
            case TimeFrame.TWENTY_HOURS:
                return timedelta(hours=20)
            case TimeFrame.EIGHTEEN_HOURS:
                return timedelta(hours=18)
            case TimeFrame.SIXTEEN_HOURS:
                return timedelta(hours=16)
            case TimeFrame.FOURTEEN_HOURS:
                return timedelta(hours=14)
            case TimeFrame.TWELVE_HOURS:
                return timedelta(hours=12)
            case TimeFrame.EIGHT_HOURS:
                return timedelta(hours=8)
            case TimeFrame.TEN_HOURS:
                return timedelta(hours=10)
            case TimeFrame.SIX_HOURS:
                return timedelta(hours=6)
            case TimeFrame.FOUR_HOURS:
                return timedelta(hours=4)
            case TimeFrame.THREE_HOURS:
                return timedelta(hours=3)
            case TimeFrame.TWO_HOURS:
                return timedelta(hours=2)
            case TimeFrame.ONE_HOUR:
                return timedelta(hours=1)
            case TimeFrame.THREE_HUNDRED_NINETY_MIN:
                return timedelta(minutes=390)
            case TimeFrame.TWO_HUNDRED_SIXTY_MIN:
                return timedelta(minutes=260)
            case TimeFrame.ONE_HUNDRED_THIRTY_MIN:
                return timedelta(minutes=130)
            case TimeFrame.SIXTY_FIVE_MIN:
                return timedelta(minutes=65)
            case TimeFrame.FORTY_FIVE_MIN:
                return timedelta(minutes=45)
            case TimeFrame.THIRTY_MIN:
                return timedelta(minutes=30)
            case TimeFrame.TWENTY_FOUR_MIN:
                return timedelta(minutes=24)
            case TimeFrame.FIFTEEN_MIN:
                return timedelta(minutes=15)
            case TimeFrame.TWELVE_MIN:
                return timedelta(minutes=12)
            case TimeFrame.FIVE_MIN:
                return timedelta(minutes=5)
            case TimeFrame.THREE_MIN:
                return timedelta(minutes=3)
            case TimeFrame.ONE_MIN:
                return timedelta(minutes=1)
