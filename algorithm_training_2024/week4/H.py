# Вершинно-реберное покрытие дерева

from memory_profiler import memory_usage
from collections import defaultdict


class Node:

    def __init__(self, idx, price=None):
        self.idx = idx
        self.price = price
        self.neighs: list[Node] = list()

        self.flag = False

    @property
    def is_leaf(self):
        return len(self.neighs) == 1

    def __repr__(self):
        return f'{self.idx, self.price, self.flag}, n_neighs={len(self.neighs)}'


class Tree:

    def __init__(self):
        self.nodes = {}

    def add_edge(self, idx1, idx2):
        node1 = self.nodes.get(idx1, Node(idx1))
        self.nodes[idx1] = node1

        node2 = self.nodes.get(idx2, Node(idx2))
        self.nodes[idx2] = node2

        node1.neighs.append(node2)
        node2.neighs.append(node1)

    def add_prices(self, price_list):
        for idx, price in enumerate(price_list, start=1):
            self.nodes[idx].price = price


def dfs1(node: Node) -> dict[int, dict[int, int]]:
    dp = defaultdict(dict)

    stack: list[tuple[Node, Node, bool]] = [(None, node, False)]

    while stack:
        parent, cur, processed = stack.pop()

        if processed:
            sum0 = 0
            sum1 = 0
            for neigh in cur.neighs:
                if neigh == parent:
                    continue
                sum0 += dp[neigh.idx][1]
                sum1 += min(dp[neigh.idx][0], dp[neigh.idx][1])

            dp[cur.idx][0] = sum0
            dp[cur.idx][1] = sum1 + cur.price

        else:
            stack.append((parent, cur, True))
            for neigh in cur.neighs:
                if neigh == parent:
                    continue
                stack.append(tuple((cur, neigh, False)))

    return dp


def dfs2(node: Node, dp: dict[int, dict[int, int]]) -> tuple[list[int], int]:
    dp2 = {-1: True}
    res = list()
    cost = 0

    stack: list[tuple[Node, Node]] = [(Node(-1), node)]

    while stack:
        parent, cur = stack.pop()
        for neigh in cur.neighs:
            if neigh == parent:
                continue
            stack.append(tuple((cur, neigh)))

        if dp2[parent.idx]:
            include, _ = min(dp[cur.idx].items(), key= lambda x: x[1])
            dp2[cur.idx] = bool(include)
            if include:
                cost += cur.price
                res.append(cur.idx)
        else:
            dp2[cur.idx] = True
            cost += cur.price
            res.append(cur.idx)

    return res, cost


def solution():
    n = int(input())
    if n == 1:
        price = int(input())
        return price, [n]

    tree = Tree()
    for _ in range(n - 1):
        idx1, idx2 = map(int, input().split())
        tree.add_edge(idx1, idx2)
    price_list = list(map(int, input().split()))
    tree.add_prices(price_list)
    dp = dfs1(tree.nodes[1])
    nodes, cost = dfs2(tree.nodes[1], dp)

    return cost, nodes


if __name__ == '__main__':
    cost, nodes = solution()
    print(cost, len(nodes))
    print(*nodes)
    print(memory_usage())

