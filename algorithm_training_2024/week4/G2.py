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


class Graph:

    def __init__(self):
        self.nodes: set[int] = set()
        self.n_edges = 0

    def permutations(self, nodes: dict[int, Node]) -> int:
        permutations = 1
        add_permutations = 1
        for nodeidx in self.nodes:
            node = nodes[nodeidx]
            if not check_correct_node(node):
                return 0
            permutations = permutations * node.permutations % K
            add_permutations = max(add_permutations, node.additional_perm)

        return 2 * add_permutations * permutations % K

    def add_edge(self, idx1, idx2):
        self.n_edges += 1
        self.nodes.add(idx1)
        self.nodes.add(idx2)

    def merge(self, other: 'Graph'):
        self.nodes.update(other.nodes)
        self.n_edges += other.n_edges + 1

    def __repr__(self):
        return f'({self.nodes}, {self.n_edges})'


class Graphs:

    def __init__(self, n):
        self.n = n
        self.nodes = {}
        self.subgraphs: dict[int, Graph] = {}
        self.last_subgraph_idx = 0

    def _create_subgraph(self, idx1, idx2):
        graph = Graph()
        self.subgraphs[self.last_subgraph_idx] = graph
        self.last_subgraph_idx += 1
        graph.add_edge(idx1, idx2)
        return graph

    def add_edge(self, idx1, idx2):
        node1 = self.nodes.get(idx1, Node(idx1))
        self.nodes[idx1] = node1

        node2 = self.nodes.get(idx2, Node(idx2))
        self.nodes[idx2] = node2

        create_edge(node1, node2)

        sub1 = None
        sub2 = None
        for subidx, subgraph in self.subgraphs.items():
            if idx1 in subgraph.nodes and idx2 in subgraph.nodes:
                return False

            if idx1 in subgraph.nodes:
                sub1 = subidx
                continue

            if idx2 in subgraph.nodes:
                sub2 = subidx
                continue

        if sub1 == sub2:
            self._create_subgraph(idx1, idx2)
        elif sub1 is not None and sub2 is not None:
            self.subgraphs[sub1].merge(self.subgraphs[sub2])
            del self.subgraphs[sub2]
        elif sub1 is not None:
            self.subgraphs[sub1].add_edge(idx1, idx2)
        elif sub2 is not None:
            self.subgraphs[sub2].add_edge(idx1, idx2)

        return True

    def count_permutations(self):
        permutations = 1
        for subgraph in self.subgraphs.values():
            subgraph_permutations = subgraph.permutations(self.nodes)
            if subgraph_permutations == 0:
                return 0
            permutations = permutations * subgraph_permutations % K

        permutations = permutations * myfact(len(self.subgraphs)) % K

        lonely = self.n - len(self.nodes)

        perm_lonely = 1
        for i in range(len(self.nodes) + 2, len(self.nodes) + 2 + lonely):
            perm_lonely = perm_lonely * i % K

        return permutations * perm_lonely % K


def main():
    global K
    n, m, K = map(int, input().split())
    graphs = Graphs(n)
    for _ in range(m):
        idx1, idx2 = map(int, input().split())
        if not graphs.add_edge(idx1, idx2):
            print(0)
            return
    # print('asdfasf')

    # print(graphs.nodes)
    # print(graphs.subgraphs)
    print(graphs.count_permutations())


if __name__ == '__main__':
    main()
