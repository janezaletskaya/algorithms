from collections import deque


class MinDeque:
    def __init__(self):
        self.deque = deque()

    def push(self, x):
        while self.deque and self.deque[-1] > x:
            self.deque.pop()
        self.deque.append(x)

    def popleft(self, x):
        if self.deque and self.deque[0] == x:
            self.deque.popleft()

    def get_min(self):  # тут не может быть такого, что deque пуст
        return self.deque[0]


def correct_solution(lst, k):
    queue = MinDeque()
    res = []

    for i in range(k):
        queue.push(lst[i])

    res.append(queue.get_min())

    for i in range(k, len(lst)):
        queue.popleft(lst[i - k])
        queue.push(lst[i])
        res.append(queue.get_min())

    return res


if __name__ == '__main__':
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    print(*correct_solution(lst, k), sep='\n')