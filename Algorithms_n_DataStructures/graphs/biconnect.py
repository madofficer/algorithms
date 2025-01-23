from collections import defaultdict


def find_biconnected_components(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    tin = [-1] * n  # время входа в вершину
    low = [-1] * n  # минимальное достижимое время
    timer = [0]
    stack = []
    biconnected_components = []

    def dfs(v, parent):
        tin[v] = low[v] = timer[0]
        timer[0] += 1
        children = 0

        for to in graph[v]:
            if to == parent:
                continue
            if tin[to] != -1:  # назад по дереву
                low[v] = min(low[v], tin[to])
            else:
                stack.append((v, to))
                dfs(to, v)
                low[v] = min(low[v], low[to])
                if low[to] >= tin[v]:
                    # Мы нашли двусвязную компоненту
                    component = []
                    while stack:
                        edge = stack.pop()
                        component.append(edge)
                        if edge == (v, to):
                            break
                    biconnected_components.append(component)
                children += 1

    for i in range(n):
        if tin[i] == -1:
            dfs(i, -1)

    return biconnected_components


def count_resilient_pairs(n, edges):
    biconnected_components = find_biconnected_components(n, edges)
    count = 0

    for component in biconnected_components:
        nodes = set()
        for u, v in component:
            nodes.add(u)
            nodes.add(v)
        size = len(nodes)
        count += size * (size - 1) // 2  # Все пары в компоненте связаны

    return count


# Чтение данных

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for i in range(m)]

# Печать результата
print(count_resilient_pairs(n, edges))
