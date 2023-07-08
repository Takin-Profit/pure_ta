# flake8: noqa
# pylint: disable=missing-function-docstring
import codecs
import os
from datetime import datetime
from typing import Any, Generator

import pytest

from pure_ta._types import Quote


def quote_from_csv(data: str, use_timestamp: bool = False) -> Quote:
    """converts a csv string to a Quote object."""
    row = data.split(",")
    dt = (
        datetime.fromtimestamp(int(row[0]))
        if use_timestamp
        else datetime.fromisoformat(row[0])
    )
    open_ = float(row[1])
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = float(row[5])

    return Quote(time=dt, o=open_, h=high, l=low, c=close, v=volume)


def _read_file_stream(filename: str, days: int = 500) -> Generator[Quote, Any, None]:
    filepath = os.path.join("tests", "data", filename)
    with codecs.open(filepath, "r", encoding="utf-8") as file:
        next(file)  # Skip the header row
        for _, line in zip(range(days), file):
            yield quote_from_csv(line)


def _get_quotes(filename: str, days: int, use_timestamp: bool = False):
    filepath = os.path.join("tests", "data", filename)
    with codecs.open(filepath, "r", encoding="utf-8") as file:
        lines = file.readlines()
        quotes = [
            quote_from_csv(data, use_timestamp=use_timestamp)
            for data in lines[
                1 : 1 + days
            ]  # Skip the header row and limit to 'days' rows
        ]
    return quotes


@pytest.fixture(scope="package")
def get_default(days: int = 502) -> list[Quote]:
    """gets the default quotes."""
    return _get_quotes("default.csv", days)


@pytest.fixture(scope="package")
def get_zeroes(days: int = 200) -> list[Quote]:
    return _get_quotes("zeroes.csv", days)


@pytest.fixture(scope="package")
def get_eth_rma(days: int = 500):
    return _get_quotes("eth_rma.csv", days, use_timestamp=True)


@pytest.fixture(scope="package")
def get_btc_mfi(days: int = 820):
    return _get_quotes("btc_mfi.csv", days)


@pytest.fixture(scope="package")
def get_eth_er(days: int = 600):
    return _get_quotes("eth_er.csv", days, use_timestamp=True)


@pytest.fixture(scope="package")
def get_gold_lin_reg(days: int = 900):
    return _get_quotes("gold_linreg.csv", days, use_timestamp=True)


@pytest.fixture(scope="package")
def get_gold_tci(days: int = 900):
    return _get_quotes("gold_tci.csv", days, use_timestamp=True)


@pytest.fixture(scope="package")
def get_gold_willy(days: int = 1000):
    return _get_quotes("gold_willy.csv", days)


@pytest.fixture(scope="package")
def get_eur_usd_phx(days: int = 700):
    return _get_quotes("eurusd_phx.csv", days)


@pytest.fixture(scope="package")
def get_eth_swma(days: int = 600):
    return _get_quotes("eth_swma.csv", days, use_timestamp=True)


@pytest.fixture(scope="package")
def get_eth_kama(days: int = 600):
    return _get_quotes("eth_kama.csv", days, use_timestamp=True)


@pytest.fixture(scope="package")
def get_eth_bbwp(days: int = 700):
    return _get_quotes("eth_bbwp.csv", days, use_timestamp=True)


@pytest.fixture(scope="package")
def get_gold_atr(days: int = 750):
    return _get_quotes("gold_atr.csv", days, use_timestamp=True)


@pytest.fixture(scope="package")
def get_btc_mom(days: int = 800):
    return _get_quotes("btc_mom.csv", days, use_timestamp=True)


@pytest.fixture(scope="package")
def get_atr_sl_rma(days: int = 800):
    return _get_quotes("atrsl_rma.csv", days, use_timestamp=True)


@pytest.fixture(scope="package")
def get_atr_sl_sma(days: int = 800):
    return _get_quotes("atrsl_sma.csv", days, use_timestamp=True)


@pytest.fixture(scope="package")
def get_atr_sl_ema(days: int = 800):
    return _get_quotes("atrsl_ema.csv", days, use_timestamp=True)


@pytest.fixture(scope="package")
def get_atr_sl_wma(days: int = 800):
    return _get_quotes("atrsl_wma.csv", days, use_timestamp=True)


@pytest.fixture(scope="package")
def get_btc_tr(days: int = 420):
    return _get_quotes("btc_tr.csv", days, use_timestamp=True)


@pytest.fixture(scope="package")
def get_crude_percent_rank(days: int = 630):
    return _get_quotes("%_rank_crude.csv", days, use_timestamp=True)


@pytest.fixture(scope="package")
def get_eth_bbw(days: int = 630):
    return _get_quotes("eth_bbw.csv", days, use_timestamp=True)


@pytest.fixture(scope="package")
def get_spx_alma(days: int = 396):
    return _get_quotes("eth_bbw.csv", days)


@pytest.fixture(scope="package")
def get_btc_tsi(days: int = 900):
    return _get_quotes("btc_tsi.csv", days)


def get_longish(days: int = 5285):  # type: ignore
    yield from _read_file_stream("longish.csv", days)
