from B import solution


def check_solution(input_array, expected_cnt=None, expected_lengths=None):
    cnt, lengths = solution(input_array)

    assert cnt == len(lengths), "Количество отрезков не совпадает с длинами"
    assert sum(lengths) == len(input_array), "Суммарная длина отрезков не равна длине входного массива"

    idx = 0
    for length in lengths:
        segment = input_array[idx:idx + length]
        assert all(x >= length for x in segment), f"Нарушено условие в сегменте {segment} длины {length}"
        idx += length

    if expected_cnt is not None:
        assert cnt == expected_cnt, f"Ожидалось {expected_cnt} отрезков, получено {cnt}"

    if expected_lengths is not None:
        assert lengths == expected_lengths, f"Ожидались длины {expected_lengths}, получено {lengths}"


def test_manual():
    check_solution([3, 3, 2, 2, 4, 5, 1], expected_cnt=4, expected_lengths=[2, 2, 2, 1])
    check_solution([1, 1, 1, 1], expected_cnt=4, expected_lengths=[1, 1, 1, 1])
    check_solution([10, 10, 10, 10], expected_cnt=1, expected_lengths=[4])
    check_solution([1], expected_cnt=1, expected_lengths=[1])
    check_solution([2, 2], expected_cnt=1, expected_lengths=[2])
    check_solution([3, 1, 3], expected_cnt=3, expected_lengths=[1, 1, 1])
    check_solution([2, 1], expected_cnt=2, expected_lengths=[1, 1])

    check_solution([1000] * 1000, expected_cnt=1, expected_lengths=[1000])
    check_solution([1] * 1000, expected_cnt=1000, expected_lengths=[1] * 1000)
