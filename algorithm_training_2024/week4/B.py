# Родословная: число потомков

import sys

sys.setrecursionlimit(100000)


class Node:

    def __init__(self, name):
        self.name = name
        self.children = set()

    def __repr__(self):
        return f'{self.name}: {self.children}'


family = {}
children_set = set()


def add_to_family(child, parent):
    global children_set
    children_set.add(child)

    node_parent = family.get(parent, Node(parent))
    node_child = family.get(child, Node(child))
    node_parent.children.add(node_child)
    family[parent] = node_parent
    family[child] = node_child


def children_count_by_node(root):
    res = []

    def dfs(node):
        if node is None:
            return 0

        children_count = 0
        for child in node.children:
            children_count += dfs(child)

        res.append((node.name, children_count))

        return children_count + 1

    dfs(root)

    return res


if __name__ == '__main__':
    n = int(input())
    for _ in range(n - 1):
        child, parent = input().split()
        add_to_family(child, parent)

    root_name = list(set(family.keys()) - children_set)[0]
    root = family[root_name]
    names_children_counts = children_count_by_node(root)

    for name, counts in sorted(names_children_counts):
        print(name, counts)



