# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from collections.abc import Callable
from dataclasses import dataclass
from math import nan

from pure_ta._sma import get_sma
from pure_ta._std_dev import get_st_dev


@dataclass
class BollingerResult:
    """Result of a Bollinger Band calculation."""

    upper: float
    middle: float
    lower: float


def get_bb(len: int = 20, multi: int = 2) -> Callable[[float], BollingerResult]:
    counter = 0
    sma = get_sma(length=len)
    st_dev = get_st_dev(len=len)

    def compute(value: float) -> BollingerResult:
        nonlocal counter
        counter += 1
        avg = sma(value)
        std = st_dev(value)

        if counter < len:
            return BollingerResult(upper=nan, lower=nan, middle=nan)
        else:
            return BollingerResult(
                upper=avg + multi * std, lower=avg - multi * std, middle=avg
            )

    return compute
