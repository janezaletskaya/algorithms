# Родословная: подсчет уровней

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


def levels_by_node(root):
    res = []

    def dfs(node, level):
        if node is None:
            return

        res.append((node.name, level))

        for child in node.children:
            dfs(child, level + 1)

    dfs(root, 0)

    return res


if __name__ == '__main__':
    n = int(input())
    for _ in range(n - 1):
        child, parent = input().split()
        add_to_family(child, parent)

    root_name = list(set(family.keys()) - children_set)[0]
    root = family[root_name]
    names_heights = levels_by_node(root)

    for name, level in sorted(names_heights):
        print(name, level)



