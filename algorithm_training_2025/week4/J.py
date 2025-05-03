# J. Простая река
class Node:

    def __init__(self, len_, left=None, right=None):
        self.len_ = len_
        self.left = left
        self.right = right


class DoublyLinkedList:

    def __init__(self, companies):
        self.head, self.sum_ = self._make_linked_list(companies)
        self.ptr = self.head
        self.ptr_idx = 1

    def bankruptcy(self, idx):
        self._find_node(idx)
        node = self.ptr
        left_neigh = node.left
        right_neigh = node.right
        if left_neigh and right_neigh:
            left_part, right_part = self.split_segment(node)
            self.sum_ -= (node.len_ ** 2 + left_neigh.len_ ** 2 + right_neigh.len_ ** 2)
            left_neigh.len_ += left_part
            right_neigh.len_ += right_part
            self.sum_ += left_neigh.len_ ** 2 + right_neigh.len_ ** 2
            left_neigh.right = right_neigh
            right_neigh.left = left_neigh
            self.ptr = left_neigh
            self.ptr_idx = idx - 1

        elif left_neigh and not right_neigh:
            self.sum_ -= (node.len_ ** 2 + left_neigh.len_ ** 2)
            left_neigh.len_ += node.len_
            self.sum_ += left_neigh.len_ ** 2
            left_neigh.right = None
            self.ptr = left_neigh
            self.ptr_idx = idx - 1

        elif right_neigh and not left_neigh:
            self.sum_ -= (node.len_ ** 2 + right_neigh.len_ ** 2)
            right_neigh.len_ += node.len_
            self.sum_ += right_neigh.len_ ** 2
            right_neigh.left = None
            self.ptr = right_neigh
            self.ptr_idx = idx

        return self.sum_

    def division(self, idx):
        self._find_node(idx)
        node = self.ptr
        new_left_len, new_right_len = self.split_segment(node)
        new_left_node, new_right_node = Node(new_left_len), Node(new_right_len)
        new_left_node.left, new_left_node.right = node.left, new_right_node
        new_right_node.left, new_right_node.right = new_left_node, node.right

        if node.left:
            node.left.right = new_left_node
        if node.right:
            node.right.left = new_right_node

        self.sum_ -= node.len_ ** 2
        self.sum_ += new_left_node.len_ ** 2 + new_right_node.len_ ** 2

        self.ptr = new_left_node
        self.ptr_idx = idx

        return self.sum_

    def _find_node(self, idx):
        if idx == self.ptr_idx:
            return

        cur_node = self.ptr
        if idx > self.ptr_idx:
            for _ in range(idx - self.ptr_idx):
                cur_node = cur_node.right
            self.ptr = cur_node
            self.ptr_idx = idx
            return

        if idx < self.ptr_idx:
            for _ in range(self.ptr_idx - idx):
                cur_node = cur_node.left

            self.ptr = cur_node
            self.ptr_idx = idx
            return

    @staticmethod
    def split_segment(node):
        if node.len_ % 2 == 0:
            return node.len_ // 2, node.len_ // 2

        return node.len_ // 2, node.len_ // 2 + 1

    @staticmethod
    def _make_linked_list(companies):
        first = companies[0]
        head = cur_node = Node(first)
        cur_sum = first ** 2
        for company in companies[1:]:
            new_node = Node(company)
            cur_node.right = new_node
            new_node.left = cur_node
            cur_sum += company ** 2

            cur_node = new_node

        return head, cur_sum

    def __repr__(self):
        cur_node = self.ptr
        while cur_node.left:
            cur_node = cur_node.left

        cur_list = []
        while cur_node:
            cur_list.append(cur_node.len_)
            cur_node = cur_node.right

        return str(cur_list)


if __name__ == '__main__':
    n = int(input())
    companies = list(map(int, input().split()))

    dll = DoublyLinkedList(companies)
    print(dll.sum_)

    k = int(input())
    actions = []
    for _ in range(k):
        action_type, idx = map(int, input().split())
        if action_type == 1:
            print(dll.bankruptcy(idx))
        elif action_type == 2:
            print(dll.division(idx))
