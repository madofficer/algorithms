n, k = map(int, input().split())

arr = list(map(int, input().split()))

queries = list(map(int, input().split()))

for x in queries:
    l = 0
    r = n - 1
    ans = l
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] <= x:
            l = mid + 1
            ans = mid
        else:
            r = mid - 1
    if arr[ans] == x:
        print('YES')
    else:
        print('NO')