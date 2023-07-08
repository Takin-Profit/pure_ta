# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
import math
from collections.abc import Callable

from pure_ta._circular_buf import CircularBuf


def get_percent_rank(len: int = 20) -> Callable[[float], float]:
    buf = CircularBuf(size=len)

    def compute(data: float) -> float:
        count = 0
        percent_rank = math.nan

        if buf.is_full:
            for value in buf.ordered_values:
                if value <= data:
                    count += 1
            percent_rank = (count * 100.0) / len

        buf.put(data)

        return percent_rank

    return compute
