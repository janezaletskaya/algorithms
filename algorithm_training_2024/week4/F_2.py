# Бюрократия
import sys
from collections import deque, defaultdict

sys.setrecursionlimit(200000)

class Node:
    def __init__(self, num, boss):
        self.num = num
        self.boss = boss
        self.coins = 0
        self.employees = deque()

    def __repr__(self):
        return f'name={self.num}: employees={list(e.num for e in self.employees)}'

def make_tree(lst):
    tree = {1: Node(1, None)}

    for employee, boss in enumerate(lst, start=2):
        if boss not in tree:
            tree[boss] = Node(boss, None)
        if employee not in tree:
            tree[employee] = Node(employee, tree[boss])
        else:
            tree[employee].boss = tree[boss]

        tree[boss].employees.append(tree[employee])

    return tree

def solution(tree, n):
    # Счётчик монет для всех сотрудников
    coins = [0] * (n + 1)

    # Найдём всех сотрудников без подчинённых
    leaves = deque(node for node in tree.values() if not node.employees)

    # Проходимся по дереву, начиная с сотрудников без подчинённых
    while leaves:
        current = leaves.popleft()

        # Считаем монеты, которые получает текущий сотрудник
        coins[current.num] += 1

        # Добавляем монеты начальнику, если он существует
        if current.boss:
            coins[current.boss.num] += coins[current.num]
            # Удаляем текущего сотрудника из списка подчинённых начальника
            current.boss.employees.remove(current)

            # Если у начальника больше нет подчинённых, он становится листом
            if not current.boss.employees:
                leaves.append(current.boss)

    return coins[1:]


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    tree = make_tree(lst)
    res = solution(tree, n)
    print(*res)