n, k = map(int, input().split())

arr = list(map(int, input().split()))


def ok(M: int, a: list) -> bool:
    count = 0
    cut = 0
    for i in range(n):
        if a[i] > mid:
            return False
        if count + a[i] > M:
            cut += 1
            count = a[i]
        else:
            count += a[i]
    if count > 0:
        cut += 1

    return cut <= k


l = 0
r = sum(arr) + 1
ans = 0
while l <= r:
    mid = (l + r) // 2

    if ok(mid, arr):
        r = mid - 1
        ans = mid
    else:
        l = mid + 1

print(ans)
