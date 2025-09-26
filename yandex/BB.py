n = int(input())
p = [0] * 201
res = 0
for _ in range(n):
    x = int(input())
    p[x] += 1
    for i in range(x):
        res += p[i]
print(res)

