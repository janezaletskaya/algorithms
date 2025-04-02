from D import *


def test_solution():
    assert solution2([3, 8, 5, 7, 1, 2, 4, 9, 6], 2) == 3
    assert solution2([4, 2, 1], 2) == 2
    assert solution2([1, 3, 1], 0) == 2
    assert solution2([32, 77, 1, 100], 4) == 1
    assert solution2([2, 1, 1, 1, 5, 5, 2, 1, 2], 1) == 7
    assert solution2([1, 2, 5, 7, 13], 2) == 2

    assert solution2([1, 1, 1, 1, 1], 22) == 5
    assert solution2([1, 1, 1, 1, 1], 0) == 5
    assert solution2([1, 2, 3, 4, 5], 0) == 1
    assert solution2([1, 2, 3, 4, 5], 2) == 3

