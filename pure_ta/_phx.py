# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from collections.abc import Callable
from dataclasses import dataclass

from pure_ta._linreg import get_linreg
from pure_ta._mfi import get_mfi
from pure_ta._rsi import get_rsi
from pure_ta._sma import get_sma
from pure_ta._tci import get_tci
from pure_ta._tsi import get_tsi
from pure_ta._types import Quote
from pure_ta._willy import get_willy


@dataclass(frozen=True, slots=True)
class PhoenixResult:
    """The result of the Phoenix Oscillator."""

    fast: float
    slow: float
    lsma: float


def get_phx() -> Callable[[Quote], PhoenixResult]:
    get_rsi_ = get_rsi(length=3)
    get_mfi_ = get_mfi(length=3)
    get_tsi_ = get_tsi(length=9, smooth_len=6)
    get_sma_ = get_sma(length=6)
    get_willy_ = get_willy(length=6)
    get_tci_ = get_tci(length=9)
    get_linreg_ = get_linreg(length=32)

    def phx_fn(quote: Quote):
        hlc3 = quote.hlc3
        tci = get_tci_(hlc3)
        mfi = get_mfi_(quote.hlc3_with_vol)
        willy = get_willy_(hlc3)
        rsi = get_rsi_(hlc3)
        tsi = get_tsi_(quote.open).tsi / 100

        csi = (rsi + (tsi * 50 + 50)) / 2
        phx = (tci + csi + mfi + willy) / 4
        trad = (tci + mfi + rsi) / 3
        fast = (phx + trad) / 2

        slow = get_sma_(fast)
        lsma = get_linreg_(fast)

        return PhoenixResult(fast=fast, slow=slow, lsma=lsma)

    return phx_fn
