from C import *


def test_solution():
    assert solution([1, 3, 2, 4, 5, 3, 1], 3) == [1, 2, 2, 3, 1]
    assert solution([1, 2, 3, 4, 5, 6, 7], 1) == [1, 2, 3, 4, 5, 6, 7]
    assert solution([1, 2, 3], 3) == [1]
    assert solution([1, 1, 1, 1, 1, 1], 2) == [1, 1, 1, 1, 1]
