from collections import deque


def one_experiment(lst, start, k):
    cur_count = 0
    cur_idx = start

    while cur_idx > 0 and lst[cur_idx - 1] <= lst[cur_idx]:
        if lst[cur_idx - 1] == lst[cur_idx]:
            cur_count += 1
            if cur_count > k:
                return cur_idx
        cur_idx -= 1

    return cur_idx


def slow_solution(lst, starts, k):
    # len(lst) > 0, каждый элемент lst > 0
    # 0 <= k <= len(lst)
    # каждый элемент starts: 1 <= elem <= len(lst)

    res = []
    for start in starts:
        start -= 1  # индексация с 0
        res.append(one_experiment(lst, start, k) + 1)

    return res


def solution(lst, starts, k):
    left_limit = [0] * len(lst)
    left_limit[0] = 0

    identical_cnt = 0
    queue = deque()

    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            left_limit[i] = i
        else:
            if lst[i] == lst[i - 1]:
                identical_cnt += 1
                queue.append(i)

                if len(queue) > k:
                    idx = queue.popleft()
                    left_limit[i] = max(idx, left_limit[i - 1])
                else:
                    left_limit[i] = left_limit[i - 1]

            else:
                left_limit[i] = left_limit[i - 1]

    result = []
    for start in starts:
        result.append(left_limit[start - 1] + 1)

    return result


if __name__ == '__main__':
    input()
    lst = list(map(int, input().split()))
    m, k = map(int, input().split())
    starts = list(map(int, input().split()))
    print(*solution(lst, starts, k))

