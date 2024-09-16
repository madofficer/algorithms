n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [0] * (m + n)

i, j = 0, 0

while i < n or j < m:

    if j == m or (i < n and a[i] < b[j]):
        c[i + j] = a[i]
        i += 1

    else:
        c[i + j] = b[j]
        j += 1

print(*c)
