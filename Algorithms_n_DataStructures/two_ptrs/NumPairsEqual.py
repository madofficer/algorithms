n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
i = 0

for j in range(m):
    count = 0
    while i < n and a[i] <= b[j]:
        if a[i] == b[j]:
            count += 1
        i += 1
    if j > 0 and b[j] == b[j - 1]:
        c.append(c[-1])
    else:
        c.append(count)
print(sum(c))
