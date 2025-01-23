from collections import deque


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


N = int(input())


def board(coord):
    return 1 <= coord.x <= N and 1 <= coord.y <= N


start = Coordinate(*map(int, input().split()))
finish = Coordinate(*map(int, input().split()))

grid = [[float("inf")] * (N + 1) for _ in range(N + 1)]
dx = (1, -1, 2, -2, 1, -1, 2, -2)
dy = (2, 2, 1, 1, -2, -2, -1, -1)

dq = deque([start])
grid[start.x][start.y] = 0

while dq:
    curr_v = dq.popleft()
    for i in range(8):
        new_v = Coordinate(curr_v.x + dx[i], curr_v.y + dy[i])
        if not board(new_v):
            continue

        if grid[new_v.x][new_v.y] > grid[curr_v.x][curr_v.y] + 1:
            grid[new_v.x][new_v.y] = grid[curr_v.x][curr_v.y] + 1
            dq.append(new_v)

print(grid[finish.x][finish.y])
