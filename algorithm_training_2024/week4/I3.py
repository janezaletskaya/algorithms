# Пара путей
# from memory_profiler import memory_usage

class Node:

    def __init__(self, idx):
        self.idx = idx
        self.neighs: list[Node] = list()

    def __repr__(self):
        return f'{self.idx}, n_neighs={len(self.neighs)}'


class Tree:

    def __init__(self, n):
        self.n = n
        self.nodes: list[Node] = [Node(i) for i in range(0, n+1)]

    def add_edge(self, idx1, idx2):
        node1 = self.nodes[idx1]
        node2 = self.nodes[idx2]

        node1.neighs.append(node2)
        node2.neighs.append(node1)


def rem(a, b, c, out):
    if a == out:
        return b, c, 0
    if b == out:
        return a, c, 0
    if c == out:
        return a, b, 0
    return a, b, c


def max3(a, b, c, new):
    if new >= a:
        return new, a, b
    if new >= b:
        return a, new, b
    if new >= c:
        return a, b, new

    return a, b, c


def remt(a, b, c, out):
    if a[0] == out[0]:
        return b, c, (0, 0)
    if b[0] == out[0]:
        return a, c, (0, 0)
    if c[0] == out[0]:
        return a, b, (0, 0)
    return a, b, c


def max3t(a, b, c, new):
    if new[0] >= a[0]:
        return new, a, b
    if new[0] >= b[0]:
        return a, new, b
    if new[0] >= c[0]:
        return a, b, new

    return a, b, c


def dfs1(n, root: Node) -> list[list[int]]:
    dp = [[(0, 0), (0, 0), (0, 0), 0, 0, 0] for _ in range(n+1)]

    stack: list[tuple[Node, Node, bool]] = [(Node(0), root, False)]

    while stack:
        parent, cur, processed = stack.pop()

        if processed:
            # print(parent.idx, cur.idx)
            # print(dp[1:])
            l1, l2, l3 = (0, 0), (0, 0), (0, 0)
            r1, r2, r3 = 0, 0, 0
            for neigh in cur.neighs:
                if neigh == parent:
                    continue
                (childl1, childl1r), (childl2, _) = dp[neigh.idx][0], dp[neigh.idx][1]

                rnew = max(dp[neigh.idx][3], childl1 + childl2)
                r1, r2, r3 = max3(r1, r2, r3, rnew)

                lnew = (childl1 + 1, rnew)
                l1, l2, l3 = max3t(l1, l2, l3, lnew)

            dp[cur.idx][0] = l1
            dp[cur.idx][1] = l2
            dp[cur.idx][2] = l3
            dp[cur.idx][3] = r1
            dp[cur.idx][4] = r2
            dp[cur.idx][5] = r3
        else:
            stack.append((parent, cur, True))
            for neigh in cur.neighs:
                if neigh == parent:
                    continue
                stack.append(tuple((cur, neigh, False)))

    return dp


def available1(r1, r2, r3, delr1):
    if r1 != delr1:
        return r1
    if r2 != delr1:
        return r2
    return r3


def available2(r1, r2, r3, delr1, delr2):
    if r1 != delr1 and r1 != delr2:
        return r1
    if r2 != delr1 and r2 != delr2:
        return r2
    return r3


def available1t(l1, l2, l3, delr1):
    if l1[1] != delr1:
        return l1
    if l2[1] != delr1:
        return l2
    return l3


def available1t_2(l1, l2, l3, delr1):
    if l1[1] != delr1:
        if l2[1] != delr1:
            return l1, l2
        return l1, l3
    return l2, l3


def dfs2(n, root, dp: list[list[int | tuple[int, int]]]):
    fake_node = Node(0)
    max_mul = 0

    stack: list[tuple[Node, Node]] = [(fake_node, root)]

    while stack:
        parent, cur = stack.pop()
        # print(parent.idx, cur.idx)
        # print(dp[1:])

        # пересчитываем себя

        if parent.idx != 0:
            # готовим ответ от родителя

            rold = max(dp[cur.idx][3], dp[cur.idx][0][0] + dp[cur.idx][1][0])
            pr1, pr2, pr3 = rem(dp[parent.idx][3], dp[parent.idx][4], dp[parent.idx][5], rold)
            lold = (dp[cur.idx][0][0] + 1, rold)
            pl1, pl2, pl3 = remt(dp[parent.idx][0], dp[parent.idx][1], dp[parent.idx][2], lold)
            # print(f'{lold=} {rold=}')
            # print(f'{pl1=} {pl2=} {pl3=}')

            rnew = max(pr1, pl1[0] + pl2[0])
            dp[cur.idx][3], dp[cur.idx][4], dp[cur.idx][5] = max3(dp[cur.idx][3], dp[cur.idx][4], dp[cur.idx][5], rnew)
            lnew = (pl1[0] + 1, rnew)
            dp[cur.idx][0], dp[cur.idx][1], dp[cur.idx][2] = max3t(dp[cur.idx][0], dp[cur.idx][1], dp[cur.idx][2], lnew)
            # print(f'{lnew=} {rnew=}')
            # print(dp[1:])

        # считаем ответ
        curr1, curr2, curr3 = dp[cur.idx][3], dp[cur.idx][4], dp[cur.idx][5]
        curl1, curl2, curl3 = dp[cur.idx][0], dp[cur.idx][1], dp[cur.idx][2]

        # самый длинный путь ЧЕРЕЗ нас * на оставшийся самый длинный путь НЕ ЧЕРЕЗ нас
        available_r1 = available2(curr1, curr2, curr3, curl1[1], curl2[1])
        mul1 = (curl1[0] + curl2[0]) * available_r1
        # print(f'{curl1=} {curl2=} {available_r1=}')
        # самый длинный путь НЕ ЧЕРЕЗ нас * второй самый длинный путь НЕ ЧЕРЕЗ нас
        mul2 = curr1 * curr2
        # print(f'{curr1=} {curr2=}')
        # самый длинны путь ДО нас * на оставшийся самый длинный путь НЕ ЧЕРЕЗ нас
        available_r1 = available1(curr1, curr2, curr3, curl1[1])
        mul3 = curl1[0] * available_r1
        # print(f'{curl1=} {available_r1=}')
        # самый длинный путь НЕ ЧЕРЕЗ нас * на оставшийся самый длинный путь ДО нас
        available_l1 = available1t(curl1, curl2, curl3, curr1)
        mul4 = curr1 * available_l1[0]
        # print(f'{curr1=} {available_l1=}')
        # самый длинный путь НЕ ЧЕРЕЗ нас * на оставшийся самый длинный путь ЧЕРЕЗ нас
        available_l1, available_l2 = available1t_2(curl1, curl2, curl3, curr1)
        mul5 = curr1 * (available_l1[0] + available_l2[0])

        # выбираем максимум
        max_mul = max(max_mul, mul1, mul2, mul3, mul4, mul5)
        # print(f'{max_mul=} {mul1=} {mul2=} {mul3=} {mul4=} {mul5=}')

        for neigh in cur.neighs:
            if neigh == parent:
                continue
            stack.append(tuple((cur, neigh)))

    return max_mul


def fast_solution(tree: Tree):
    dp = dfs1(tree.n, tree.nodes[1])
    ans = dfs2(tree.n, tree.nodes[1], dp)
    return ans


def create_tree_from_console():
    n = int(input())
    tree = Tree(n)
    for _ in range(n - 1):
        idx1, idx2 = map(int, input().split())
        tree.add_edge(idx1, idx2)
    return tree


def main():
    tree = create_tree_from_console()
    print(fast_solution(tree))


if __name__ == '__main__':
    main()
