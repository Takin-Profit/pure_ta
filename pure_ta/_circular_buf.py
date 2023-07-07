"""A circular buffer implementation for storing values in a fixed size array."""
import math
from array import array
from collections.abc import Generator, Iterable
from typing import Any


class CircularBuf:
    """A circular buffer.

    implementation for storing values
    in a fixed size array.
    """

    def __init__(self, size: int):
        self._buffer = array("d", [0.0] * size)
        self._start = 0
        self._counter = 0

    @property
    def filled_size(self) -> int:
        """The number of values in the buffer."""
        return self._counter

    @property
    def values(self) -> Iterable[float]:
        """The values in the buffer."""
        return self._buffer if self.is_full else array("d")

    @property
    def ordered_values(self) -> Generator[float, Any, None]:
        """Values in the buffer ordered from oldest to newest."""
        if self.is_full:
            for i in range(len(self._buffer)):
                yield self._buffer[(self._start + i) % len(self._buffer)]

    @property
    def first(self) -> float:
        """The oldest value in the buffer."""
        return (
            self._buffer[self._start]
            if self._counter > 0 and self.is_full
            else math.nan
        )

    @property
    def last(self) -> float:
        """The newest value in the buffer."""
        return (
            self._buffer[
                (self._start - 1 + len(self._buffer)) % len(self._buffer)
            ]  # noqa: E501
            if self.is_full
            else math.nan
        )

    @property
    def length(self) -> int:
        """The size of the buffer."""
        return len(self._buffer)

    @property
    def is_full(self) -> bool:
        """Whether the buffer is full."""
        return self._counter >= len(self._buffer)

    def put(self, value: float) -> None:
        """Put a value into the buffer."""
        self._buffer[self._start] = value
        self._start = (self._start + 1) % len(self._buffer)
        self._counter = min(self._counter + 1, len(self._buffer))
