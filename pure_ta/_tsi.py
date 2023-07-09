# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from collections.abc import Callable
from dataclasses import dataclass
from math import isnan, nan

from pure_ta._ema import get_ema


def double_smooth(long: int, short: int) -> Callable[[float], float]:
    ema_short = get_ema(length=short)
    ema_long = get_ema(length=long)

    def apply_double_smooth(value: float) -> float:
        return ema_short(ema_long(value))

    return apply_double_smooth


@dataclass
class TsiResult:
    """The result of calculating the TSI indicator."""

    tsi: float
    signal: float


def get_tsi(
    len: int = 25, smooth_len: int = 13, signal_len: int = 13
) -> Callable[[float], TsiResult]:
    last_value = None
    double_smooth_pc = double_smooth(long=len, short=smooth_len)
    double_smooth_apc = double_smooth(long=len, short=smooth_len)
    ema_signal = get_ema(length=signal_len)

    def tsi_function(value: float) -> TsiResult:
        nonlocal last_value

        pc = nan
        apc: float = nan

        if last_value is not None:
            pc = value - last_value
            apc = abs(pc)

        last_value = value

        double_smooth_pc_value = double_smooth_pc(pc)
        double_smooth_apc_value = double_smooth_apc(apc)

        if isnan(double_smooth_pc_value) or isnan(double_smooth_apc_value):
            return TsiResult(tsi=float("nan"), signal=float("nan"))

        tsi = (
            double_smooth_pc_value * 100 / double_smooth_apc_value
            if double_smooth_apc_value != 0
            else 0
        )
        signal = ema_signal(tsi)

        return TsiResult(tsi=tsi, signal=signal)

    return tsi_function
