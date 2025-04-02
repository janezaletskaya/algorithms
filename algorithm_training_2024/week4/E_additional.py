# Размер поддеревьев
import sys

sys.setrecursionlimit(100000)


class Node:
    def __init__(self, name):
        self.name = name
        self.neighs = set()

    def __repr__(self):
        return f"{self.name}: {self.neighs}"


def add_to_tree(id1, id2):
    node1 = tree.get(id1, Node(id1))
    node2 = tree.get(id2, Node(id2))

    node1.neighs.add(node2.name)
    node2.neighs.add(node1.name)

    tree[id1] = node1
    tree[id2] = node2


def descendants_count_by_node(root, n):
    descendants_by_node = [0] * (n + 1)

    def dfs(node_name, parent_name):
        descendants_by_node[node_name] = 1
        node = tree[node_name]
        for neigh_name in node.neighs:
            if neigh_name != parent_name:
                dfs(neigh_name, node_name)
                descendants_by_node[node_name] += descendants_by_node[neigh_name]

    dfs(root.name, -1)
    return descendants_by_node


if __name__ == "__main__":
    n = int(input())

    tree = {}
    for _ in range(n - 1):
        id1, id2 = map(int, input().split())
        add_to_tree(id1, id2)

    root = tree[1]
    subtree_size = descendants_count_by_node(root, n)
    print(" ".join(map(str, subtree_size[1:])))

