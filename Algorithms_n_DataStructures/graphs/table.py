n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
table = [[float("inf")] * m for _ in range(n)]


class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def is_table(coord: Coords) -> bool:
    return 0 <= coord.x < m and 0 <= coord.y < n


stack = []
for i in range(n):
    for j in range(m):
        if grid[i][j]:
            stack.append(Coords(j, i))
            table[i][j] = 0
# BFS
while stack:
    nstack = []
    dx = (0, 0, 1, -1)
    dy = (-1, 1, 0, 0)
    for coord in stack:
        for i in range(4):
            nc = Coords(coord.x + dx[i], coord.y + dy[i])
            if is_table(nc) and table[nc.y][nc.x] > table[coord.y][coord.x] + 1:
                table[nc.y][nc.x] = table[coord.y][coord.x] + 1
                nstack.append(nc)
    stack = nstack

for i in table:
    print(*i)
