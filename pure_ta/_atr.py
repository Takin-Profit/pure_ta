# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from collections.abc import Callable
from math import isnan, nan

from pure_ta._rma import get_rma
from pure_ta._types import Hlc


def get_atr(length: int = 14) -> Callable[[Hlc], float]:
    """Return a function that calculates the ATR (Average True Range)."""
    prev_close = nan
    rma_func = get_rma(length)

    def atr_func(q: Hlc) -> float:
        nonlocal prev_close
        high_low = q.high - q.low
        high_close = high_low if isnan(prev_close) else abs(q.high - prev_close)
        low_close = high_low if isnan(prev_close) else abs(q.low - prev_close)

        true_range = max(high_low, high_close, low_close)
        prev_close = q.close

        return rma_func(true_range)

    return atr_func
