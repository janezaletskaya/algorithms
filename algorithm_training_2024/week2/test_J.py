from J import slow_solution, one_experiment, solution
import random


def test_random():
    n = 10
    min_value = 1
    max_value = 100

    m = 5
    min_value_m = 1
    max_value_n = n

    for _ in range(100):
        random_list = [random.randint(min_value, max_value) for _ in range(n)]
        random_starts = [random.randint(min_value_m, max_value_n) for _ in range(m)]
        expected = slow_solution(random_list, random_starts, k=2)
        actual = solution(random_list, random_starts, k=2)

        if expected != actual:
            print("Input list:", random_list)
            print("Starts:", random_starts)
            print("Expected:", expected)
            print("Actual:", actual)
            assert False


def test_random_load():
    n = 4 * 10 ** 5
    min_value = 10 ** 8
    max_value = 10 ** 9
    res = []

    m = 4 * 10 ** 5
    min_value_m = 0

    for _ in range(100):
        random_list = [random.randint(min_value, max_value) for _ in range(n)]
        m_list = [random.randint(min_value_m, n) for _ in range(m)]
        execution_time = timeit.timeit(partial(solution, random_list, m_list, 2), number=1)
        res.append(execution_time)

    print(sum(res) / len(res))
    assert sum(res) / len(res) < 2


def test_load():
    n = 4 * 10 ** 5
    res = []

    m = 4 * 10 ** 5

    for k in range(100):
        lst1 = k*[1] + list(range(1, n-k+1))
        print(len(lst1))
        m_list = [n for _ in range(m)]
        execution_time = timeit.timeit(partial(solution, lst1, m_list, k), number=1)
        res.append(execution_time)

    print(sum(res) / len(res))

    assert sum(res) / len(res) < 2


def test_one_experiment():
    assert one_experiment([3, 3, 3, 4, 4, 5], 4, 2) == 1
    assert one_experiment([3, 3, 3, 4, 4, 5], 5, 2) == 1
    assert one_experiment([8, 10, 13, 13, 13, 10, 7], 6, 3) == 6
    assert one_experiment([8, 10, 13, 13, 13, 10, 7], 5, 3) == 5
    assert one_experiment([8, 10, 13, 13, 13, 10, 7], 4, 3) == 0
    assert one_experiment([8, 10, 13, 13, 13, 10, 7], 4, 2) == 0

    assert one_experiment([16, 60, 58, 86, 40, 100, 19, 2, 2, 38], 8, 0) == 8
    assert one_experiment(
        [2, 2, 3, 3, 1, 3, 1, 3, 1, 3, 2, 2, 3, 3, 1, 3, 1, 3, 1, 3, 2, 2, 3, 3], 23, 5
    ) == 20


def test_slow_solution():
    assert slow_solution(
        [16, 60, 58, 86, 40, 100, 19, 2, 2, 38], [5, 8, 9, 9, 9], 2
    ) == [5, 8, 8, 8, 8]
    assert slow_solution(
        [1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6], 0
    ) == [1, 2, 3, 4, 5, 6]
    assert slow_solution(
        [5, 5, 5, 5, 5, 5], [6, 5, 4, 3, 2, 1], 2
    ) == [4, 3, 2, 1, 1, 1]
    assert slow_solution(
        [3, 4] * 10, [20, 10, 5, 15], 1
    ) == [19, 9, 5, 15]
    assert slow_solution(
        list(range(10, 0, -1)), [10, 5, 1], 3
    ) == [10, 5, 1]
    assert slow_solution(
        list(range(1, 11)), [10, 5, 1], 3
    ) == [1, 1, 1]
    assert slow_solution(
        [1] * 10 + [2] * 10 + [3] * 10, [15, 25, 10], 3
    ) == [12, 22, 7]
    assert slow_solution(
        [4, 4, 4, 4, 5, 5, 5, 6, 6, 6], [10, 5, 1], 2
    ) == [7, 2, 1]
    assert slow_solution(
        [1, 3, 1, 3, 1, 3, 2, 2, 3, 3] * 10, [50, 70, 90], 5
    ) == [47, 67, 87]
    assert slow_solution(
        [1, 3, 1, 3, 1, 3, 2, 2, 3, 3] * 20, [50, 70, 90, 110, 150], 3
    ) == [47, 67, 87, 107, 147]


def test_solution():
    assert solution(
        [16, 60, 58, 86, 40, 100, 19, 2, 2, 38], [5, 8, 9, 9, 9], 2
    ) == [5, 8, 8, 8, 8]
    assert solution(
        [1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6], 0
    ) == [1, 2, 3, 4, 5, 6]
    assert solution(
        [1, 3, 2, 3], [4], 0
    ) == [3]
    assert solution(
        [5, 5, 5, 5, 5, 5], [6, 5, 4, 3, 2, 1], 2
    ) == [4, 3, 2, 1, 1, 1]
    assert solution(
        [3, 4] * 10, [20, 10, 5, 15], 1
    ) == [19, 9, 5, 15]
    assert solution(
        list(range(10, 0, -1)), [10, 5, 1], 3
    ) == [10, 5, 1]
    assert solution(
        list(range(1, 11)), [10, 5, 1], 3
    ) == [1, 1, 1]
    assert solution(
        [1] * 10 + [2] * 10 + [3] * 10, [15, 25, 10], 3
    ) == [12, 22, 7]
    assert solution(
        [4, 4, 4, 4, 5, 5, 5, 6, 6, 6], [10, 5, 1], 2
    ) == [7, 2, 1]
    assert solution(
        [1, 3, 1, 3, 1, 3, 2, 2, 3, 3] * 10, [50, 70, 90], 5
    ) == [47, 67, 87]
    assert solution(
        [2, 2, 3, 3, 1, 3, 1, 3, 1, 3, 2, 2, 3, 3, 1, 3, 1, 3, 1, 3, 2, 2, 3, 3], [24], 5
    ) == [21]
    assert solution(
        [1, 3, 1, 3, 1, 3, 2, 2, 3, 3] * 20, [50, 70, 90, 110, 150], 3
    ) == [47, 67, 87, 107, 147]
