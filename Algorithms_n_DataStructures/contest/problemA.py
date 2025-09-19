import math

n, m, x, y = map(int, input().split())
grid = [input() for _ in range(n * x)]

def is_awake(x2, y2):
    x1, y1 = x2 - x + 1, y2 - y + 1
    total = prefix[x2][y2] - prefix[x1 - 1][y2] - prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1]
    if total >= math.ceil((x * y) / 2):
        return True
    return False

awake = 0
prefix = [[0] * (m * y + 1) for _ in range(n * x + 1)]
for i in range(1, n * x + 1):
    row_sum = 0
    for j in range(1, m * y + 1):
        row_sum += 1 if grid[i - 1][j - 1] == 'X' else 0
        prefix[i][j] = prefix[i - 1][j] + row_sum
        if i % x == 0 and j % y == 0 and is_awake(i, j):
            awake += 1

print(awake)
