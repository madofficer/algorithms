def count_fence_ways(length):
    dp = [0] * (length + 1)
    dp[1] = 1

    for i in range(2, length + 1):
        dp[i] += dp[i - 1]

        if i >= 2:
            dp[i] += dp[i - 2]

        if i >= 5:
            dp[i] += dp[i - 5]

    return dp[length]


length_of_fence = 14
result = count_fence_ways(length_of_fence)
print(f"Num of ways to build fence of {length_of_fence} m: {result}")