class NaiveSnowmen:
    def __init__(self):
        self.snowmen = [[]]

    def add_snowman(self, t, m):
        if m == 0:
            new_stack = self.snowmen[t][:-1]
        else:
            new_stack = self.snowmen[t] + [m]
        self.snowmen.append(new_stack)

    @property
    def total_mass(self):
        return sum(sum(stack) for stack in self.snowmen)


if __name__ == '__main__':
    n = int(input())
    snowmen = NaiveSnowmen()
    for _ in range(n):
        t, m = map(int, input().split())
        snowmen.add_snowman(t, m)
    print(snowmen.total_mass)

