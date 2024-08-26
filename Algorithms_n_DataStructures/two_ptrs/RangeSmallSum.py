n, s = map(int, input().split())  # n: num of vals; s: target sum

a = list(map(int, input().split()))

curr_sum = 0
l = 0
res = 0
for r in range(n):

    curr_sum += a[r]

    while curr_sum > s:
        curr_sum -= a[l]
        l += 1

    res = max(res, r - l + 1)

print(res)
