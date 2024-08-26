n, k = map(int, input().split())

coords = list(map(int, input().split()))


def ok(M: int, a: list) -> bool:
    cows = 1
    prev_cow = 0
    for i in range(1, len(a)):
        if a[i] - a[prev_cow] >= M:
            cows += 1
            prev_cow = i

    return cows >= k


l = 0
r = coords[-1] + 1
ans = 0

while l <= r:
    mid = (l + r) // 2

    if ok(mid, coords):
        l = mid + 1
        ans = mid
    else:
        r = mid - 1

print(ans)
