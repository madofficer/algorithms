from collections import deque

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
start, finish = map(int, input().split())
edges = [[] for _ in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        if matrix[i][j]:
            edges[i].append(j)
            edges[j].append(i)

dist = [None] * N
start -= 1
finish -= 1
dist[start] = 0
q = deque([start])

while q:
    v = q.popleft()
    for i in edges[v]:
        if dist[i] is None:
            dist[i] = dist[v] + 1
            q.append(i)
if dist[finish] is not None:
    print(dist[finish])
else:
    print(-1)
