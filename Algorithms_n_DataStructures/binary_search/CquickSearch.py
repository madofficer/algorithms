n = int(input())

arr = sorted(list(map(int, input().split())))

k = int(input())
ans = []
for q in range(k):
    L, R = map(int, input().split())

    l = 0
    r = n - 1
    idx_l = 0

    while l <= r:
        mid = (l + r) // 2

        if arr[mid] >= L:
            r = mid - 1
            idx_l = mid
        else:
            l = mid + 1

    l = 0
    r = n - 1
    idx_r = 0

    while l <= r:
        mid = (l + r) // 2

        if arr[mid] <= R:
            l = mid + 1
            idx_r = mid
        else:
            r = mid - 1
    if arr[idx_l] >= L and arr[idx_r] <= R:
        ans.append(idx_r - idx_l + 1)
    else:
        ans.append(0)

print(*ans)
