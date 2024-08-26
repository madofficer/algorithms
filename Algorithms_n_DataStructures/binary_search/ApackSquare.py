w, h, n = map(int, input().split())

l = 0

r = 10 ** 15
ans = 0
while l <= r:
    mid = (l + r) // 2

    if (mid // w) * (mid // h) >= n:
        r = mid - 1
        ans = mid
    else:
        l = mid + 1

print(ans)
