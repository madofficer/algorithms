n, k = map(int, input().split())
prices = list(map(int, input().split()))

max_income = 0
for i in range(n):
    j = 1
    while j <= k and i + j < n:
        max_income = max(max_income, prices[i + j] - prices[i])
        j += 1

print(max_income)