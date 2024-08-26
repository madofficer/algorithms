n = int(input())

berries = [list(map(int, input().split())) for _ in range(n)]

berries_weighted = [[berries[i][0] / berries[i][1], i] if berries[i][1] > 0 else [berries[i][0], i] for i in
                    range(len(berries))]
berries_weighted = sorted(berries_weighted, key=lambda x: x[0], reverse=True)
print(berries_weighted)
order = [i[1] for i in berries_weighted]
local_max = 0
current = 0
for i in order:
    current += berries[i][0]
    local_max = max(local_max, current)
    current -= berries[i][1]

print(local_max)
print(*[i + 1 for i in order])
