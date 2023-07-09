# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
import math
from collections.abc import Callable

from pure_ta._circular_buf import CircularBuf


def get_willy(length: int = 6) -> Callable[[float], float]:
    """Returns a function that calculates the WILLY."""
    buf = CircularBuf(size=length)

    def willy_func(data: float) -> float:
        buf.put(data)

        if buf.is_full:
            high = max(buf.values)
            low = min(buf.values)

            return 60 * (data - high) / (high - low) + 80
        else:
            return math.nan

    return willy_func
