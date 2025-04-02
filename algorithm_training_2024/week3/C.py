# минимум на отрезке
from collections import deque


def solution(lst, k):
    queue = deque()
    left = 0
    right = k
    res = []

    for i in range(k):
        if not queue or queue[-1] < lst[i]:
            queue.append(lst[i])
        else:
            while queue and queue[-1] > lst[i]:
                queue.pop()
            queue.append(lst[i])

    while right < len(lst):
        out_elem = lst[left]
        in_elem = lst[right]

        if out_elem == queue[0]:
            res.append(queue.popleft())
        else:
            res.append(queue[0])

        if not queue or queue[-1] < in_elem:
            queue.append(in_elem)
        else:
            while queue and queue[-1] > in_elem:
                queue.pop()
            queue.append(in_elem)

        left += 1
        right += 1

    res.append(queue[0])

    return res


if __name__ == '__main__':
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    print(*solution(lst, k), sep='\n')