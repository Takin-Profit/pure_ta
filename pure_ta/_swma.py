# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from collections.abc import Callable

from pure_ta._circular_buf import CircularBuf


def get_swma() -> Callable[[float], float]:
    buf = CircularBuf(size=4)

    def swma(price: float):
        buf.put(price)

        # If the buffer isn't full yet, return NaN
        if not buf.is_full:
            return float("nan")

        # Retrieve the last four data points
        last_four_prices = list(buf.ordered_values)

        # Compute the SWMA
        return (
            (last_four_prices[0] * 1 / 6)
            + (last_four_prices[1] * 2 / 6)
            + (last_four_prices[2] * 2 / 6)
            + (last_four_prices[3] * 1 / 6)
        )

    return swma
