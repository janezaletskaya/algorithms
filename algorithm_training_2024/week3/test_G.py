from G import fast_solution
from G_additional import slow_solution, mid_solution, solution
import random
import timeit
from functools import partial


def test_random():
    n = 50
    min_value = 0
    max_value = 20

    for _ in range(10000):
        random_list = [random.randint(min_value, max_value) for _ in range(n)]
        for b in range(10):
            random_list1 = random_list.copy()
            random_list2 = random_list.copy()
            assert (slow_solution(random_list, b) == solution(random_list1, b)
                    == mid_solution(random_list2, b) == fast_solution(random_list, b))


def test_random_without_slow():
    n = 10000
    min_value = 0
    max_value = 20

    for _ in range(10):
        random_list = [random.randint(min_value, max_value) for _ in range(n)]
        for b in range(10):
            random_list1 = random_list.copy()
            random_list2 = random_list.copy()
            random_list3 = random_list.copy()

            assert (solution(random_list1, b) == mid_solution(random_list2, b) ==
                    fast_solution(random_list3, b))


def test_solution():
    assert solution([0, 0, 0, 0], 15) == 0
    assert solution([1, 1, 1, 1], 0) == 5 + 4 + 3 + 2
    assert solution([1, 5, 9], 4) == 22
    assert solution([0, 5, 1, 20, 2], 1) == 83
    assert solution([1, 5, 9], 4) == 22
    assert solution([1, 2, 1], 5) == 4
    assert solution([3, 3, 3], 1) == 21
    assert solution([2, 0, 1], 2) == 3
    assert solution([1], 1) == 1
    assert solution([0, 0, 5], 2) == 2 + 3 * 2
    assert solution([2, 2, 2], 2) == 6
    assert solution([0, 0, 0], 4) == 0
    assert solution([4, 4, 4], 4) == 3 * 4
    assert solution([10, 0, 0], 3) == 3 * 1 + 3 * 2 + 3 * 3 + 1 * 4
    assert solution([10], 5) == 15
    assert solution([1, 1, 1, 1, 1], 10) == 5
    assert solution([5, 0, 0, 0, 0], 1) == 1 + 2 + 3 + 4 + 5
    assert solution([5, 0, 0, 0, 0], 0) == 5 * 6
    assert solution([0, 6, 0, 2, 0, 3, 0], 3) == 14
    assert solution([1, 5, 7, 0, 0, 100], 4) == 22 + 96 * 2


def test_slow_solution():
    assert slow_solution([0, 0, 0, 0], 15) == 0
    assert slow_solution([1, 1, 1, 1], 0) == 5 + 4 + 3 + 2
    assert slow_solution([1, 5, 9], 4) == 22
    assert slow_solution([0, 5, 1, 20, 2], 1) == 83
    assert slow_solution([1, 5, 9], 4) == 22
    assert slow_solution([1, 2, 1], 5) == 4
    assert slow_solution([3, 3, 3], 1) == 21
    assert slow_solution([2, 0, 1], 2) == 3
    assert slow_solution([1], 1) == 1
    assert slow_solution([0, 0, 5], 2) == 2 + 3 * 2
    assert slow_solution([2, 2, 2], 2) == 6
    assert slow_solution([0, 0, 0], 4) == 0
    assert slow_solution([4, 4, 4], 4) == 3 * 4
    assert slow_solution([10, 0, 0], 3) == 3 * 1 + 3 * 2 + 3 * 3 + 1 * 4
    assert slow_solution([10], 5) == 15
    assert slow_solution([1, 1, 1, 1, 1], 10) == 5
    assert slow_solution([0, 6, 0, 2, 0, 3, 0], 3) == 14
    assert slow_solution([1, 5, 7, 0, 0, 100], 4) == 22 + 96 * 2


def test_mid_solution():
    assert mid_solution([0, 0, 0, 0], 15) == 0
    assert mid_solution([1, 1, 1, 1], 0) == 5 + 4 + 3 + 2
    assert mid_solution([1, 5, 9], 4) == 22
    assert mid_solution([0, 5, 1, 20, 2], 1) == 83
    assert mid_solution([1, 5, 9], 4) == 22
    assert mid_solution([1, 2, 1], 5) == 4
    assert mid_solution([3, 3, 3], 1) == 21
    assert mid_solution([2, 0, 1], 2) == 3
    assert mid_solution([1], 1) == 1
    assert mid_solution([0, 0, 5], 2) == 2 + 3 * 2
    assert mid_solution([2, 2, 2], 2) == 6
    assert mid_solution([0, 0, 0], 4) == 0
    assert mid_solution([4, 4, 4], 4) == 3 * 4
    assert mid_solution([10, 0, 0], 3) == 3 * 1 + 3 * 2 + 3 * 3 + 1 * 4
    assert mid_solution([10], 5) == 15
    assert mid_solution([1, 1, 1, 1, 1], 10) == 5
    assert mid_solution([0, 6, 0, 2, 0, 3, 0], 3) == 14
    assert mid_solution([1, 5, 7, 0, 0, 100], 4) == 22 + 96 * 2


def test_fast_solution():
    assert fast_solution([0, 0, 0, 0], 15) == 0
    assert fast_solution([1, 1, 1, 1], 0) == 1 + 2 + 3 + 4 + 4
    assert fast_solution([1, 5, 9], 4) == 22
    assert fast_solution([0, 5, 1, 20, 2], 1) == 83
    assert fast_solution([1, 5, 9], 4) == 22
    assert fast_solution([1, 2, 1], 5) == 4
    assert fast_solution([3, 3, 3], 1) == 21
    assert fast_solution([2, 0, 1], 2) == 3
    assert fast_solution([1], 1) == 1
    assert fast_solution([0, 0, 5], 2) == 2 + 3 * 2
    assert fast_solution([2, 2, 2], 2) == 6
    assert fast_solution([0, 0, 0], 4) == 0
    assert fast_solution([4, 4, 4], 4) == 3 * 4
    assert fast_solution([10, 0, 0], 3) == 3 * 1 + 3 * 2 + 3 * 3 + 1 * 4
    assert fast_solution([10], 5) == 15
    assert fast_solution([1, 1, 1, 1, 1], 10) == 5
    assert fast_solution([0, 6, 0, 2, 0, 3, 0], 3) == 14
    assert fast_solution([1, 5, 7, 0, 0, 100], 4) == 22 + 96 * 2


def test_load():
    max_val = 10 ** 8
    max_n = 100_000
    lst = [max_val for _ in range(max_n)]
    execution_time1 = timeit.timeit(partial(solution, lst, 1), number=1)
    execution_time2 = timeit.timeit(partial(mid_solution, lst, 1), number=1)
    execution_time3 = timeit.timeit(partial(fast_solution, lst, 1), number=1)

    print()
    print(execution_time1)
    print(execution_time2)
    print(execution_time3)
