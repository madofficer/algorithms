N, M = map(int, input().split())
edges = [[] for _ in range(N)]
color = [0] * N
flag = True
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)


def dfs(v, c):
    global flag
    color[v] = c
    for to in edges[v]:
        if color[to] == 0:
            nc = 1 if c == 2 else 2
            dfs(to, nc)
        elif color[to] == c:
            flag = False


for i in range(N):
    if color[i] == 0:
        dfs(i, 1)
    if not flag:
        print('NO')
        exit()

print('YES')
