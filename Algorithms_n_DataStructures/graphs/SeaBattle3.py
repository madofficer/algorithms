from collections import deque

n, m = map(int, input().split())
graph = [input() for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dq = deque()


class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def is_battle(coord: Coords) -> bool:
    return 0 <= coord.x < m and 0 <= coord.y < n


res = [0, 0, 0]
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] != "-":
            dq.append(Coords(j, i))
            visited[i][j] = True
            status = (
                2 if graph[i][j] == "X" else 0
            )  # 0: full hp; 1: damaged; 2: destroyed
            while dq:
                v = dq.popleft()
                dx = (-1, 0, 0, 1)
                dy = (0, 1, -1, 0)

                for to in range(4):
                    nc = Coords(v.x + dx[to], v.y + dy[to])

                    if is_battle(nc) and not visited[nc.y][nc.x]:
                        visited[nc.y][nc.x] = True
                        if graph[nc.y][nc.x] != "-":
                            dq.append(nc)
                            if (status == 2 and graph[nc.y][nc.x] == "S") or (
                                status == 0 and graph[nc.y][nc.x] == "X"
                            ):
                                status = 1

            res[status] += 1

print(*res)
