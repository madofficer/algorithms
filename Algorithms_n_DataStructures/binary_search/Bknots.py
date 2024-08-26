n, k = map(int, input().split())

ropes = sorted([int(input()) for _ in range(n)])

l = 0

r = 10 ** 12

for i in range(1000):
    mid = (l + r) / 2

    s = 0
    flag = False
    for j in range(n):
        s += int(ropes[j] / mid)
    if s >= k:
        flag = True
    if flag:
        l = mid + 1
        ans = mid
    else:
        r = mid - 1

print(ans)
