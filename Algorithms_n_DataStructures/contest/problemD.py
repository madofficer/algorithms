n, m, d = map(int, input().split())
grid = [input().strip() for _ in range(n)]

prefix = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    row_sum = 0
    for j in range(1, m + 1):
        row_sum += 1 if grid[i - 1][j - 1] == 'x' else 0
        prefix[i][j] = prefix[i - 1][j] + row_sum

def is_available(k):
    for i in range(k, n + 1):
        for j in range(k, m + 1):
            x1, y1 = i - k + 1, j - k + 1
            x2, y2 = i, j
            total = prefix[x2][y2] - prefix[x1 - 1][y2] - prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1]
            if total == 0:
                return True
    return False

left, right = 0, min(n, m)
result = 0
while left <= right:
    mid = (left + right) // 2
    if is_available(mid):
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)
