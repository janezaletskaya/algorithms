# I. Снеговики
class Snowmen:

    def __init__(self):
        self.snowmen = [0]
        self.prev = [-1]

    def add_snowman(self, from_, m):
        if m == 0:
            from_ = self.prev[from_]
            new_snowman = self.snowmen[from_]
            from_ = self.prev[from_]
        else:
            new_snowman = self.snowmen[from_] + m

        self.snowmen.append(new_snowman)
        self.prev.append(from_)

    @property
    def total_mass(self):
        return sum(self.snowmen)

    def __repr__(self):
        return self.snowmen.__repr__()


if __name__ == '__main__':
    n = int(input())
    snowmen = Snowmen()
    for _ in range(n):
        from_, m = map(int, input().split())
        snowmen.add_snowman(from_, m)

    print(snowmen.total_mass)
