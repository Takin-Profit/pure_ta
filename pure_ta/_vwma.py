# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from collections.abc import Callable

from pure_ta._sma import get_sma
from pure_ta._types import PriceDataWithVol


def get_vwma(length: int = 20) -> Callable[[PriceDataWithVol], float]:
    """Returns a function that calculates the volume weighted moving average."""
    sma1 = get_sma(length=length)
    sma2 = get_sma(length=length)

    def vwma_func(data: PriceDataWithVol) -> float:
        return sma1(data.value * data.volume) / sma2(data.volume)

    return vwma_func
