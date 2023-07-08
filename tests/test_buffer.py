"""buffer tests."""
import math
from math import isnan

from pure_ta._circular_buf import CircularBuf


def test_circular_buf_init():
    """Test the initialization of a circular buffer."""
    size = 5
    buf = CircularBuf(size)
    assert buf.length == size
    assert buf.filled_size == 0
    assert buf.is_full is False
    assert buf.values == []
    assert isnan(buf.first)
    assert isnan(buf.last)


def test_circular_buf_put():
    """Test inserting values into the circular buffer."""
    size = 5
    buf = CircularBuf(size)
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    # sourcery skip: no-loop-in-tests
    for val in data:
        buf.put(val)

    assert buf.filled_size == size
    assert buf.is_full is True
    assert buf.first == data[0]
    assert buf.last == data[-1]


def test_circular_buf_ordered_values():
    """Test retrieving ordered values from the circular buffer."""
    size = 5
    buf = CircularBuf(size)
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    # sourcery skip: no-loop-in-tests
    for val in data:
        buf.put(val)

    ordered_data = list(buf.ordered_values)
    assert len(ordered_data) == size
    assert ordered_data == data


def test_circular_buf_overfill():
    """Test overfilling the circular buffer."""
    size = 5
    buf = CircularBuf(size)
    data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
    # sourcery skip: no-loop-in-tests
    for val in data:
        buf.put(val)

    assert buf.filled_size == size
    assert buf.is_full is True
    assert buf.first == data[2]  # First element should be the third inserted
    assert buf.last == data[-1]  # Last element should be the last inserted
    assert (
        list(buf.ordered_values) == data[2:]
    )  # Ordered values should start from the third inserted


def test_circular_buf_not_full():
    """Test the is_full property.

    should returns False when the buffer is not full.
    """
    size = 5
    buf = CircularBuf(size)
    data = [1.0, 2.0, 3.0]
    # sourcery skip: no-loop-in-tests
    for val in data:
        buf.put(val)

    assert buf.filled_size == len(data)
    assert buf.is_full is False
    assert buf.first is math.nan
    assert buf.last is math.nan


def test_circular_buf_fill_up():
    """More is_full property tests.

    Test the transition of the is_full property from False
    to True as the buffer fills up.
    """
    size = 5
    buf = CircularBuf(size)
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    # sourcery skip: no-loop-in-tests
    for i, val in enumerate(data):
        buf.put(val)
        # sourcery skip: no-conditionals-in-tests
        if i < size - 1:
            assert buf.is_full is False
        else:
            assert buf.is_full is True
