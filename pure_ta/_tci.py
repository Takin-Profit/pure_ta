# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
import math
from collections.abc import Callable
from math import nan

from pure_ta._circular_buf import CircularBuf


def get_tci(length: int = 9) -> Callable[[float], float]:
    ema_src = math.inf
    ema_diff_abs = math.inf
    ema_tci_raw = math.inf
    data_buffer = CircularBuf(size=length)

    def tci(data: float) -> float:
        nonlocal ema_src, ema_diff_abs, ema_tci_raw
        data_buffer.put(data)

        if data_buffer.is_full:
            if ema_src == math.inf:
                # Initialize emaSrc, emaDiffAbs and emaTCIRaw using SMA
                ema_src = sum(data_buffer.ordered_values) / length
                diff_sum = sum(abs(val - ema_src) for val in data_buffer.ordered_values)
                ema_diff_abs = diff_sum / length
                tci_raw_sum = sum(
                    (val - ema_src) / (0.025 * abs(val - ema_src))
                    for val in data_buffer.ordered_values
                )
                ema_tci_raw = tci_raw_sum / 6
            else:
                # Update emaSrc, emaDiffAbs and emaTCIRaw
                ema_src = (2 / (length + 1)) * data + (1 - 2 / (length + 1)) * ema_src
                diff_abs = abs(data - ema_src)
                ema_diff_abs = (2 / (length + 1)) * diff_abs + (
                    1 - 2 / (length + 1)
                ) * ema_diff_abs
                tci_raw = (data - ema_src) / (ema_diff_abs * 0.025)
                ema_tci_raw = (2 / (6 + 1)) * tci_raw + (1 - 2 / (6 + 1)) * ema_tci_raw

            return ema_tci_raw + 50
        else:
            return nan

    return tci
