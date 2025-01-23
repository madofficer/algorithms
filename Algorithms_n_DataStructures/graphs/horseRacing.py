N, K = map(int, input().split())
K -= 1
edges = [[] for _ in range(N)]


def dfs(v, visited):
    visited[v] = True
    for to in edges[v]:
        if not visited[to]:
            dfs(to, visited)


while True:
    x = list(map(int, input().split()))
    if len(x) == 1:
        break

    u = x[0] - 1
    v = x[1] - 1
    edges[u].append(v)
    if v == K:
        print("No")
        exit()

visited = [False] * N

dfs(K, visited)
print("Yes" if all(visited) else "No")
