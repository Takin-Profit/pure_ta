# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from collections.abc import Callable
from math import nan

from pure_ta._circular_buf import CircularBuf


def get_er(length: int = 10) -> Callable[[float], float]:
    """Returns a function that calculates the efficiency ratio."""
    buf = CircularBuf(size=length + 1)

    def er(price: float) -> float:
        buf.put(price)

        if not buf.is_full:
            return nan

        total_abs_change = 0.0
        prev_price = buf.first

        for current_price in list(buf.ordered_values)[1:]:
            total_abs_change += abs(current_price - prev_price)
            prev_price = current_price

        net_change = price - buf.first

        return (net_change / total_abs_change) * 100 if total_abs_change != 0 else 0.0

    return er
