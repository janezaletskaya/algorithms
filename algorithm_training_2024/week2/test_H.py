from H import *
import random
import timeit
from functools import partial


def test_random():
    n = 50
    min_value = 1
    max_value = 100000000

    for _ in range(10000):
        random_list = [random.randint(min_value, max_value) for _ in range(n)]

        assert solution(random_list) == slow_solution(random_list)


def test_load():
    n = 2 * 10 ** 5
    min_value = 10 ** 8
    max_value = 10 ** 9
    res = []

    for _ in range(100):
        random_list = [random.randint(min_value, max_value) for _ in range(n)]
        execution_time = timeit.timeit(partial(solution, random_list), number=1)
        res.append(execution_time)

    assert sum(res) / len(res) < 1


def test_solution():
    assert solution([5, 2, 3, 1]) == 10
    assert solution([5, 4, 3, 2, 1]) == 15

