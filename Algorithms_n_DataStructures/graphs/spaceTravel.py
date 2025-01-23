n = int(input())
edges = [[] for i in range(n)]
for i in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)

res = 0
for i in range(n):
    if len(edges[i]) > 1:
        res += 1

print(res)