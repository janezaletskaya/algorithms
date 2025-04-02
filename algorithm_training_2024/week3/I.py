#  Автоматизированный склад
from collections import namedtuple, deque


class RoadQueue:

    def __init__(self, road_idx):
        self.road_idx = road_idx
        self.queue = deque()

    def push_rover(self, rover):
        if rover:
            self.queue.append(rover)

    def popleft_rover(self):
        if self.queue:
            return self.queue.popleft()

    def __bool__(self):
        return bool(self.queue)

    def __repr__(self):
        return self.queue.__repr__()


class Regulator:

    def __init__(self, road1, road2, road3, road4, a, b, dct):
        self.road1 = road1
        self.road2 = road2
        self.road3 = road3
        self.road4 = road4
        self.dct = dct
        self.a = a
        self.b = b

    def get_rovers_gone(self):
        rovers_gone_main = self.get_rovers_gone_main_road()
        if rovers_gone_main:
            return rovers_gone_main

        rovers_gone_minor = self.get_rovers_gone_minor_road()
        return rovers_gone_minor

    def get_rovers_gone_main_road(self):
        rovers_gone = []

        if abs(self.a - self.b) == 2:
            if self.dct[self.a] or self.dct[self.b]:
                rovers_gone.append(self.dct[self.a].popleft_rover())
                rovers_gone.append(self.dct[self.b].popleft_rover())
                return rovers_gone

        if abs(self.a - self.b) == 1:
            first_road = min(self.a, self.b)
            second_road = max(self.a, self.b)
            if self.dct[first_road]:
                rovers_gone.append(self.dct[first_road].popleft_rover())
                return rovers_gone
            if self.dct[second_road]:
                rovers_gone.append(self.dct[second_road].popleft_rover())
                return rovers_gone

        if abs(self.a - self.b) == 3:
            first_road = max(self.a, self.b)
            second_road = min(self.a, self.b)
            if self.dct[first_road]:
                rovers_gone.append(self.dct[first_road].popleft_rover())
                return rovers_gone
            if self.dct[second_road]:
                rovers_gone.append(self.dct[second_road].popleft_rover())
                return rovers_gone

        return rovers_gone

    def get_rovers_gone_minor_road(self):
        rovers_gone = []
        roads_indices = tuple({1, 2, 3, 4} - {self.a, self.b})
        c, d = roads_indices

        if abs(c - d) == 2:
            if self.dct[c] or self.dct[d]:
                rovers_gone.append(self.dct[c].popleft_rover())
                rovers_gone.append(self.dct[d].popleft_rover())

        if abs(c - d) == 1:
            first_road = min(c, d)
            second_road = max(c, d)
            if self.dct[first_road]:
                rovers_gone.append(self.dct[first_road].popleft_rover())
                return rovers_gone
            if self.dct[second_road]:
                rovers_gone.append(self.dct[second_road].popleft_rover())
                return rovers_gone

        if abs(c - d) == 3:
            first_road = max(c, d)
            second_road = min(c, d)
            if self.dct[first_road]:
                rovers_gone.append(self.dct[first_road].popleft_rover())
                return rovers_gone
            if self.dct[second_road]:
                rovers_gone.append(self.dct[second_road].popleft_rover())
                return rovers_gone

        return rovers_gone

    def __repr__(self):
        return self.road1.__repr__() + self.road2.__repr__() + self.road3.__repr__() + self.road4.__repr__()


def solution(rovers, a, b):
    rovers_by_time = [[] for _ in range(105)]
    res = [0] * 105

    road1 = RoadQueue(1)
    road2 = RoadQueue(2)
    road3 = RoadQueue(3)
    road4 = RoadQueue(4)

    dct = {
        1: road1,
        2: road2,
        3: road3,
        4: road4
    }

    regulator = Regulator(road1, road2, road3, road4, a, b, dct)

    for rover in rovers:
        rovers_by_time[rover.time] += [rover]

    for minute in range(1, 105):
        rovers_in_minute = rovers_by_time[minute]
        for rover in rovers_in_minute:
            dct[rover.direction].push_rover(rover)

        # TODO: регулировщик говорит, кто может поехать в эту минуту
        rovers_gone = regulator.get_rovers_gone()
        for rover in rovers_gone:
            if rover:
                res[rover.index] = minute

    return res


if __name__ == '__main__':
    n = int(input())
    a, b = map(int, input().split())
    Rover = namedtuple('Rover', ['time', 'direction', 'index'])
    rovers = []
    for i in range(n):
        direction_i, time_i = map(int, input().split())
        rovers.append(Rover(time=time_i, direction=direction_i, index=i))

    res = solution(rovers, a, b)
    for time in res:
        if time != 0:
            print(time)
