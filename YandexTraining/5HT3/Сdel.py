from collections import Counter

n = int(input())

a = Counter(map(int, input().split()))

if len(a) <= 2:
    print(0)
else:
    m = 0
    for k in a.keys():
        if k + 1 in a:
            m = max(a[k] + a[k + 1], m)
    print(n - 1 if m == 0 else n - m)
