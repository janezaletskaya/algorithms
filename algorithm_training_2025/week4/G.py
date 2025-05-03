# G. Острова
import sys
sys.setrecursionlimit(1000000)


class BridgeMap:

    def __init__(self, n_islands):
        self.prevs = [i for i in range(n_islands)]
        self.depths = [0 for _ in range(n_islands)]
        self.n_sets = n_islands

    def add_bridge(self, island1, island2):
        island1_root = self.find_root(island1)
        island2_root = self.find_root(island2)

        if island1_root == island2_root:
            return self.n_sets == 1

        if self.depths[island1_root] < self.depths[island2_root]:
            self.prevs[island1_root] = island2_root
        elif self.depths[island1_root] > self.depths[island2_root]:
            self.prevs[island2_root] = island1_root
        else:
            self.prevs[island2_root] = island1_root
            self.depths[island1_root] += 1

        self.n_sets -= 1

        return self.n_sets == 1

    def find_root(self, island):
        if self.prevs[island] == island:
            return self.prevs[island]

        self.prevs[island] = self.find_root(self.prevs[island])
        return self.prevs[island]


if __name__ == '__main__':
    n, m = map(int, input().split())
    bm = BridgeMap(n_islands=n)

    for i in range(1, m + 1):
        island1, island2 = map(int, input().split())
        if bm.add_bridge(island1 - 1, island2 - 1):
            print(i)
            break

