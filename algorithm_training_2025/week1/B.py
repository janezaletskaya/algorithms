# B. Ни больше ни меньше

def solution(array: list[int]) -> tuple[int, list[int]]:
    res = []

    cur_min = len(array) + 1
    cur_len = 0
    for i in range(len(array)):
        elem_in = array[i]
        new_min = min(cur_min, elem_in)
        if cur_len + 1 <= new_min:
            cur_len += 1
            cur_min = new_min
        else:
            res.append(cur_len)
            cur_len = 1
            cur_min = elem_in

    res.append(cur_len)

    return len(res), res


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        input()
        lst = list(map(int, input().split()))
        n_intervals, lengths = solution(lst)
        print(n_intervals)
        print(*lengths)
