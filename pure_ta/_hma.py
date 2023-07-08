# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from collections.abc import Callable
from math import isnan, nan, sqrt

from pure_ta._wma import get_wma


def get_hma(length: int = 16) -> Callable[[float], float]:
    wma_n = get_wma(length=length)
    wma_n_by_2 = get_wma(length=length // 2)
    wma_sqrt_n = get_wma(length=round(sqrt(length)))

    def hma_func(data: float) -> float:
        wma_n_val = wma_n(data)
        wma_n_by_2_val = wma_n_by_2(data)

        if isnan(wma_n_val) or isnan(wma_n_by_2_val):
            return nan

        raw_hma = wma_n_by_2_val * 2 - wma_n_val

        return wma_sqrt_n(raw_hma)

    return hma_func
