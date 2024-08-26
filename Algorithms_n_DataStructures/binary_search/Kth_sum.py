n, k = map(int, input().split())  # n: list len; k: sum index

a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))


def count_less(x: int, a, b: list) -> int:
    counter = 0
    for i in range(n):
        l = 0
        r = n - 1
        res = -1
        while l <= r:
            mid = (l + r) // 2

            if b[mid] <= x - a[i]:
                l = mid + 1
                res = mid
            else:
                r = mid - 1
        counter += res + 1
    return counter


l = 0
r = a[-1] + b[-1] + 1
ans = 0
while l <= r:
    mid = (l + r) // 2

    if count_less(mid, a, b) >= k:
        r = mid - 1
        ans = mid
    else:
        l = mid + 1

print(ans)
