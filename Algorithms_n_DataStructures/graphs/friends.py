N, S = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


def dfs(v, visited) -> None:
    visited[v] = True
    global res
    res += 1
    for to in range(N):
        if graph[v][to] == 1 and not visited[to]:
            dfs(to, visited)


res = 0
visited = [False] * N
dfs(S - 1, visited)
print(res - 1)
