#  Автоматизированный склад
from collections import deque


class RoadQueue:

    def __init__(self):
        self.queue = deque()

    def push_rover(self, rover):
        self.queue.append(rover)

    def popleft_rover(self):
        if self.queue:
            return self.queue.popleft()

    def __repr__(self):
        return self.queue.__repr__()


class Regulator:

    def __init__(self, main1, main2, roads):
        self.roads = roads

        minor1, minor2 = tuple({1, 2, 3, 4} - {main1, main2})
        self.roads_order = self._get_roads_order(main1, main2) + self._get_roads_order(minor1, minor2)

    def get_rovers_gone(self):
        rovers_gone = []
        for roads in self.roads_order:
            for road in roads:
                rover = self.roads[road].popleft_rover()
                if rover:
                    rovers_gone.append(rover)
            if rovers_gone:
                return rovers_gone
        return []

    @staticmethod
    def _get_roads_order(k, m):
        roads_order = []
        diff = abs(k - m)
        if diff == 2:
            roads_order.append((k, m))
        elif diff == 1:
            roads_order.append((min(k, m),))
            roads_order.append((max(k, m),))
        elif diff == 3:
            roads_order.append((max(k, m),))
            roads_order.append((min(k, m),))

        return roads_order


def solution(n, rovers_by_time, a, b):
    res = [0] * n

    roads = {
        1: RoadQueue(),
        2: RoadQueue(),
        3: RoadQueue(),
        4: RoadQueue(),
    }

    regulator = Regulator(a, b, roads)

    for minute in range(1, 200):
        if minute <= 100:
            rovers_in_minute = rovers_by_time[minute]
            for rover in rovers_in_minute:
                roads[rover[0]].push_rover(rover)

        rovers_gone = regulator.get_rovers_gone()
        for rover in rovers_gone:
            res[rover[1]] = minute

    return res


if __name__ == '__main__':
    n = int(input())
    a, b = map(int, input().split())
    rovers_by_time = [[] for _ in range(101)]  # type: list[list[tuple[int,int]]]

    for i in range(n):
        direction_i, time_i = map(int, input().split())
        rovers_by_time[time_i].append((direction_i, i))

    print(*solution(n, rovers_by_time, a, b), sep='\n')
