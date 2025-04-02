from collections import deque
from I_additional import solution, Regulator, RoadQueue
import timeit
from functools import partial


def rovers_to_time(rovers: list[tuple[int, int]]):
    rovers_by_time = [[] for _ in range(101)]  # type: list[list[tuple[int,int]]]
    for i, rover in enumerate(rovers):
        direction_i, time_i = rover
        rovers_by_time[time_i].append((direction_i, i))

    return rovers_by_time


def gen_rovers():
    res1 = []
    for t in range(75, 100):
        res1.append((1, t))
        res1.append((2, t))
        res1.append((3, t))
        res1.append((4, t))
    return res1


def test_queue():
    q = RoadQueue()

    q.push_rover((4, 3, 1))
    assert q.queue == deque([(4, 3, 1)])

    q.push_rover((2, 4, 2))
    assert q.queue == deque([(4, 3, 1), (2, 4, 2)])
    assert q.popleft_rover() == (4, 3, 1)
    assert q.popleft_rover() == (2, 4, 2)
    assert q.popleft_rover() is None


def test_time():
    res1 = gen_rovers()
    ans1 = []
    for r in range(25):
        ans1.append(r + 100)
        ans1.append(r + 125)
        ans1.append(r + 150)
        ans1.append(r + 75)

    execution_time = timeit.timeit(partial(solution, 100, rovers_to_time(res1), 1, 4), number=1)

    print(execution_time)
    assert execution_time < 1


def test_corner_solution():
    res1 = gen_rovers()
    ans1 = []
    for r in range(25):
        ans1.append(r+100)
        ans1.append(r+125)
        ans1.append(r+150)
        ans1.append(r+75)

    assert solution(100, rovers_to_time(res1), 1, 4) == ans1

    res2 = gen_rovers()
    ans2 = []
    for r in range(25):
        ans2.append(r+75)
        ans2.append(r+100)
        ans2.append(r+75)
        ans2.append(r+100)

    assert solution(100, rovers_to_time(res2), 1, 3) == ans2


def test_solution():
    assert solution(5,
                    rovers_to_time([(1, 4), (1, 3), (1, 2), (4, 1), (4, 2)]),
                    1, 4) == [5, 4, 3, 1, 2]
    assert solution(4,
                    rovers_to_time([(1, 1), (3, 1), (2, 1), (2, 2)]),
                    1, 3) == [1, 1, 2, 3]
    assert solution(4,
                    rovers_to_time([(1, 1), (2, 1), (3, 1), (4, 1)]),
                    1, 2) == [1, 2, 3, 4]
    assert solution(
        1, rovers_to_time([(1, 1)]), 1, 4
    ) == [1]
    assert solution(4, rovers_to_time([(3, 1), (1, 2), (2, 2), (2, 1)]),
                    1, 3) == [1, 2, 4, 3]
    assert solution(
        6, rovers_to_time([(3, 1), (3, 2), (3, 3), (4, 1), (4, 2), (4, 3)]), 3, 4
    ) == [1, 2, 3, 4, 5, 6]
    assert solution(4, rovers_to_time([(1, 1), (1, 2), (3, 1), (3, 2)]), 3, 2) == [3, 4, 1, 2]
    assert solution(4, rovers_to_time([(1, 1), (1, 2), (3, 1), (3, 2)]), 3, 4) == [3, 4, 1, 2]
    assert solution(4, rovers_to_time([(1, 1), (1, 2), (3, 1), (3, 2)]), 1, 4) == [1, 2, 3, 4]
    assert solution(4, rovers_to_time([(1, 1), (1, 2), (3, 1), (3, 2)]), 1, 2) == [1, 2, 3, 4]
    assert solution(5, rovers_to_time([(2, 1), (1, 1), (4, 1), (3, 2), (3, 4)]), 1, 4) == [3, 2, 1, 4, 5]
    assert solution(27,
                    rovers_to_time([(4, 59), (4, 66), (3, 25), (3, 79), (2, 8), (4, 94), (2, 32), (1, 2),
    (3, 41), (1, 43), (2, 29), (4, 61), (4, 34), (2, 20), (3, 66), (3, 100),
    (3, 75), (3, 87), (2, 97), (1, 73), (3, 93), (1, 71), (1, 67), (3, 43),
    (2, 95), (2, 82), (2, 77)]), 4, 3) == [59, 67, 25, 79, 8, 94, 32, 2, 41,
                                         44, 29, 61, 34, 20, 66, 100, 75, 87, 97,
                                         73, 93, 71, 68, 43, 95, 82, 77]

    assert solution(1, rovers_to_time([(4, 77)]), 1, 2) == [77]
    assert solution(1, rovers_to_time([(4, 77)]), 2, 3) == [77]
    assert solution(1, rovers_to_time([(4, 77)]), 1, 3) == [77]
    assert solution(1, rovers_to_time([(4, 77)]), 1, 4) == [77]
    assert solution(1, rovers_to_time([(4, 77)]), 2, 3) == [77]

    assert solution(1, rovers_to_time([(4, 100)]), 2, 3) == [100]


def test_get_roads_order():
    assert Regulator(1, 2, {}).roads_order == [(1,), (2,), (3,), (4,)]
    assert Regulator(2, 1, {}).roads_order == [(1,), (2,), (3,), (4,)]

    assert Regulator(1, 4, {}).roads_order == [(4,), (1,), (2,), (3,)]
    assert Regulator(4, 1, {}).roads_order == [(4,), (1,), (2,), (3,)]

    assert Regulator(2, 3, {}).roads_order == [(2,), (3,), (4,), (1,)]
    assert Regulator(3, 2, {}).roads_order == [(2,), (3,), (4,), (1,)]

    assert Regulator(3, 4, {}).roads_order == [(3,), (4,), (1,), (2,)]
    assert Regulator(4, 3, {}).roads_order == [(3,), (4,), (1,), (2,)]

    assert Regulator(1, 3, {}).roads_order == [(1, 3), (2, 4)]
    assert Regulator(3, 1, {}).roads_order == [(3, 1), (2, 4)]
    assert Regulator(2, 4, {}).roads_order == [(2, 4), (1, 3)]
    assert Regulator(4, 2, {}).roads_order == [(4, 2), (1, 3)]