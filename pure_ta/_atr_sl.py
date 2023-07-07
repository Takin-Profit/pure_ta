# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from collections.abc import Callable

from pure_ta._ema import get_ema
from pure_ta._enum_types import AtrSlMaType
from pure_ta._rma import get_rma
from pure_ta._sma import get_sma
from pure_ta._tr import get_tr
from pure_ta._types import Hlc
from pure_ta._wma import get_wma


def _get_ma_type(length: int, ma_type: AtrSlMaType) -> Callable[[float], float]:
    match ma_type:
        case AtrSlMaType.SMA:
            return get_sma(length)
        case AtrSlMaType.WMA:
            return get_wma(length)
        case AtrSlMaType.EMA:
            return get_ema(length)
        case AtrSlMaType.RMA:
            return get_rma(length)


def get_atr_sl(
    length: int = 14, ma_type: AtrSlMaType = AtrSlMaType.RMA, multi: float = 1.5
) -> Callable[[Hlc], tuple[float, float]]:
    short_ma = _get_ma_type(length, ma_type)
    long_ma = _get_ma_type(length, ma_type)
    tr = get_tr()  # Assuming `get_tr` is defined elsewhere and returns a callable

    def atr_sl_func(data: Hlc) -> tuple[float, float]:
        true_range = tr(data)

        long_sl = data.low - long_ma(true_range) * multi
        short_sl = short_ma(true_range) * multi + data.high

        return long_sl, short_sl

    return atr_sl_func
