# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import math
from collections.abc import Callable

from pure_ta._circular_buf import CircularBuf
from pure_ta._types import Hlc


def get_wpr(len: int = 20) -> Callable[[Hlc], float]:
    """Returns a function that calculates the Williams %R."""
    highest_buffer = CircularBuf(size=len)
    lowest_buffer = CircularBuf(size=len)

    def wpr_func(data: Hlc) -> float:
        highest_buffer.put(data.high)
        lowest_buffer.put(data.low)
        last_close = data.close

        if highest_buffer.is_full and lowest_buffer.is_full:
            highest_high = max(highest_buffer.values)
            lowest_low = min(lowest_buffer.values)

            return -100 * (highest_high - last_close) / (highest_high - lowest_low)
        else:
            return math.nan

    return wpr_func
