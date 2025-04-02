# Бюрократия
import sys


sys.setrecursionlimit(200000)


class Node:

    def __init__(self, num, boss):
        self.num = num
        self.boss = boss

        self.employees = list()

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


def merge_dicts(dict1, dict2):
    for key, value in dict2.items():
        dict1[key] = dict1.get(key, 0) + value


def solution(tree):
    coins = [0] * (len(tree) + 1)

    def dfs(node, level):
        if node is None:
            return

        coins_dict = {level: 1}

        for employee in node.employees:
            coins_dict_n = dfs(employee, level + 1)
            merge_dicts(coins_dict, coins_dict_n)

        coins_from_dict = 0
        for level_from_dict, n_employees in coins_dict.items():
            coins_from_dict += (level_from_dict - level + 1) * n_employees

        coins[node.num] = coins_from_dict

        return coins_dict

    dfs(tree[1], 0)

    return coins[1:]


def solution2(tree):
    coins = [0] * (len(tree) + 1)

    def dfs(node):
        if node is None:
            return

        _coins = 0
        _n = 1
        for employee in node.employees:
            e_coins, e_n = dfs(employee)
            _coins += e_coins
            _n += e_n

        _coins += _n
        coins[node.num] = _coins

        return _coins, _n

    dfs(tree[1])

    return coins[1:]


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    tree = make_tree(lst)
    res = solution2(tree)
    print(*res)

