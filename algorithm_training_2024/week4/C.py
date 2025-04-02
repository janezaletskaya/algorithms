# Родословная: LCA

import sys

sys.setrecursionlimit(100000)


class Node:

    def __init__(self, name, parent=None, height=None):
        self.name = name
        self.parent = parent
        self.children = set()
        self.height = height

    def __repr__(self):
        return f'height={self.height}, {self.name}: {self.children}'


family = {}
children_set = set()


def add_to_family(child, parent):
    global children_set
    children_set.add(child)

    node_parent = family.get(parent, Node(parent))
    node_child = family.get(child, Node(child))

    node_child.parent = node_parent
    node_parent.children.add(node_child)

    family[parent] = node_parent
    family[child] = node_child


def levels_by_node(root):
    res = []

    def dfs(node, level):
        if node is None:
            return

        node.height = level

        for child in node.children:
            dfs(child, level + 1)

    dfs(root, 0)

    return res


def family_LCA(name1, name2):
    node1 = family[name1]
    node2 = family[name2]

    while node1.height > node2.height:
        node1 = node1.parent

    while node2.height > node1.height:
        node2 = node2.parent

    while node1.name != node2.name:
        node1 = node1.parent
        node2 = node2.parent

    return node1.name


if __name__ == '__main__':
    n = int(input())
    for _ in range(n - 1):
        child, parent = input().split()
        add_to_family(child, parent)

    root_name = list(set(family.keys()) - children_set)[0]
    root = family[root_name]
    levels_by_node(root)
    requests = sys.stdin.read().split('\n')

    for request in requests:
        if request:
            name1, name2 = request.split()
            print(family_LCA(name1, name2))
