# Дятлы
from functools import reduce


K = 1


def myfact(n):
    if n < 2:
        return 1
    return reduce(lambda x, y: x * y % K, range(2, n+1))


class Node:

    def __init__(self, idx):
        self.idx = idx
        self.neighs: set[Node] = set()
        self.n_leaves = 0
        self.viewed = False

    @property
    def is_leaf(self):
        return len(self.neighs) == 1

    @property
    def permutations(self):
        return myfact(self.n_leaves)

    @property
    def additional_perm(self):
        return 2 if len(self.neighs) != 1 and len(self.neighs) != self.n_leaves else 1

    def __repr__(self):
        return f'({self.idx}, n_neighs={len(self.neighs)}, n_leaves={self.n_leaves})'


def check_correct_node(node: Node) -> bool:
    if len(node.neighs) > 2:
        return len(node.neighs) - node.n_leaves < 3
    return True


def create_edge(node1: Node, node2: Node):
    if node1.is_leaf:
        for neigh in node1.neighs:
            neigh.n_leaves -= 1
    if node2.is_leaf:
        for neigh in node2.neighs:
            neigh.n_leaves -= 1

    node1.neighs.add(node2)
    node2.neighs.add(node1)
    if node1.is_leaf:
        node2.n_leaves += 1
    if node2.is_leaf:
        node1.n_leaves += 1

class Graphs:

    def __init__(self, n):
        self.n = n
        self.nodes = {}

        self.n_subgraphs = 0
        self.perm = 1

    def add_edge(self, idx1, idx2):
        node1 = self.nodes.get(idx1, Node(idx1))
        self.nodes[idx1] = node1

        node2 = self.nodes.get(idx2, Node(idx2))
        self.nodes[idx2] = node2

        create_edge(node1, node2)

    def make_subgraph(self, node: Node):
        stack = [node]
        perm = 1
        nodes = 0
        edges = 0

        add_perm = 1
        while stack:
            cur = stack.pop()
            if cur.viewed:
                continue
            if not check_correct_node(cur):
                return 0

            # del self.nodes[cur.idx]
            cur.viewed = True
            nodes += 1
            edges += len(cur.neighs)
            perm = perm * cur.permutations % K
            add_perm = max(add_perm, cur.additional_perm)

            stack.extend(cur.neighs)

        edges //= 2
        if nodes != edges + 1:
            return 0

        return perm * add_perm * 2 % K

    def count_permutations(self):
        n_nodes = len(self.nodes)
        perm = 1
        for node in self.nodes.values():
            if node.viewed:
                continue
            sub_perm = self.make_subgraph(node)
            if sub_perm == 0:
                return 0
            perm = perm * sub_perm % K
            self.n_subgraphs += 1

        perm = perm * myfact(self.n_subgraphs) % K

        lonely = self.n - n_nodes
        perm_lonely = 1
        for i in range(n_nodes + 2, n_nodes + 2 + lonely):
            perm_lonely = perm_lonely * i % K

        return perm * perm_lonely % K


def main():
    global K
    n, m, K = map(int, input().split())
    graphs = Graphs(n)
    for _ in range(m):
        idx1, idx2 = map(int, input().split())
        graphs.add_edge(idx1, idx2)
    # print('asdfasf')

    # print(graphs.nodes)
    # print(graphs.subgraphs)
    print(graphs.count_permutations())


if __name__ == '__main__':
    main()
