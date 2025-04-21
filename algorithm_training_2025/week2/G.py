# G. Нолики
from collections import deque


class Node:
    def __init__(self, left_node=None, right_node=None, left_idx=None, right_idx=None):
        self.left_node = left_node
        self.right_node = right_node

        self.left_idx = left_idx
        self.right_idx = right_idx

        self.max_len = 0
        self.prefix = 0
        self.suffix = 0
        self.is_all_zeroes = False


def make_segment_tree(array: list[int]):
    queue = deque()

    n = 1
    while n < len(array):
        n *= 2

    array = array + [-1] * (n - len(array))

    for i, elem in enumerate(array):
        node = Node(left_idx=i, right_idx=i)
        if elem == 0:
            node.max_len = 1
            node.prefix = 1
            node.suffix = 1
            node.is_all_zeroes = True

        queue.append(node)

    while len(queue) > 1:
        left_node, right_node = queue.popleft(), queue.popleft()
        node = Node(left_node, right_node)
        node.left_idx, node.right_idx = left_node.left_idx, right_node.right_idx

        if left_node.is_all_zeroes and right_node.is_all_zeroes:
            left_suffix_right_prefix = left_node.max_len + right_node.max_len
        elif left_node.is_all_zeroes:
            left_suffix_right_prefix = left_node.max_len + right_node.prefix
        elif right_node.is_all_zeroes:
            left_suffix_right_prefix = left_node.suffix + right_node.max_len
        else:
            left_suffix_right_prefix = left_node.suffix + right_node.prefix

        node.max_len = max(left_node.max_len, right_node.max_len, left_suffix_right_prefix)

        if left_node.is_all_zeroes:
            node.prefix = left_node.max_len + right_node.prefix
        else:
            node.prefix = left_node.prefix

        if right_node.is_all_zeroes:
            node.suffix = left_node.suffix + right_node.max_len
        else:
            node.suffix = right_node.suffix

        node.is_all_zeroes = left_node.is_all_zeroes and right_node.is_all_zeroes

        queue.append(node)

    root = queue[0]

    return root


def change_element(idx: int, new_val: int, root: Node):
    def change_node(node: Node):
        if node.left_idx == node.right_idx == idx:
            node.max_len = 1 if new_val == 0 else 0
            node.prefix = 1 if new_val == 0 else 0
            node.suffix = 1 if new_val == 0 else 0
            node.is_all_zeroes = new_val == 0
            return

        mid = (node.left_idx + node.right_idx) // 2

        if idx <= mid:
            change_node(node.left_node)
        else:
            change_node(node.right_node)

        left_node = node.left_node
        right_node = node.right_node

        if left_node.is_all_zeroes and right_node.is_all_zeroes:
            left_suffix_right_prefix = left_node.max_len + right_node.max_len
        elif left_node.is_all_zeroes:
            left_suffix_right_prefix = left_node.max_len + right_node.prefix
        elif right_node.is_all_zeroes:
            left_suffix_right_prefix = left_node.suffix + right_node.max_len
        else:
            left_suffix_right_prefix = left_node.suffix + right_node.prefix

        node.max_len = max(left_node.max_len, right_node.max_len, left_suffix_right_prefix)

        if left_node.is_all_zeroes:
            node.prefix = left_node.max_len + right_node.prefix
        else:
            node.prefix = left_node.prefix

        if right_node.is_all_zeroes:
            node.suffix = left_node.suffix + right_node.max_len
        else:
            node.suffix = right_node.suffix

        node.is_all_zeroes = left_node.is_all_zeroes and right_node.is_all_zeroes

    change_node(root)


def find_max_len_zeroes(root: Node, left: int, right: int):
    def execute_query(node, l, r):
        if l <= node.left_idx and node.right_idx <= r:
            return node.max_len, node.prefix, node.suffix, node.is_all_zeroes

        if node.right_idx < l or r < node.left_idx:
            return 0, 0, 0, True

        left_max_len, left_prefix, left_suffix, left_all_zeroes = execute_query(node.left_node, l, r)
        right_max_len, right_prefix, right_suffix, right_all_zeroes = execute_query(node.right_node, l, r)

        if left_all_zeroes and right_all_zeroes:
            mid_max_len = left_max_len + right_max_len
        elif left_all_zeroes:
            mid_max_len = left_max_len + right_prefix
        elif right_all_zeroes:
            mid_max_len = left_suffix + right_max_len
        else:
            mid_max_len = left_suffix + right_prefix

        max_len = max(left_max_len, right_max_len, mid_max_len)

        if left_all_zeroes:
            prefix = left_max_len + right_prefix
        else:
            prefix = left_prefix

        if right_all_zeroes:
            suffix = left_suffix + right_max_len
        else:
            suffix = right_suffix

        is_all_zeroes = left_all_zeroes and right_all_zeroes

        return max_len, prefix, suffix, is_all_zeroes

    max_len, _, _, _ = execute_query(root, left, right)

    return max_len


if __name__ == '__main__':
    input()
    arr = list(map(int, input().split()))
    st_root = make_segment_tree(arr)

    m = int(input())
    for _ in range(m):
        query_type, first, second = input().split()
        if query_type == 'UPDATE':
            idx, value = int(first) - 1, int(second)
            change_element(idx, value, st_root)
        elif query_type == 'QUERY':
            left, right = int(first) - 1, int(second) - 1
            print(find_max_len_zeroes(st_root, left, right))
