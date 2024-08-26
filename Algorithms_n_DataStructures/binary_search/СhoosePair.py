n, k = map(int, input().split())
a, b = [0] * n, [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())


def pair_counter(x, n: int, a, b: list) -> int:
    temp = [0] * n

    for i in range(n):
        temp[i] = a[i] - x * b[i]

    temp.sort(reverse=True)

    pair_count = 0
    has_sum = 0

    for i in range(n):
        if temp[i] >= 0:
            has_sum += temp[i]
            pair_count += 1

    for i in range(n):
        if temp[i] < 0:
            has_sum += temp[i] + 10e-7
            if has_sum < 0:
                break
            pair_count += 1

    return pair_count


l = 0
r = 10 ** 12
ans = 0
for i in range(100):
    mid = (l + r) / 2

    if pair_counter(mid, n, a, b) >= k:
        l = mid
        ans = mid
    else:
        r = mid

print(ans)
