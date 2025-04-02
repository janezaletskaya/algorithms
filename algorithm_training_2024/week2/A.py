input()
lst = list(map(int, input().split()))


def solution(lst):
    res = [0] * len(lst)
    res[0] = lst[0]
    for i in range(1, len(lst)):
        res[i] = res[i - 1] + lst[i]

    return res


print(*solution(lst))

