import pytest
from get_matrix import spiral_order


def test_one():
    m = [[1]]
    assert spiral_order(m) == [1]


def test_square():
    m = [
        [1, 2],
        [3, 4]
    ]
    assert spiral_order(m) == [1, 3, 4, 2]


def test_unsquare():
    m = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    assert spiral_order(m) == [1, 3, 5, 6, 4, 2]
