# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from collections.abc import Callable
from math import nan

from pure_ta._circular_buf import CircularBuf


def get_wma(length: int = 15) -> Callable[[float], float]:
    buf = CircularBuf(size=length)
    divisor = float(length) * (length + 1) / 2.0

    def wma_func(data: float) -> float:
        buf.put(data)

        if buf.is_full:
            sum_ = 0.0
            ordered_values = list(buf.ordered_values)[::-1]  # reverse the order
            for i in range(length):
                weight = length - i
                sum_ += ordered_values[i] * weight

            return sum_ / divisor
        else:
            return nan

    return wma_func
