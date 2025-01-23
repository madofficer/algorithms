import sys

sys.setrecursionlimit(10**6)
blackboard = [input().strip() for _ in range(8)]
visited = [[False] * 8 for _ in range(8)]


class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def is_blackboard(coord: Coords) -> bool:
    return 0 <= coord.x < 8 and 0 <= coord.y < 8


def dfs(coord: Coords) -> None:
    visited[coord.y][coord.x] = True
    dx = (-1, 0, 1, 0)
    dy = (0, -1, 0, 1)

    for to in range(4):
        nc = Coords(coord.x + dx[to], coord.y + dy[to])

        if is_blackboard(nc) and not visited[nc.y][nc.x]:
            if blackboard[nc.y][nc.x] != blackboard[coord.y][coord.x]:
                dfs(nc)


count = 0
for i in range(8):
    for j in range(8):
        if not visited[i][j]:
            coord = Coords(j, i)
            dfs(coord)
            count += 1

print(count)
