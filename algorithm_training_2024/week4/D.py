# Бинарное дерево (вставка, поиск, обход)
import sys


class Node:

    def __init__(self, value=None, left=None, right=None, parent=None, height=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.height = height

    def __repr__(self):
        return f"{self.value}: l{self.left}, r{self.right}"


class Tree:

    def __init__(self):
        self.root: Node = None
        self.height = 0

    def add(self, x):
        if not self.root:
            self.root = Node(value=x, height=1)
            self.height = 1
            return 'DONE'

        cur_node = self.root
        cur_height = 1
        prev_node = None
        while cur_node:
            prev_node = cur_node
            if x == cur_node.value:
                return 'ALREADY'
            if x > cur_node.value:
                cur_node = cur_node.right
                cur_height += 1
            else:
                cur_node = cur_node.left
                cur_height += 1

        if x > prev_node.value:
            prev_node.right = Node(value=x, height=cur_height, parent=prev_node)
        else:
            prev_node.left = Node(value=x, height=cur_height, parent=prev_node)

        self.height = max(self.height, cur_height)

        return 'DONE'

    def find(self, x):
        cur_node = self.root
        while cur_node:
            if x == cur_node.value:
                return 'YES'
            if x > cur_node.value:
                cur_node = cur_node.right
            else:
                cur_node = cur_node.left

        return 'NO'

    def print_tree(self, cur_node):
        if cur_node is None:
            return

        self.print_tree(cur_node.left)
        print(('.' * (cur_node.height - 1)) + str(cur_node.value))
        self.print_tree(cur_node.right)


func_dict = {'ADD': Tree.add, 'SEARCH': Tree.find, 'PRINTTREE': Tree.print_tree}
my_tree = Tree()

text = sys.stdin.read().split('\n')

for elem in text:
    if not elem:
        continue
    if elem == 'PRINTTREE':
        func_dict[elem](my_tree, my_tree.root)

    else:
        command, number = elem.split()
        print(func_dict[command](my_tree, int(number)))




