# Размер поддеревьев
import sys


sys.setrecursionlimit(100000)


class Node:

    def __init__(self, name):
        self.name = name
        self.neighs = set()

    def __repr__(self):
        return f'{self.name}: {self.neighs}'


tree = {1: Node(1)}


def add_to_tree(id1, id2):
    node1 = tree.get(id1, Node(id1))
    node2 = tree.get(id2, Node(id2))

    node1.neighs.add(node2)
    node2.neighs.add(node1)

    tree[id1] = node1
    tree[id2] = node2


def children_count_by_node(root):
    res = []

    def dfs(node):
        if node is None:
            return 0

        neighs_count = 0
        for neigh in node.neighs:
            neighs_count += dfs(neigh)

        res.append((node.name, neighs_count))

        return neighs_count + 1

    dfs(root)

    return res


if __name__ == '__main__':
    n = int(input())
    for _ in range(n - 1):
        parent, child = map(int, input().split())
        add_to_tree(parent, child)

    root = tree[1]
    names_children_counts = children_count_by_node(root)

    for name, counts in sorted(names_children_counts):
        print(name, counts + 1)


