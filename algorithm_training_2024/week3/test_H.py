from H import Stack, PrefixStack
from H_additional import generate_commands, multi_execution, slow_multi_execution
import timeit
from functools import partial


def test_random():
    for _ in range(100):
        commands = generate_commands(10000, 1, 100)
        assert slow_multi_execution(commands) == multi_execution(commands)


def test_load():
    n = (10 ** 5) // 2
    value = 10 ** 9
    commands = []
    for _ in range(n):
        commands.append(f'+{value}')
    for _ in range(n):
        commands.append(f'?{n}')

    execution_time = timeit.timeit(partial(multi_execution, commands), number=1)

    print(execution_time)
    assert execution_time < 1


def test_slow_multi_execution():
    assert slow_multi_execution(
        ['+1', '+2', '+3', '?2', '-', '-', '?1']
    ) == [5, 3, 2, 1]
    assert slow_multi_execution(
        ['+5', '+10', '+15', '?3', '-']
    ) == [30, 15]
    assert slow_multi_execution(
        ['+7', '+3', '-', '-', '+5', '?1']
    ) == [3, 7, 5]
    assert slow_multi_execution(
        ['+2', '+3', '+4', '+5', '?1', '?2', '?3', '?4']
    ) == [5, 9, 12, 14]
    assert slow_multi_execution(
        ['+8', '+10', '?2', '-', '+6', '?2', '-', '?1', '-']
    ) == [18, 10, 14, 6, 8, 8]


def test_multi_execution():
    assert multi_execution(
        ['+1', '+2', '+3', '?2', '-', '-', '?1']
    ) == [5, 3, 2, 1]
    assert multi_execution(
        ['+5', '+10', '+15', '?3', '-']
    ) == [30, 15]
    assert multi_execution(
        ['+7', '+3', '-', '-', '+5', '?1']
    ) == [3, 7, 5]
    assert multi_execution(
        ['+2', '+3', '+4', '+5', '?1', '?2', '?3', '?4']
    ) == [5, 9, 12, 14]
    assert multi_execution(
        ['+8', '+10', '?2', '-', '+6', '?2', '-', '?1', '-']
    ) == [18, 10, 14, 6, 8, 8]


def test_stack():
    s = Stack()
    s.push_back(5)
    s.push_back(10)
    s.push_back(15)

    assert s.stack == [5, 10, 15]
    assert s.pop_back() == 15
    assert s.stack == [5, 10]

    assert s.pop_back() == 10
    assert s.pop_back() == 5
    assert s.stack == []


def test_prefix_stack():
    ps = PrefixStack()

    assert ps.prefix_stack == [0]
    assert ps.pop_back() is None
    assert ps.prefix_stack == [0]

    ps.push_back(1)
    ps.push_back(2)
    ps.push_back(3)

    assert ps.prefix_stack == [0, 1, 3, 6]

    ps.pop_back()
    ps.pop_back()

    assert ps.prefix_stack == [0, 1]

    ps.push_back(0)
    ps.push_back(2)

    assert ps.prefix_stack == [0, 1, 1, 3]
    assert ps.count_sum(2) == 2
    assert ps.count_sum(3) == 3


