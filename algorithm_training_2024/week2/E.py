def solution(lst):
    if len(lst) == 1:
        return lst

    res = []
    n = len(lst)
    lst.sort()

    if n % 2 == 1:
        res.append(lst[n // 2])
        lst.remove(lst[n // 2])
        n -= 1

    left = (n // 2) - 1
    right = n // 2

    while left >= 0 and right < n:
        res.append(lst[left])
        left -= 1
        res.append(lst[right])
        right += 1

    return res


assert solution([19, 3, 8]) == [8, 3, 19]
assert solution([1, 2, 4, 2]) == [2, 2, 1, 4]
assert solution([2, 3, 4, 1, 6, 5, 7]) == [4, 3, 5, 2, 6, 1, 7]
assert solution([2, 2]) == [2, 2]
assert solution([0]) == [0]


if __name__ == "__main__":
    input()
    lst = list(map(int, input().split()))
    print(*solution(lst))
