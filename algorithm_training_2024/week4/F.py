# Бюрократия
import sys
from collections import deque


sys.setrecursionlimit(100000)


class Node:

    def __init__(self, num, boss):
        self.num = num
        self.boss = boss

        self.coins = 0
        self.employees = deque()

    def __repr__(self):
        return f'name={self.num}: employees={self.employees}'


def make_tree(lst):
    tree = {1: Node(1, Node(0, None))}

    for employee, boss in enumerate(lst, start=2):
        boss_node = tree.get(boss, Node(boss, None))
        employee_node = tree.get(employee, Node(employee, boss_node))
        boss_node.employees.append(employee_node)

        tree[boss] = boss_node
        tree[employee] = employee_node

    return tree


def solution(tree):
    coins = [0] * (len(tree) + 1)

    while len(tree) > 1:
        leaf = None
        for node in tree.values():
            if not node.employees:
                if leaf is None or node.num < leaf.num:
                    leaf = node

        current = leaf
        level = 1
        while current.boss:
            coins[current.num] += level
            current = current.boss
            level += 1

        boss = leaf.boss
        del tree[leaf.num]

        if boss:
            boss.employees.popleft()

    coins[1] += 1

    return coins[1:]


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    tree = make_tree(lst)
    res = solution(tree)
    print(*res)

