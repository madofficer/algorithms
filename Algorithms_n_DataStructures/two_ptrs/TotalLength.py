n, s = map(int, input().split())

a = list(map(int, input().split()))

l = 0
curr_sum = 0
res = 0

for r in range(n):
    curr_sum += a[r]

    while curr_sum > s:
        curr_sum -= a[l]
        l += 1
    res += (r - l + 1) * (r - l + 2) // 2

print(res)
