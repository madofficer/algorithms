n, k = map(int, input().split())  # n: table size; k: val index


def count_less(x: int, n: int) -> int:
    count = 0

    for i in range(1, n + 1):
        count += min(x // i, n)
    return count


l = int(k ** 0.5)
r = n ** 2
ans = 0
while l <= r:
    mid = (l + r) // 2

    if count_less(mid, n) < k:
        l = mid + 1
        ans = mid + 1
    else:
        r = mid - 1
print(1 if ans == 0 else ans)
