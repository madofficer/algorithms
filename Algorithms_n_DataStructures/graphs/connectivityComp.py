import sys
import bisect

sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
edges = [[] for _ in range(N)]
visited = [False] * N
comps = []
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)

component = []


def dfs(v) -> None:
    visited[v] = True
    pos = bisect.bisect_left(component, v + 1)
    if pos == len(component) or component[pos] != v + 1:
        bisect.insort(component, v + 1)

    for to in edges[v]:
        if not visited[to]:
            dfs(to)


for i in range(N):
    if not visited[i]:
        component.clear()
        dfs(i)
        comps.append(component.copy())

print(len(comps))
for comp in comps:
    if len(comp) > 0:
        print(len(comp))
        print(*comp)
