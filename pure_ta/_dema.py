# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from collections.abc import Callable
from math import isnan, nan

from pure_ta._ema import get_ema


def get_dema(length: int = 20) -> Callable[[float], float]:
    """Returns a function that calculates the double exponential moving average."""
    ema1 = get_ema(length)
    ema2 = get_ema(length)

    def dema_function(data: float) -> float:
        ema1_val = ema1(data)
        ema2_val = ema2(ema1_val)

        return nan if isnan(ema1_val) or isnan(ema2_val) else 2 * ema1_val - ema2_val

    return dema_function
