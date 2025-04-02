def solution(lst):
    total = sum(lst)
    h = total // 2

    cur_sum = 0
    med = 0
    for i, elem in enumerate(lst):
        cur_sum += elem
        if cur_sum > h:
            med = i
            break

    res = sum(abs(i - med) * elem for i, elem in enumerate(lst))

    return res


def slow_solution(lst):
    n = len(lst)
    min_moves = float('inf')

    for openspace in range(n):
        left_moves = sum(lst[i] * abs(openspace - i) for i in range(openspace))
        right_moves = sum(lst[i] * abs(openspace - i) for i in range(openspace + 1, n))
        total_moves = left_moves + right_moves

        min_moves = min(min_moves, total_moves)

    return min_moves


if __name__ == '__main__':
    input()
    lst = list(map(int, input().split()))
    print(solution(lst))
