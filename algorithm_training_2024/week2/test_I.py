from I import *
import random
import timeit
from functools import partial


def test_slow_solution():
    assert slow_solution(
        5, [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 0, 1, 0, 0]
    ) == [1, 5, 2, 4, 3]
    assert slow_solution(
        4, [3, 3, 3, 3], [3, 3, 3, 3], [1, 0, 1, 0]
    ) == [1, 2, 3, 4]
    assert slow_solution(
        3, [10, 20, 30], [30, 20, 10], [0, 0, 0]
    ) == [3, 2, 1]
    assert slow_solution(
        1, [5], [10], [0]
    ) == [1]
    assert slow_solution(
        6, [3, 3, 6, 1, 5, 3], [4, 4, 2, 2, 7, 6], [1, 1, 1, 1, 1, 1]
    ) == [5, 6, 1, 2, 3, 4]
    assert slow_solution(
        6, [3, 3, 6, 1, 5, 3], [4, 4, 2, 2, 7, 6], [0, 0, 0, 0, 0, 0]
    ) == [3, 5, 6, 1, 2, 4]
    assert slow_solution(
        6, [3, 3, 6, 1, 5, 3], [4, 4, 2, 2, 7, 6], [0, 1, 1, 0, 0, 1]
    ) == [3, 5, 6, 1, 2, 4]


def test_solution():
    assert solution(
        5, [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 0, 1, 0, 0]
    ) == [1, 5, 2, 4, 3]
    assert solution(
        4, [3, 3, 3, 3], [3, 3, 3, 3], [1, 0, 1, 0]
    ) == [1, 2, 3, 4]
    assert solution(
        3, [10, 20, 30], [30, 20, 10], [0, 0, 0]
    ) == [3, 2, 1]
    assert slow_solution(
        1, [5], [10], [0]
    ) == [1]
    assert solution(
        6, [3, 3, 6, 1, 5, 3], [4, 4, 2, 2, 7, 6], [1, 1, 1, 1, 1, 1]
    ) == [5, 6, 1, 2, 3, 4]
    assert solution(
        6, [3, 3, 6, 1, 5, 3], [4, 4, 2, 2, 7, 6], [0, 0, 0, 0, 0, 0]
    ) == [3, 5, 6, 1, 2, 4]
    assert solution(
        6, [3, 3, 6, 1, 5, 3], [4, 4, 2, 2, 7, 6], [0, 1, 1, 0, 0, 1]
    ) == [3, 5, 6, 1, 2, 4]


def test_random():
    n = 100
    min_value = 1
    max_value = 10

    for _ in range(10000):
        random_a = [random.randint(min_value, max_value) for _ in range(n)]
        random_b = [random.randint(min_value, max_value) for _ in range(n)]
        random_p = [random.choice([0, 1]) for _ in range(n)]

        assert (solution(n, random_a, random_b, random_p)
                == slow_solution(n, random_a, random_b, random_p))


# def test_load_slow_solution():
#     n = 10 ** 5
#     min_value = 10 ** 8
#     max_value = 10 ** 9
#
#     res = []
#
#     for _ in range(1):
#         random_a = [random.randint(min_value, max_value) for _ in range(n)]
#         random_b = [random.randint(min_value, max_value) for _ in range(n)]
#         random_p = [random.choice([0, 1]) for _ in range(n)]
#         execution_time = timeit.timeit(partial(slow_solution, n, random_a, random_b, random_p), number=1)
#         res.append(execution_time)
#
#     print(sum(res) / len(res))
#     assert sum(res) / len(res) < 1


def test_load_solution():
    n = 10 ** 5
    min_value = 10 ** 8
    max_value = 10 ** 9

    res = []

    for _ in range(100):
        random_a = [random.randint(min_value, max_value) for _ in range(n)]
        random_b = [random.randint(min_value, max_value) for _ in range(n)]
        random_p = [random.choice([0, 1]) for _ in range(n)]
        execution_time = timeit.timeit(partial(solution, n, random_a, random_b, random_p), number=1)
        res.append(execution_time)

    print(sum(res) / len(res))
    assert sum(res) / len(res) < 1

