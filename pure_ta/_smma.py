# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from collections.abc import Callable
from math import isnan, nan

from pure_ta._circular_buf import CircularBuf


def get_smma(length: int = 20) -> Callable[[float], float]:
    buf = CircularBuf(size=length)
    smma = nan

    def smma_calculator(price: float) -> float:
        nonlocal smma

        buf.put(price)

        if isnan(smma):
            if buf.is_full:
                smma = sum(buf.ordered_values) / length
        else:
            smma = ((smma * (length - 1)) + price) / length

        return smma

    return smma_calculator
