def solution(lst):
    prefix_sum = [0] * len(lst)
    prefix_sum[0] = lst[0]
    for i in range(1, len(lst)):
        prefix_sum[i] = prefix_sum[i - 1] + lst[i]

    res = 0

    for left in range(len(lst) - 2):
        for right in range(left + 1, len(lst) - 1):
            cur_sum = prefix_sum[-1] - prefix_sum[right]
            res += lst[left] * lst[right] * cur_sum
            res %= 1000000007

    return res


def solution2(lst):
    res = 0
    for first in range(len(lst) - 2):
        for second in range(first + 1, len(lst) - 1):
            for third in range(second + 1, len(lst)):
                res += lst[first] * lst[second] * lst[third]
                res %= 1000000007

    return res


def solution3(lst):
    prefix_sum = [0] * len(lst)
    prefix_sum[0] = lst[0]
    for i in range(1, len(lst)):
        prefix_sum[i] = prefix_sum[i - 1] + lst[i]

    res = 0

    for pointer in range(1, len(lst) - 1):
        res += prefix_sum[pointer - 1] * lst[pointer] * (prefix_sum[-1] - prefix_sum[pointer])
        res %= 1000000007

    return res


if __name__ == "__main__":
    input()
    lst = list(map(int, input().split()))
    print(solution3(lst))