def get_cells(x1, y1, x2, y2):
    cells = set()
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            cells.add((x, y))
    return cells


def expand(prev):
    expanded = set()
    for (x, y) in prev:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= W and 1 <= ny <= H:
                expanded.add((nx, ny))
    return expanded


W, H = map(int, input().split())
N = int(input())

x1, y1, x2, y2 = map(int, input().split())
cur = get_cells(x1, y1, x2, y2)

result = "Yes"

for _ in range(1, N):
    x1, y1, x2, y2 = map(int, input().split())
    next_frame = get_cells(x1, y1, x2, y2)

    reachable = expand(cur)

    next_possible = reachable & next_frame

    if not next_possible:
        result = "No"
        break

    cur = next_possible

print(result)