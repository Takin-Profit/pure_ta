# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from collections.abc import Callable
from math import isnan, nan


def get_rsi(len: int = 14) -> Callable[[float], float]:
    last_value = nan
    avg_gain = 0.0
    avg_loss = 0.0
    count = 0

    def rsi(current_value: float) -> float:
        nonlocal last_value, avg_gain, avg_loss, count

        gain = 0.0
        loss = 0.0

        if not isnan(last_value):
            change = current_value - last_value
            gain = max(0, change)
            loss = max(0, -change)

        if count < len:
            # Calculating the first average gain and loss
            avg_gain = ((avg_gain * count) + gain) / (count + 1)
            avg_loss = ((avg_loss * count) + loss) / (count + 1)
        else:
            # Calculating the subsequent average gain and loss
            avg_gain = ((avg_gain * (len - 1)) + gain) / len
            avg_loss = ((avg_loss * (len - 1)) + loss) / len

        count += 1
        last_value = current_value

        if count < len:
            return nan
        rs = avg_gain / avg_loss if avg_loss != 0 else nan

        return nan if isnan(rs) else 100 - (100 / (rs + 1))

    return rsi
