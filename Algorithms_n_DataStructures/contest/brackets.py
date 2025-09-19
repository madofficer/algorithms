MOD_ = 10 ** 9 + 7

def count_brackets(l, k, open, close):
    count = 0
    for t in range(3):
        if open[l][t] and close[k][t]:
            count += 1
    return count


n = int(input())
s = input()

dp = [[0] * n for _ in range(n)]
open = [[False] * 3 for _ in range(n)]
close = [[False] * 3 for _ in range(n)]

for i in range(n):
    ch = s[i]
    if ch == '(':
        open[i][0] = True
    elif ch == '{':
        open[i][1] = True
    elif ch == '[':
        open[i][2] = True
    elif ch == ')':
        close[i][0] = True
    elif ch == '}':
        close[i][1] = True
    elif ch == ']':
        close[i][2] = True
    elif ch == '?':
        open[i][0] = open[i][1] = open[i][2] = True
        close[i][0] = close[i][1] = close[i][2] = True

for length in range(2, n + 1):
    for left in range(n - length + 1):
        right = left + length - 1
        dp[left][right] = 0

        for mid in range(left + 1, right + 1, 2):
            bracket_counter = count_brackets(left, mid, open, close)

            if bracket_counter == 0:
                continue

            left_ways = dp[left + 1][mid - 1] if left + 1 <= mid - 1 else 1
            right_ways = dp[mid + 1][right] if mid + 1 <= right else 1

            total_ways = (left_ways * right_ways) % MOD_
            total_ways = (total_ways * bracket_counter) % MOD_

            dp[left][right] = (dp[left][right] + total_ways) % MOD_

print(dp[0][n - 1])