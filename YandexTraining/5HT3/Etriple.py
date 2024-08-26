n = []
a = [[], [], []]
for i in range(3):
    n.append(int(input()))
    a[i] = set(map(int, input().split()))

ans = []
for i in sorted(a[0] | a[1] | a[2]):
    if i in a[0] and i in a[1] or i in a[0] and i in a[2] or i in a[1] and i in a[2]:
        ans.append(i)

print(*ans)
