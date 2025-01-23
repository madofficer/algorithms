n, k = map(int, input().split())  # n: num of ranges; k: val index we look for

num_ranges = [[] for _ in range(n)]

for i in range(n):
    num_ranges[i] = list(map(int, input().split()))


def count_less(x: int, l: list) -> int:
    counter = 0
    for r in l:
        if x <= r[0]:
            pass
        else:
            counter += min(x, r[1] + 1) - r[0]

    return counter


l = 2 * -(10**9)
r = 2 * 10**9
ans = 0
while l <= r:
    mid = (l + r) // 2
    if count_less(mid, num_ranges) <= k:
        l = mid + 1
        ans = mid

    else:
        r = mid - 1

print(ans)
