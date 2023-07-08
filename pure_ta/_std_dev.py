# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from collections.abc import Callable
from math import sqrt

from pure_ta._circular_buf import CircularBuf
from pure_ta._enum_types import StDevOf


def get_st_dev(
    len: int = 20, bias: StDevOf = StDevOf.POPULATION
) -> Callable[[float], float]:
    buf = CircularBuf(size=len)
    sum_ = 0.0
    sum_of_squares = 0.0

    def divisor() -> int:
        if bias == StDevOf.POPULATION:
            return len
        elif len - 1 > 0:
            return len - 1
        else:
            raise ValueError("Cannot calculate sample stdev for buffer of length 1")

    def compute(data: float) -> float:
        nonlocal sum_, sum_of_squares

        old_val = buf.first if buf.is_full else 0.0

        # update the buffer
        buf.put(data)

        sum_ += data - old_val
        sum_of_squares += data**2 - old_val * old_val

        if not buf.is_full:
            return float("nan")

        mean = sum_ / len
        mean_of_squares = sum_of_squares / len
        variance = mean_of_squares - mean * mean
        adjusted_variance = variance * len / divisor()  # Adjust variance for bias

        return sqrt(adjusted_variance)

    return compute
