# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from collections.abc import Callable
from math import nan

from pure_ta._bb import get_bb


def get_bbw(length: int = 5, multi: int = 4) -> Callable[[float], float]:
    get_bb_func = get_bb(length=length, multi=multi)

    def compute(value: float) -> float:
        bb = get_bb_func(value)

        return (bb.upper - bb.lower) / bb.middle if bb.middle != 0 else nan

    return compute
