# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from collections.abc import Callable
from math import isnan, nan

from pure_ta._circular_buf import CircularBuf


def get_linreg(length: int = 9) -> Callable[[float], float]:
    buf = CircularBuf(size=length)
    x_sum = 0.0
    y_sum = 0.0
    xx_sum = 0.0
    xy_sum = 0.0
    count = 0

    def linreg(y: float) -> float:
        nonlocal x_sum, y_sum, xx_sum, xy_sum, count

        if isnan(y):
            return y

        x = float(count)

        if buf.is_full:
            first_y = buf.first
            first_x = count - length
            x_sum -= first_x
            y_sum -= first_y
            xx_sum -= first_x * first_x
            xy_sum -= first_x * first_y

        x_sum += x
        y_sum += y
        xx_sum += x**2
        xy_sum += x * y

        buf.put(y)

        if count < length - 1:
            count += 1
            return nan
        else:
            slope = (length * xy_sum - x_sum * y_sum) / (length * xx_sum - x_sum**2)
            intercept = (y_sum - slope * x_sum) / length
            count += 1

            return slope * x + intercept

    return linreg
