# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from collections.abc import Callable
from math import isnan, nan

from pure_ta._circular_buf import CircularBuf
from pure_ta._types import PriceDataWithVol


def get_mfi(length: int = 14) -> Callable[[PriceDataWithVol], float]:
    """Get Money Flow Index (MFI)."""
    upper_buffer = CircularBuf(size=length)
    lower_buffer = CircularBuf(size=length)
    prev = nan

    def mfi(data: PriceDataWithVol) -> float:
        nonlocal prev
        value = data.value
        vol = data.volume
        change = 0.0 if isnan(prev) else value - prev
        mf = vol * value  # Raw Money Flow

        if change > 0:
            upper = mf
            lower = 0.0
        elif change < 0:
            upper = 0.0
            lower = mf
        else:
            upper = 0.0
            lower = 0.0

        upper_buffer.put(upper)
        lower_buffer.put(lower)

        prev = value

        if upper_buffer.is_full and lower_buffer.is_full:
            upper_sum = sum(upper_buffer.values)
            lower_sum = sum(lower_buffer.values)

            if lower_sum != 0:
                mf_ratio = upper_sum / lower_sum
                return 100 - (100 / (mf_ratio + 1))
            else:
                return 100
        else:
            return float("nan")

    return mfi
