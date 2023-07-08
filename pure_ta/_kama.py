# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from collections.abc import Callable
from math import isnan, nan

from pure_ta._er import get_er


def get_kama(length: int = 10) -> Callable[[float], float]:
    """Returns a function that calculates the Kaufman's Adaptive Moving Average."""
    er = get_er(length=length)

    kama = [0.0]
    fast = 2.0 / (2.0 + 1.0)
    slow = 2.0 / (30.0 + 1.0)

    def kama_func(price: float) -> float:
        er_value = er(price)
        if isnan(er_value):
            return nan

        er_value = abs(er_value) / 100.0
        sc = pow(er_value * (fast - slow) + slow, 2)

        kama[0] = price if kama[0] == 0.0 else kama[0] + sc * (price - kama[0])

        return kama[0]

    return kama_func
