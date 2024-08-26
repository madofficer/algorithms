n, x, y = map(int, input().split())

l = 0
r = 2 * 10 ** 18

while l <= r:
    mid = (l + r) // 2

    if (mid // x) + (mid // y) >= n - 1:
        r = mid - 1
        ans = mid
    else:
        l = mid + 1
if n == 1:
    print(min(x, y))
else:
    print(ans + min(x, y))
