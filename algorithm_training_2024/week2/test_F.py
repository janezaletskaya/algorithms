from F import *
import random


def test_random():
    n = 10
    min_value = 1
    max_value = 100

    for _ in range(10000):
        random_list = [random.randint(min_value, max_value) for _ in range(n)]

        assert solution(random_list) == solution2(random_list) == solution3(random_list)


def test_manual():
    assert solution([0, 0, 0, 0, 0, 0]) == 0
    assert solution2([0, 0, 0, 0, 0, 0]) == 0

    assert solution([1, 2, 3]) == 6
    assert solution2([1, 2, 3]) == 6

    assert solution([1, 1, 1, 1]) == 4
    assert solution2([1, 1, 1, 1]) == 4

    assert solution([0, 5, 6, 7]) == 210
    assert solution2([0, 5, 6, 7]) == 210


    assert solution2([1, 2, 3, 4, 5]) == 225
    assert solution3([1, 2, 3, 4, 5]) == 225
