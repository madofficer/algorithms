import sys

sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
edges = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)

k = int(input())
higher = list(map(int, input().split()))
higher = [i - 1 for i in higher]
capitals = set(higher)
cities = [[] for _ in range(k)]


def dfs(v: int, h: int) -> None:
    visited[v] = True
    cities[h].append(v + 1)
    for to in edges[v]:
        if not visited[to] and not (to in capitals):
            dfs(to, h)


for i in range(k):
    if not visited[higher[i]]:
        dfs(higher[i], i)

for i in cities:
    print(len(i))
    print(*i)
