# Кровать из стульев
from collections import deque


class MaxDeque:

    def __init__(self):
        self.deque = deque()

    def push(self, x):
        while self.deque and self.deque[-1] < x:
            self.deque.pop()

        self.deque.append(x)

    def popleft(self, x):
        if self.deque and self.deque[0] == x:
            self.deque.popleft()

    def get_max(self):
        if not self.deque:
            return 0
        return self.deque[0]

    def __repr__(self):
        return self.deque.__repr__()


def fast_solution(chairs, W):
    if len(chairs) == 1:
        return 0

    chairs = sorted(chairs, key=lambda x: x[0])
    min_inc = float('inf')

    left = 0
    right = 0
    cur_W = chairs[right][1]
    max_deque = MaxDeque()
    max_deque.push(0)

    while True:
        if cur_W < W:
            right += 1
            if right >= len(chairs):
                break
            max_deque.push(chairs[right][0] - chairs[max(right - 1, left)][0])
            cur_W += chairs[right][1]

        else:
            cur_inc = max_deque.get_max()
            if cur_inc == 0:
                return 0

            min_inc = min(min_inc, cur_inc)
            cur_W -= chairs[left][1]
            max_deque.popleft(chairs[min(left + 1, right)][0] - chairs[left][0])
            left += 1

    return min_inc


if __name__ == '__main__':
    n, H = map(int, input().split())
    chairs = list(zip(list(map(int, input().split())), list(map(int, input().split()))))
    print(fast_solution(chairs, H))
