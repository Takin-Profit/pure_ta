""" A circular buffer implementation for storing values in a fixed size array.
    """
from array import array
from typing import Iterable


class CircularBuf:
    """A circular buffer implementation for storing values
    in a fixed size array."""

    def __init__(self, size: int):
        self._buffer = array("d", [0.0] * size)
        self._start = 0
        self._counter = 0

    @property
    def filled_size(self) -> int:
        """the number of values in the buffer."""
        return self._counter

    @property
    def values(self) -> Iterable[float]:
        """the values in the buffer."""
        return self._buffer if self.is_full else array("d")

    @property
    def ordered_values(self) -> Iterable[float]:
        """values in the buffer ordered from oldest to newest."""
        if self.is_full:
            for i in range(len(self._buffer)):
                yield self._buffer[(self._start + i) % len(self._buffer)]

    @property
    def first(self) -> float:
        """the oldest value in the buffer."""
        return (
            self._buffer[self._start]
            if self._counter > 0 and self.is_full
            else float("nan")
        )

    @property
    def last(self) -> float:
        """the newest value in the buffer."""
        return (
            self._buffer[
                (self._start - 1 + len(self._buffer)) % len(self._buffer)
            ]  # noqa: E501
            if self.is_full
            else float("nan")
        )

    @property
    def length(self) -> int:
        """the size of the buffer."""
        return len(self._buffer)

    @property
    def is_full(self) -> bool:
        """whether the buffer is full."""
        return self._counter >= len(self._buffer)

    def put(self, value: float) -> None:
        """put a value into the buffer."""
        self._buffer[self._start] = value
        self._start = (self._start + 1) % len(self._buffer)
        self._counter = min(self._counter + 1, len(self._buffer))
        self._counter = min(self._counter + 1, len(self._buffer))
