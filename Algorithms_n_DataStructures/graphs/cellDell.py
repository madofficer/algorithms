import sys

sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
graph = [input() for _ in range(n)]
edges = [[] for _ in range(n)]

visited = [[False] * m for _ in range(n)]


class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def is_paper(coord: Coords) -> bool:
    return 0 <= coord.y < n and 0 <= coord.x < m


def dfs(coord: Coords) -> None:
    visited[coord.y][coord.x] = True
    dx = (-1, 0, 0, 1)
    dy = (0, -1, 1, 0)
    for to in range(4):
        new_coord = Coords(coord.x + dx[to], coord.y + dy[to])
        if (
            is_paper(new_coord)
            and not visited[new_coord.y][new_coord.x]
            and graph[new_coord.y][new_coord.x] == "#"
        ):
            dfs(new_coord)
        elif is_paper(new_coord) and graph[new_coord.y][new_coord.x] != "#":
            visited[new_coord.y][new_coord.x] = True


count = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == "#":
            coord = Coords(j, i)
            dfs(coord)
            count += 1
print(count)
