n, r = map(int, input().split())

a = list(map(int, input().split()))

i = 0
res = 0

for j in range(1, n):

    while abs(a[j] - a[i]) > r and i < j:
        if abs(a[j] - a[i]) > r:
            res += n - j
        i += 1

print(res)
