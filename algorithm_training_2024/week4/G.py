# Дятлы
import math
import sys

sys.setrecursionlimit(300000)


class Node:

    def __init__(self, idx):
        self.idx = idx
        self.neighs = set()
        self.viewed = False
        self.leaf_neighs = None

    @property
    def permutations(self):
        leaf_neighs = 0
        for neigh in self.neighs:
            if len(neigh.neighs) == 1:
                leaf_neighs += 1

        self.leaf_neighs = leaf_neighs
        return math.factorial(leaf_neighs)

    def __repr__(self):
        return f'{self.idx, self.viewed}, n_neighs={len(self.neighs)}'


class Graphs:

    def __init__(self):
        self.nodes = {}
        self.edges = set()
        self.subgraphs = {}
        self.last_subgraph_idx = 0
        self.node_in_pairs = 0

    def add_edge(self, idx1, idx2):
        node1 = self.nodes.get(idx1, Node(idx1))
        node2 = self.nodes.get(idx2, Node(idx2))

        node1.neighs.add(node2)
        node2.neighs.add(node1)

        self.nodes[idx1] = node1
        self.nodes[idx2] = node2

        self.edges.add(tuple((node1, node2)))

    def make_dict_subgraphs(self):
        for node in self.nodes.values():
            if len(node.neighs) > 2:
                count_non_leafs = 0
                for neigh in node.neighs:
                    if len(neigh.neighs) > 1:
                        count_non_leafs += 1
                        if count_non_leafs > 2:
                            raise Exception('WTF???')

            if not node.viewed:
                self.subgraphs[self.last_subgraph_idx] = [0, 0, 1, 1]
                self._traversal_subgraph(node, None)
                self.subgraphs[self.last_subgraph_idx][1] //= 2
                nodes, edges, _, _ = self.subgraphs[self.last_subgraph_idx]
                if nodes != edges + 1:
                    raise Exception("is not a tree")
                self.last_subgraph_idx += 1

    def _traversal_subgraph(self, node, parent):
        if node.viewed:
            return

        node.viewed = True
        self.subgraphs[self.last_subgraph_idx][0] += 1
        self.subgraphs[self.last_subgraph_idx][1] += len(node.neighs)
        self.subgraphs[self.last_subgraph_idx][2] *= node.permutations

        if len(node.neighs) != 1 and len(node.neighs) != node.leaf_neighs:
            self.subgraphs[self.last_subgraph_idx][3] = 2

        for neigh in node.neighs:
            if neigh == parent:
                continue
            self._traversal_subgraph(neigh, node)

    def count_permutations(self, k, n):
        perm_subgraphs = math.factorial(len(self.subgraphs))
        perm_in_subgraphs = 1
        for _, lst in self.subgraphs.items():
            self.node_in_pairs += lst[0]
            perm_in_subgraphs *= 2
            perm_in_subgraphs *= lst[2]
            perm_in_subgraphs *= lst[3]

        perm_lonely = 1
        self.lonely = n - self.node_in_pairs
        for i in range(self.node_in_pairs + 2, self.node_in_pairs + 2 + self.lonely):
            perm_lonely *= i

        return (perm_subgraphs * perm_in_subgraphs * perm_lonely) % k


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    graphs = Graphs()
    for _ in range(m):
        idx1, idx2 = map(int, input().split())
        graphs.add_edge(idx1, idx2)

    try:
        graphs.make_dict_subgraphs()
        print(graphs.count_permutations(k, n))
    except Exception as e:
        print(0)


