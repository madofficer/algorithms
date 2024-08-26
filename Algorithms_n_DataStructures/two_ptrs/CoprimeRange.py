import math


def findMinimumLength(a):
    n = len(a)
    dp = [[0] * n for _ in range(n)]

    gcd = a[0]
    for i in range(1, n):
        gcd = math.gcd(gcd, a[i])

    if gcd != 1:
        return -1

    for i in range(n):
        dp[i][i] = 1

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            g = math.gcd(a[i], a[j])
            if g == 1:
                dp[i][j] = 2
            else:
                dp[i][j] = float('inf')
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])

    return dp[0][n - 1]


_ = int(input())
a = list(map(int, input().split()))
ans = findMinimumLength(a)
if ans == -1:
    print(-1)
else:
    print(ans)
