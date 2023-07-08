# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from collections.abc import Callable
from math import isnan, nan

from pure_ta._circular_buf import CircularBuf


def get_mom(length: int = 20) -> Callable[[float], float]:
    prices = CircularBuf(size=length + 1)

    def inner(close: float):
        if isnan(close):
            return close

        prices.put(close)

        return nan if prices.filled_size < length + 1 else close - prices.first

    return inner
