n, d = map(int, input().split())

a = list(map(int, input().split()))


def ok(x: int, arr: list) -> list:
    prefix_sum = [0] * (n + 1)
    pos_min = [0] * (n + 1)
    min_prefix_sum = [0] * (n + 1)

    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1] - x

    for i in range(1, n + 1):
        if prefix_sum[i] <= min_prefix_sum[i - 1]:
            pos_min[i] = i
            min_prefix_sum[i] = prefix_sum[i]
        else:
            min_prefix_sum[i] = min_prefix_sum[i - 1]
            pos_min[i] = pos_min[i - 1]

    for r in range(d, n + 1):
        if min_prefix_sum[r - d] <= prefix_sum[r]:
            return [pos_min[r - d], r]
    else:
        return [-1, 1]


l = 0
r = max(a)
ans_l, ans_r = -1, -1

for i in range(100):
    mid = (l + r) / 2
    pos = ok(mid, a)

    if pos[0] != -1:
        l = mid
        ans_l, ans_r = pos
    else:
        r = mid

print(ans_l + 1, ans_r)
