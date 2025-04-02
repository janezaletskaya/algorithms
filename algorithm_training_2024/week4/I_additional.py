# Пара путей


class Node:

    def __init__(self, idx):
        self.idx = idx
        self.neighs: set[Node] = set()

    @property
    def is_leaf(self):
        return len(self.neighs) == 1

    def __repr__(self):
        return f'{self.idx}, n_neighs={len(self.neighs)}'


class Tree:

    def __init__(self):
        self.nodes = {}
        self.edges: set[tuple[Node, Node]] = set()

    def add_edge(self, idx1, idx2):
        node1 = self.nodes.get(idx1, Node(idx1))
        node2 = self.nodes.get(idx2, Node(idx2))

        node1.neighs.add(node2)
        node2.neighs.add(node1)

        self.nodes[idx1] = node1
        self.nodes[idx2] = node2

        self.edges.add(tuple((node1, node2)))

    def max_two_paths(self):
        max_mul = 0
        for node1, node2 in self.edges:
            node1.neighs.remove(node2)
            node2.neighs.remove(node1)

            path1 = count_diameter(node1)
            path2 = count_diameter(node2)
            mul = path1 * path2
            max_mul = max(max_mul, mul)

            node1.neighs.add(node2)
            node2.neighs.add(node1)
        return max_mul

    def __repr__(self):
        return f'{self.edges}'


def count_diameter(node: Node):
    u, _ = dfs(node)
    v, diameter = dfs(u)
    return diameter


def dfs(node: Node) -> tuple[Node, int]:
    max_dist_tuple = (node, 0)

    stack = [(None, node, 0)]

    while stack:
        parent, cur, level = stack.pop()
        for neigh in cur.neighs:
            if neigh == parent:
                continue
            stack.append(tuple((cur, neigh, level + 1)))

        if cur.is_leaf:
            max_dist_tuple = max(max_dist_tuple, tuple((cur, level)), key=lambda x: x[1])

    return max_dist_tuple


def slow_solution(tree: Tree):
    return tree.max_two_paths()


def create_tree_from_console():
    n = int(input())
    tree = Tree()
    for _ in range(n - 1):
        idx1, idx2 = map(int, input().split())
        tree.add_edge(idx1, idx2)
    return tree


def main():
    tree = create_tree_from_console()
    print(slow_solution(tree))


if __name__ == '__main__':
    main()
