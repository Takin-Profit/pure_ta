# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from collections.abc import Callable

from pure_ta._bbw import get_bbw
from pure_ta._percent_rank import get_percent_rank


def get_bbwp(length: int = 13) -> Callable[[float], float]:
    percent_rank = get_percent_rank(len=252)
    bbw = get_bbw(length=length, multi=1)

    def compute(data: float) -> float:
        bbw_value = bbw(data)

        return percent_rank(bbw_value)

    return compute
