from A import solution


def test_manual():
    assert solution(
        [10, 5, 3], [12, 4, 4]
    ) == (2, [1, 0, 2])

    assert solution(
        [10, 7, 3, 2], [8, 8, 4, 3]
    ) == (3, [0, 1, 2, 3])

    assert solution(
        [1, 2, 3], [10, 10, 10, 10]
    ) == (3, [3, 2, 1])

    assert solution(
        [100, 100, 100], [1, 1, 1]
    ) == (0, [0, 0, 0])

    assert solution(
        [2, 2, 2], [3, 3, 3]
    ) == (3, [1, 2, 3])

    assert solution(
        [2, 2, 2], [2, 2, 2, 2, 2, 3]
    ) == (1, [6, 0, 0])

    assert solution(
        [2, 2, 2], [2, 2, 2, 2]
    ) == (0, [0, 0, 0])

    assert solution(
        [5, 4, 3, 2, 1], [6, 5, 4, 3]
    ) == (4, [1, 2, 3, 4, 0])

    assert solution(
        [3, 2, 1, 4, 5], [6, 5, 4, 3]
    ) == (4, [3, 4, 0, 2, 1])
