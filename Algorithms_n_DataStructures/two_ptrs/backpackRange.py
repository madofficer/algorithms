n, s = map(int, input().split())

w = list(map(int, input().split()))
c = list(map(int, input().split()))

l = 0
weight = 0
cost = 0
res = 0

for r in range(n):

    weight += w[r]
    cost += c[r]

    while weight > s:
        weight -= w[l]
        cost -= c[l]
        l += 1
    else:
        res = max(res, cost)

print(res)