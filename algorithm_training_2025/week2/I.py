# I. Максимум на подотрезках с добавлением на отрезке
from collections import deque


class Node:
    def __init__(self, val, left_node=None, right_node=None, left_idx=None, right_idx=None):
        self.val = val
        self.left_node = left_node
        self.right_node = right_node
        self.left_idx = left_idx
        self.right_idx = right_idx
        self.update_value = 0


def make_segment_tree(array: list[int]):
    queue = deque()

    n = 1
    while n < len(array):
        n *= 2

    array = array + [float('-inf')] * (n - len(array))

    for i, elem in enumerate(array):
        node = Node(val=elem, left_idx=i, right_idx=i)
        queue.append(node)

    while len(queue) > 1:
        left_node, right_node = queue.popleft(), queue.popleft()
        node = Node(
            val=max(left_node.val, right_node.val),
            left_node=left_node,
            right_node=right_node,
            left_idx=left_node.left_idx,
            right_idx=right_node.right_idx
        )
        queue.append(node)

    root = queue[0]
    return root


def push_down_addition(node):
    if node.update_value != 0:
        if node.left_node:
            node.left_node.update_value += node.update_value
            node.left_node.val += node.update_value
        if node.right_node:
            node.right_node.update_value += node.update_value
            node.right_node.val += node.update_value
        node.update_value = 0


def update_segment(root, left, right, update):
    def update_range(node, l, r, add_val):
        if node.right_idx < l or node.left_idx > r:
            return

        if l <= node.left_idx and node.right_idx <= r:
            node.val += add_val
            node.update_value += add_val
            return

        push_down_addition(node)
        update_range(node.left_node, l, r, add_val)
        update_range(node.right_node, l, r, add_val)

        node.val = max(node.left_node.val, node.right_node.val)

    update_range(root, left, right, update)


def find_max_on_segment(root, left, right):
    def query_max(node, l, r):
        if node.right_idx < l or node.left_idx > r:
            return float('-inf')

        if l <= node.left_idx and node.right_idx <= r:
            return node.val

        push_down_addition(node)

        left_max = query_max(node.left_node, l, r)
        right_max = query_max(node.right_node, l, r)

        return max(left_max, right_max)

    return query_max(root, left, right)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    st_root = make_segment_tree(arr)

    m = int(input())
    for _ in range(m):
        query_list = input().split()
        if query_list[0] == 'm':
            l, r = map(int, query_list[1:])
            print(find_max_on_segment(st_root, l - 1, r - 1), end=' ')
        elif query_list[0] == 'a':
            l, r, addition = map(int, query_list[1:])
            update_segment(st_root, l - 1, r - 1, addition)
