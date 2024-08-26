n, k = map(int, input().split())

arr = list(map(int, input().split()))

queries = list(map(int, input().split()))

for x in queries:
    l = 0
    r = n - 1
    ans = 0

    while l <= r:
        mid = (l + r) // 2

        if arr[mid] >= x:
            r = mid - 1
            ans = mid + 1
        else:
            l = mid + 1

    if arr[-1] < x:
        print(n + 1)
    else:
        print(ans)
