n, s = map(int, input().split())

a = list(map(int, input().split()))

curr_sum = 0
l = 0
res = sum(a)
flag = False

for r in range(n):
    curr_sum += a[r]

    while curr_sum - a[l] >= s:
        curr_sum -= a[l]
        l += 1

    if curr_sum >= s:
        flag = True
        res = min(res, r - l + 1)

print(res if flag else -1)