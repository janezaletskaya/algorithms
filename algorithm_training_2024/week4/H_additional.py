# Вершинно-реберное покрытие дерева
class Node:

    def __init__(self, idx, price=None):
        self.idx = idx
        self.price = price
        self.neighs: list[Node] = list()

    @property
    def is_leaf(self):
        return len(self.neighs) == 1


class Tree:

    def __init__(self, n=None):
        self.n = n
        self.nodes: list[Node] = [None] * (n + 1)
        for i in range(0, n+1):
            self.nodes[i] = Node(i)

    def add_edge(self, idx1, idx2):
        node1 = self.nodes[idx1]
        node2 = self.nodes[idx2]

        node1.neighs.append(node2)
        node2.neighs.append(node1)

    def add_prices(self, price_list):
        for idx, price in enumerate(price_list, start=1):
            self.nodes[idx].price = price


def dfs1(n, node: Node) -> list[list[int]]:
    dp = [[0, 0] for _ in range(n+1)]

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


def dfs2(n, node: Node, dp: list[list[int]]) -> tuple[list[int], int]:
    dp2 = [True for _ in range(n+1)]
    res = []
    cost = 0

    stack: list[tuple[Node, Node]] = [(Node(0), node)]

    while stack:
        parent, cur = stack.pop()
        for neigh in cur.neighs:
            if neigh == parent:
                continue
            stack.append(tuple((cur, neigh)))

        if dp2[parent.idx]:
            include = 0 if dp[cur.idx][0] < dp[cur.idx][1] else 1
            dp2[cur.idx] = bool(include)
            if include:
                cost += cur.price
                res.append(cur.idx)
        else:
            dp2[cur.idx] = True
            cost += cur.price
            res.append(cur.idx)

    return res, cost


def create_tree_from_console():
    n = int(input())
    tree = Tree(n)
    for _ in range(n - 1):
        idx1, idx2 = map(int, input().split())
        tree.add_edge(idx1, idx2)
    price_list = list(map(int, input().split()))
    tree.add_prices(price_list)
    return tree


def solution(tree):
    if tree.n == 1:
        return tree.nodes[1].price, [1]
    dp = dfs1(tree.n, tree.nodes[1])
    nodes, cost = dfs2(tree.n, tree.nodes[1], dp)

    return cost, nodes


def main():
    tree = create_tree_from_console()
    cost, nodes = solution(tree)
    print(cost, len(nodes))
    print(*nodes)


if __name__ == '__main__':
    main()
