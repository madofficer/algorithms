N, K = map(int, input().split())
a = list(map(int, input().split()))
res = float('-inf')
local_min = float('inf')
for r in range(K, N):
    l = r - K
    local_min = min(local_min, a[l])
    res = max(a[r] - local_min, res)

local_min = float('inf')
for l in range(N - 1 - K, -1, -1):
    r = l + K
    local_min = min(local_min, a[r])
    res = max(a[l] - local_min, res)

print(res)
