# F. Свинки-копилки
def find_components(graph):
    visited = set()
    components = []

    def dfs(vertex, current_component):
        stack = [vertex]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                current_component.append(node)
                stack.extend(graph[node] - visited)

    for vertex in graph:
        if vertex not in visited:
            current_component = []
            dfs(vertex, current_component)
            components.append(current_component)

    return components


if __name__ == '__main__':
    n = int(input())
    graph = {i: set() for i in range(n)}
    for i in range(n):
        v = int(input()) - 1
        graph[i].add(v)
        graph[v].add(i)

    components = find_components(graph)
    print(len(components))


