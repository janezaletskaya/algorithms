# H. Разрезание графа
import sys


input = sys.stdin.readline


class Graph:

    def __init__(self, n_vertex):
        self.prevs = [i for i in range(n_vertex)]
        self.depths = [0 for _ in range(n_vertex)]

    def add_edge(self, vertex1, vertex2):
        vertex1_root = self.find_root(vertex1)
        vertex2_root = self.find_root(vertex2)

        if vertex1_root == vertex2_root:
            return

        if self.depths[vertex1_root] < self.depths[vertex2_root]:
            self.prevs[vertex1_root] = vertex2_root
        elif self.depths[vertex1_root] > self.depths[vertex2_root]:
            self.prevs[vertex2_root] = vertex1_root
        else:
            self.prevs[vertex2_root] = vertex1_root
            self.depths[vertex1_root] += 1

        return

    def find_root(self, vertex):
        root = vertex
        while self.prevs[root] != root:
            root = self.prevs[root]

        while vertex != root:
            parent = self.prevs[vertex]
            self.prevs[vertex] = root
            vertex = parent

        return root

    def is_in_one_set(self, vertex1, vertex2):
        return self.find_root(vertex1) == self.find_root(vertex2)


if __name__ == '__main__':
    n_vertex, n_edges, n_queries = map(int, input().split())
    edges = set()
    for _ in range(n_edges):
        v1, v2 = map(int, input().split())
        edges.add((min(v1 - 1, v2 - 1), max(v1 - 1, v2 - 1)))

    queries = []
    edges_for_cut = set()
    for _ in range(n_queries):
        query, v1, v2 = input().split()
        v1 = int(v1) - 1
        v2 = int(v2) - 1
        if query == 'cut':
            edges_for_cut.add((min(v1, v2), max(v1, v2)))

        queries.append((query, v1, v2))

    graph = Graph(n_vertex)

    for edge in edges:
        if edge not in edges_for_cut:
            graph.add_edge(edge[0], edge[1])

    ans = []
    queries.reverse()
    for query_tuple in queries:
        query, v1, v2 = query_tuple

        if query == 'ask':
            in_one_set = graph.is_in_one_set(v1, v2)
            if in_one_set:
                ans.append('YES')
            else:
                ans.append('NO')
        elif query == 'cut':
            graph.add_edge(v1, v2)

    ans.reverse()
    for val in ans:
        print(val)
        