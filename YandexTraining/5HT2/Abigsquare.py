n = int(input())

coords = [list(map(int, input().split())) for _ in range(n)]
low_left = [float('inf'), float('inf')]
top_right = [float('-inf'), float('-inf')]
for x, y in coords:
    low_left[0] = min(low_left[0], x)
    low_left[1] = min(low_left[1], y)
    top_right[0] = max(top_right[0], x)
    top_right[1] = max(top_right[1], y)
print(low_left[0],low_left[1], top_right[0], top_right[1])