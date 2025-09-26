n = int(input())
a = list(map(int, input().split()))

if n < 2:
    print(0)
else:
    n_2 = 2 * n + 1
    s = [None] * n_2
    for i in range(n):
        s[2 * i + 1] = a[i]

    max_len = 0
    l, r = 0, -1
    d = [0] * (2 * n + 1)

    for i in range(n_2):
        k = 1 if i > r else min(d[l + r - i], r - i + 1)

        while 0 <= i - k and i + k < n_2 and s[i - k] == s[i + k]:
            k += 1

        d[i] = k
        if i + k - 1 > r:
            l = i - k + 1
            r = i + k - 1

        current_len = k - 1
        max_len = max(max_len, current_len)

    print(max_len if max_len > 1 else 0)


