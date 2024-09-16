N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
edges = [[] for _ in range(N)]
for i in range(N):
    for j in range(i + 1, N):
        if G[i][j]:
            edges[i].append(j)
            edges[j].append(i)


def dfs(v):
    global edge
    visited[v] = True
    for to in edges[v]:
        edge += 1
        if not visited[to]:
            dfs(to)


count = 0
edge = 0

for i in visited:
    if not i:
        dfs(i)
        count += 1
        if count > 1:
            print('NO')
            exit()

if edge // 2 == N - 1:
    print('YES')
else:
    print('NO')
