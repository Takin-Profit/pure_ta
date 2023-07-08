"""A circular buffer implementation backed by a deque."""
import math
from collections import deque
from collections.abc import Generator, Iterable
from typing import Any


class CircularBuf:
    """A circular buffer."""

    def __init__(self, size: int):
        self._buffer: deque[float] = deque(maxlen=size)
        self._size = size

    @property
    def filled_size(self) -> int:
        """The number of values in the buffer."""
        return len(self._buffer)

    @property
    def values(self) -> Iterable[float]:
        """The values in the buffer."""
        return list(self._buffer) if self._buffer else []

    @property
    def ordered_values(self) -> Generator[float, Any, None]:
        """Values in the buffer ordered from oldest to newest."""
        yield from self._buffer

    @property
    def first(self) -> float:
        """The oldest value in the buffer."""
        return self._buffer[0] if self.is_full else math.nan

    @property
    def last(self) -> float:
        """The newest value in the buffer."""
        return self._buffer[-1] if self.is_full else math.nan

    @property
    def length(self) -> int:
        """The size of the buffer."""
        return self._size

    @property
    def is_full(self) -> bool:
        """Whether the buffer is full."""
        return len(self._buffer) == self._size

    def put(self, value: float) -> None:
        """Put a value into the buffer."""
        self._buffer.append(value)
