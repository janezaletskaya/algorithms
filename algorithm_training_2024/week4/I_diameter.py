class Node:
    def __init__(self, idx):
        self.idx = idx
        self.neighs: set[Node] = set()

    def __repr__(self):
        return f'Node({self.idx})'


class Tree:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, idx1, idx2):
        if idx1 not in self.nodes:
            self.nodes[idx1] = Node(idx1)
        if idx2 not in self.nodes:
            self.nodes[idx2] = Node(idx2)

        self.nodes[idx1].neighs.add(self.nodes[idx2])
        self.nodes[idx2].neighs.add(self.nodes[idx1])

    def max_two_paths(self):
        n = len(self.nodes)
        max_path_down = [0] * (n + 1)  # Самый длинный путь вниз
        top_two_down = [[0, 0] for _ in range(n + 1)]  # Две максимальные длины вниз

        # Первый DFS проход: считаем max_path_down и top_two_down
        def dfs1(node, parent):
            for neigh in node.neighs:
                if neigh == parent:
                    continue
                dfs1(neigh, node)
                length = max_path_down[neigh.idx] + 1
                if length > top_two_down[node.idx][0]:
                    top_two_down[node.idx][1] = top_two_down[node.idx][0]
                    top_two_down[node.idx][0] = length
                elif length > top_two_down[node.idx][1]:
                    top_two_down[node.idx][1] = length

            max_path_down[node.idx] = top_two_down[node.idx][0]

        dfs1(self.nodes[1], None)

        # Второй DFS проход: пересчитываем значения для каждой вершины
        def dfs2(node, parent, parent_max_path):
            nonlocal max_mul
            # Находим два лучших непересекающихся пути
            best_two_paths = sorted(
                [parent_max_path] + top_two_down[node.idx], reverse=True
            )[:2]
            max_mul = max(max_mul, best_two_paths[0] * best_two_paths[1])

            # Передаем информацию детям
            for neigh in node.neighs:
                if neigh == parent:
                    continue
                # Пересчитываем parent_max_path для дочерней вершины
                new_parent_max_path = (
                    parent_max_path + 1
                    if max_path_down[neigh.idx] + 1 != max_path_down[node.idx]
                    else top_two_down[node.idx][1] + 1
                )
                dfs2(neigh, node, new_parent_max_path)

        max_mul = 0
        dfs2(self.nodes[1], None, 0)
        return max_mul


def create_tree_from_console():
    n = int(input())
    tree = Tree()
    for _ in range(n - 1):
        u, v = map(int, input().split())
        tree.add_edge(u, v)
    return tree


def main():
    tree = create_tree_from_console()
    print(tree.max_two_paths())


if __name__ == '__main__':
    main()