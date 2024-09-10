n, m, s, A, B = map(int, input().split())

a = sorted(list(map(int, input().split())))[::-1]
b = sorted(list(map(int, input().split())))[::-1]

cost = 0
weight = 0
res = 0

for i in range(n):
    cost += a[i]
    weight += A

    if weight <= s:
        res = max(res, cost)

r = n - 1
for i in range(m):
    cost += b[i]
    weight += B

    while r >= 0 and weight > s:
        weight -= A
        cost -= a[r]
        r -= 1

    if weight > s:
        break

    res = max(res, cost)


print(res)