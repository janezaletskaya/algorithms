# H. Дерево отрезков с операцией на отрезке
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

    array = array + [-1] * (n - len(array))

    for i, elem in enumerate(array):
        node = Node(val=elem, left_idx=i, right_idx=i)
        queue.append(node)

    while len(queue) > 1:
        left_node, right_node = queue.popleft(), queue.popleft()
        node = Node(
            val=None,
            left_node=left_node,
            right_node=right_node,
            left_idx=left_node.left_idx,
            right_idx=right_node.right_idx
        )

        queue.append(node)

    root = queue[0]

    return root


def find_element(root, idx):
    def find_and_update(node, update_val):
        total_update = update_val + node.update_value

        if node.left_idx == node.right_idx == idx:
            node.val += total_update
            node.update_value = 0
            return node.val

        if node.update_value != 0:
            node.left_node.update_value += node.update_value
            node.right_node.update_value += node.update_value
            node.update_value = 0

        mid = (node.left_idx + node.right_idx) // 2

        if idx <= mid:
            return find_and_update(node.left_node, 0)
        else:
            return find_and_update(node.right_node, 0)

    return find_and_update(root, 0)


def update_segment(root, left, right, update):
    def update_range(node, l, r, add_val):
        if node.right_idx < l or node.left_idx > r:
            return

        if l <= node.left_idx and node.right_idx <= r:
            node.update_value += add_val
            return

        if node.update_value != 0:
            node.left_node.update_value += node.update_value
            node.right_node.update_value += node.update_value
            node.update_value = 0

        update_range(node.left_node, l, r, add_val)
        update_range(node.right_node, l, r, add_val)

    update_range(root, left, right, update)


if __name__ == '__main__':
    input()
    arr = list(map(int, input().split()))
    st_root = make_segment_tree(arr)

    m = int(input())
    for _ in range(m):
        query_list = input().split()
        if query_list[0] == 'g':
            print(find_element(st_root, int(query_list[1]) - 1))
        elif query_list[0] == 'a':
            l, r, addition = map(int, query_list[1:])
            update_segment(st_root, l - 1, r - 1, addition)
