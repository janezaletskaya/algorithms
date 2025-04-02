def solution(lst, r):
    # гарантируется, что len(lst) >= 2
    left = 0
    right = left + 1
    res = 0
    while abs(lst[left] - lst[-1]) > r:
        if abs(lst[left] - lst[right]) <= r:
            right += 1

        else:
            res += len(lst) - right
            left += 1

            if right == left:
                right += 1

    return res


assert solution([1, 3, 5, 8], 4) == 2


if __name__ == "__main__":
    n, r = map(int, input().split())
    lst = list(map(int, input().split()))
    print(solution(lst, r))
