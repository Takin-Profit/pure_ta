# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from collections.abc import Callable
from math import isnan

from pure_ta._ema import get_ema


def get_tema(length: int = 20) -> Callable[[float], float]:
    """Returns a function that calculates the triple exponential moving average."""
    ema1 = get_ema(length)
    ema2 = get_ema(length)
    ema3 = get_ema(length)

    def tema_function(data: float) -> float:
        ema1_val = ema1(data)
        ema2_val = ema2(ema1_val)
        ema3_val = ema3(ema2_val)

        if isnan(ema1_val) or isnan(ema2_val) or isnan(ema3_val):
            return float("nan")

        return (ema1_val * 3) - (ema2_val * 3) + ema3_val

    return tema_function
