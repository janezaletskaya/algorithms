# Пара путей

class Node:

    def __init__(self, idx):
        self.idx = idx
        self.neighs: list[Node] = list()

    def __repr__(self):
        return f'{self.idx}, n_neighs={len(self.neighs)}'


class Tree:

    def __init__(self, n):
        self.n = n
        self.nodes: list[Node] = [Node(i) for i in range(0, n+1)]

    def add_edge(self, idx1, idx2):
        node1 = self.nodes[idx1]
        node2 = self.nodes[idx2]

        node1.neighs.append(node2)
        node2.neighs.append(node1)


def rem(a, b, c, new, out):
    if a == out:
        return max3(b, c, 0, new)
    if b == out:
        return max3(a, c, 0, new)
    if c == out:
        return max3(a, b, 0, new)
    return max3(a, b, c, new)


def max3(a, b, c, new):
    if new >= a:
        return new, a, b
    if new >= b:
        return a, new, b
    if new >= c:
        return a, b, new

    return a, b, c


def dfs1(n, root: Node) -> list[list[int]]:
    dp = [[0, 0, 0] for _ in range(n+1)]

    stack: list[tuple[Node, Node, bool]] = [(None, root, False)]

    while stack:
        parent, cur, processed = stack.pop()

        if processed:
            a, b, c = 0, 0, 0
            for neigh in cur.neighs:
                if neigh == parent:
                    continue
                new = dp[neigh.idx][0] + 1
                a, b, c = max3(a, b, c, new)

            dp[cur.idx][0] = a
            dp[cur.idx][1] = b
            dp[cur.idx][2] = c

        else:
            stack.append((parent, cur, True))
            for neigh in cur.neighs:
                if neigh == parent:
                    continue
                stack.append(tuple((cur, neigh, False)))

    return dp


def dfs2(n, root, dp: list[list[int]]):
    fakeNode = Node(0)
    max_mul = 0
    stack: list[tuple[Node, Node, Node, bool, list[int] | None]] = [(fakeNode, fakeNode, root, False, None)]

    while stack:
        prev, parent, cur, after_children, state = stack.pop()
        p_stat = dp[parent.idx]
        if after_children:
            print('up')
            print(prev.idx, parent.idx, cur.idx)
            print(dp[1:])
            dp[parent.idx] = state
            print(dp[1:])

        else:
            print('down')
            print(prev.idx, parent.idx, cur.idx)
            print(dp[1:])

            stack.append(tuple((prev, parent, cur, True, p_stat[:])))
            new = dp[prev.idx][0] + 1
            if prev.idx == 0:
                new = 0
            old = dp[cur.idx][0] + 1
            p_stat[0], p_stat[1], p_stat[2] = rem(p_stat[0], p_stat[1], p_stat[2], new, old)
            mul = (dp[cur.idx][0] + dp[cur.idx][1]) * (p_stat[0] + p_stat[1])
            max_mul = max(max_mul, mul)
            print('after')
            print(dp[1:])

            for neigh in cur.neighs:
                if neigh == parent:
                    continue
                stack.append(tuple((parent, cur, neigh, False, None)))


    return max_mul


def fast_solution(tree: Tree):
    print('start')
    dp = dfs1(tree.n, tree.nodes[1])
    ans = dfs2(tree.n, tree.nodes[1], dp)
    print('end')
    return ans


def create_tree_from_console():
    n = int(input())
    tree = Tree(n)
    for _ in range(n - 1):
        idx1, idx2 = map(int, input().split())
        tree.add_edge(idx1, idx2)
    return tree


if __name__ == '__main__':
    tree = create_tree_from_console()
    print(fast_solution(tree))


