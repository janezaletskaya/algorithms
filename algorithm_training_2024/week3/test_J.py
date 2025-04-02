from J import fast_solution
from J_additional import solution, count_inc, slow_solution, slow_count_inc
import random
import timeit
from functools import partial


def test_random_solution_vs_fast_solution():
    n = 100
    min_value = 1
    max_value = 10 ** 9

    for _ in range(100):
        random_list1 = [random.randint(min_value, max_value) for _ in range(n)]
        random_list2 = [random.randint(min_value, max_value) for _ in range(n)]
        random_lst1 = list(zip(random_list1, random_list2))
        random_lst2 = random_lst1.copy()
        random_lst3 = random_lst1.copy()
        sum_W = sum(random_list2)
        for w in [random.randint(1, sum_W) for _ in range(2*n)]:
            # assert slow_solution(random_lst1, w) == solution(random_lst2, w) == fast_solution(random_lst3, w)
            assert solution(random_lst2, w) == fast_solution(random_lst3, w)


def test_random_slow_solution_vs_fast_solution():
    n = 5
    min_value = 1
    max_value = 10 ** 9

    for _ in range(100):
        random_list1 = [random.randint(min_value, max_value) for _ in range(n)]
        random_list2 = [random.randint(min_value, max_value) for _ in range(n)]
        random_lst1 = list(zip(random_list1, random_list2))
        random_lst2 = random_lst1.copy()
        sum_W = sum(random_list2)

        for w in [random.randint(1, sum_W) for _ in range(2*n)]:
            assert slow_solution(random_lst2, w) == fast_solution(random_lst1, w)


def test_load():
    n = 2 * 10 ** 5
    val = 10 ** 9 - n
    W = 2
    hs = list(range(val, n+val))
    ws = [1 for _ in range(n)]
    lst = list(zip(hs, ws))
    execution_time = timeit.timeit(partial(fast_solution, lst, W), number=1)

    assert fast_solution(lst, W) == 1
    print(execution_time)
    assert execution_time < 1


def test_load2():
    n = 2 * 10 ** 4
    val = 10 ** 9 - n
    W = n // 2
    hs = list(range(val, n+val))
    ws = [1 for _ in range(n)]
    lst = list(zip(hs, ws))
    lst2 = lst.copy()
    execution_time1 = timeit.timeit(partial(fast_solution, lst, W), number=1)
    execution_time2 = timeit.timeit(partial(solution, lst2, W), number=1)

    print(execution_time1)
    print(execution_time2)


def test_random_count_inc():
    n = 8
    min_value = 1
    max_value = 10 ** 9

    for _ in range(100):
        random_list1 = [random.randint(min_value, max_value) for _ in range(n)]
        random_list2 = [random.randint(min_value, max_value) for _ in range(n)]
        random_lst1 = list(zip(random_list1, random_list2))
        random_lst2 = random_lst1.copy()

        assert count_inc(sorted(random_lst1)) == slow_count_inc(random_lst2)


def test_fast_solution():
    assert fast_solution(
        [(1, 3), (2, 6), (7, 5), (7, 8), (8, 7), (9, 5), (9, 9), (9, 4), (10, 4), (10, 10)], 5
    ) == 0
    assert fast_solution(
        [(1, 1), (4, 4), (1, 2), (2, 3)], 7
    ) == 2
    assert fast_solution(
        [(5, 10)], 1
    ) == 0
    assert fast_solution(
        [(5, 10)], 10
    ) == 0
    assert fast_solution(
        [(3, 5), (3, 5)], 1
    ) == 0
    assert fast_solution(
        [(3, 5), (3, 5)], 10
    ) == 0
    assert fast_solution(
        [(1, 2), (2, 2), (3, 2), (4, 2)], 6
    ) == 1
    assert fast_solution(
        [(1, 3), (5, 2), (2, 3), (7, 2), (3, 3)], 6
    ) == 1
    assert fast_solution(
        [(1, 3), (2, 2), (3, 1)], 6
    ) == 1
    assert fast_solution(
        [(100, 1), (200, 1), (300, 1), (400, 1)], 3
    ) == 100
    assert fast_solution(
        [(1, 1), (2, 1), (1, 1)], 3
    ) == 1
    assert fast_solution(
        [(100, 1), (2, 1), (1, 1)], 3
    ) == 98
    assert fast_solution(
        [(5, 1), (5, 2), (5, 3), (5, 4)], 8
    ) == 0
    assert fast_solution(
        [(5, 1), (3, 1), (4, 1), (1, 1), (2, 1)], 3
    ) == 1
    assert fast_solution(
        [(1, 1), (2, 2), (3, 3)], 1
    ) == 0
    assert fast_solution(
        [(1, 2), (2, 3), (3, 1)], 6
    ) == 1
    assert fast_solution(
        [(i, 1000) for i in range(1, 101)], 50000
    ) == 1
    assert fast_solution(
        [(1, 5), (1, 5), (2, 5), (2, 5)], 10
    ) == 0
    assert fast_solution(
        [(1, 2), (3, 2), (5, 2), (7, 2)], 8
    ) == 2
    assert fast_solution(
        [(1, 3), (5, 1), (2, 3), (4, 1), (3, 3)], 7
    ) == 1
    assert fast_solution(
        [(1, 2), (5, 2), (1, 2), (5, 2), (1, 2)], 6
    ) == 0
    assert fast_solution(
        [(1, 1), (2, 1), (3, 1), (3, 1), (2, 1), (1, 1)], 3
    ) == 1


def test_solution():
    assert solution(
        [(1, 3), (2, 6), (7, 5), (7, 8), (8, 7), (9, 5), (9, 9), (9, 4), (10, 4), (10, 10)], 5
    ) == 0
    assert solution(
        [(1, 1), (4, 4), (1, 2), (2, 3)], 7
    ) == 2
    assert solution(
        [(5, 10)], 1
    ) == 0
    assert solution(
        [(5, 10)], 10
    ) == 0
    assert solution(
        [(3, 5), (3, 5)], 1
    ) == 0
    assert solution(
        [(3, 5), (3, 5)], 10
    ) == 0
    assert solution(
        [(1, 2), (2, 2), (3, 2), (4, 2)], 6
    ) == 1
    assert solution(
        [(1, 3), (5, 2), (2, 3), (7, 2), (3, 3)], 6
    ) == 1
    assert solution(
        [(1, 3), (2, 2), (3, 1)], 6
    ) == 1
    assert solution(
        [(100, 1), (200, 1), (300, 1), (400, 1)], 3
    ) == 100
    assert solution(
        [(1, 1), (2, 1), (1, 1)], 3
    ) == 1
    assert solution(
        [(100, 1), (2, 1), (1, 1)], 3
    ) == 98
    assert solution(
        [(5, 1), (5, 2), (5, 3), (5, 4)], 8
    ) == 0
    assert solution(
        [(5, 1), (3, 1), (4, 1), (1, 1), (2, 1)], 3
    ) == 1
    assert solution(
        [(1, 1), (2, 2), (3, 3)], 1
    ) == 0
    assert solution(
        [(1, 2), (2, 3), (3, 1)], 6
    ) == 1
    assert solution(
        [(i, 1000) for i in range(1, 101)], 50000
    ) == 1
    assert solution(
        [(1, 5), (1, 5), (2, 5), (2, 5)], 10
    ) == 0
    assert solution(
        [(1, 2), (3, 2), (5, 2), (7, 2)], 8
    ) == 2
    assert solution(
        [(1, 3), (5, 1), (2, 3), (4, 1), (3, 3)], 7
    ) == 1
    assert solution(
        [(1, 2), (5, 2), (1, 2), (5, 2), (1, 2)], 6
    ) == 0
    assert solution(
        [(1, 1), (2, 1), (3, 1), (3, 1), (2, 1), (1, 1)], 3
    ) == 1


def test_slow_solution():
    assert slow_solution(
        [(1, 3), (2, 6), (7, 5), (7, 8), (8, 7), (9, 5), (9, 9), (9, 4), (10, 4), (10, 10)], 5
    ) == 0
    assert slow_solution(
        [(1, 1), (4, 4), (1, 2), (2, 3)], 7
    ) == 2
    assert slow_solution(
        [(5, 10)], 1
    ) == 0
    assert slow_solution(
        [(5, 10)], 10
    ) == 0
    assert slow_solution(
        [(3, 5), (3, 5)], 1
    ) == 0
    assert slow_solution(
        [(3, 5), (3, 5)], 10
    ) == 0
    assert slow_solution(
        [(1, 2), (2, 2), (3, 2), (4, 2)], 6
    ) == 1
    assert slow_solution(
        [(1, 3), (5, 2), (2, 3), (7, 2), (3, 3)], 6
    ) == 1
    assert slow_solution(
        [(1, 3), (2, 2), (3, 1)], 6
    ) == 1
    assert slow_solution(
        [(100, 1), (200, 1), (300, 1), (400, 1)], 3
    ) == 100
    assert slow_solution(
        [(1, 1), (2, 1), (1, 1)], 3
    ) == 1
    assert slow_solution(
        [(100, 1), (2, 1), (1, 1)], 3
    ) == 98
    assert slow_solution(
        [(5, 1), (5, 2), (5, 3), (5, 4)], 8
    ) == 0
    assert slow_solution(
        [(5, 1), (3, 1), (4, 1), (1, 1), (2, 1)], 3
    ) == 1
    assert slow_solution(
        [(1, 1), (2, 2), (3, 3)], 1
    ) == 0
    assert slow_solution(
        [(1, 2), (2, 3), (3, 1)], 6
    ) == 1
    # assert slow_solution(
    #     [(i, 1000) for i in range(1, 101)], 50000
    # ) == 1
    assert slow_solution(
        [(1, 5), (1, 5), (2, 5), (2, 5)], 10
    ) == 0
    assert slow_solution(
        [(1, 2), (3, 2), (5, 2), (7, 2)], 8
    ) == 2
    assert slow_solution(
        [(1, 3), (5, 1), (2, 3), (4, 1), (3, 3)], 7
    ) == 1
    assert slow_solution(
        [(1, 2), (5, 2), (1, 2), (5, 2), (1, 2)], 6
    ) == 0
    assert slow_solution(
        [(1, 1), (2, 1), (3, 1), (3, 1), (2, 1), (1, 1)], 3
    ) == 1


def test_count_inc():
    assert count_inc([(1, 0), (2, 0), (3, 0), (4, 0), (6, 0)]) == 2
    assert count_inc([(1, 0), (1, 0), (1, 0), (1, 0), (1, 0)]) == 0
    assert count_inc([(1, 0), (5, 0), (10, 0), (11, 0), (12, 0)]) == 5
    assert count_inc([(1, 0), (20, 0), (22, 0), (24, 0), (25, 0)]) == 19


def test_slow_count_inc():
    assert slow_count_inc([(1, 0), (2, 0), (3, 0), (4, 0), (6, 0)]) == 2
    assert slow_count_inc([(1, 0), (1, 0), (1, 0), (1, 0), (1, 0)]) == 0
    assert slow_count_inc([(1, 0), (5, 0), (10, 0), (11, 0), (12, 0)]) == 5
    assert slow_count_inc([(1, 0), (20, 0), (22, 0), (24, 0), (25, 0)]) == 19
