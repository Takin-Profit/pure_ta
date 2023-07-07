# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from collections.abc import Callable
from math import fabs, isfinite, isnan, nan

from pure_ta._types import Hlc


def get_tr(handle_na: bool = True) -> Callable[[Hlc], float]:
    prev_close = nan

    def tr_func(q: Hlc) -> float:
        nonlocal prev_close

        if isnan(prev_close) and handle_na:
            true_range = (
                q.high - q.low
            )  # If prevClose is nan and handleNa is true, calculate as high-low
        elif isfinite(prev_close):
            high_close = fabs(q.high - prev_close)
            low_close = fabs(q.low - prev_close)

            true_range = max(q.high - q.low, max(high_close, low_close))
        else:
            true_range = nan  # If prevClose is null and handleNa is false, return NaN

        prev_close = q.close

        return true_range

    return tr_func
