def solution(lst, k):
    res = 0
    dct = {}

    cur_sum = 0
    dct[0] = 1

    for elem in lst:
        cur_sum += elem

        if (cur_sum - k) in dct:
            res += dct[cur_sum - k]

        dct[cur_sum] = dct.get(cur_sum, 0) + 1

    return res


assert (solution([17, 7, 10, 7, 10], 17)) == 4
assert (solution([1, 2, 3, 4, 1], 10)) == 2


if __name__ == "__main__":
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    print(solution(lst, k))
