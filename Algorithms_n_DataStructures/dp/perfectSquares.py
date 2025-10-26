class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0

        # precompute each number less than target
        for num in range(1, n + 1):
            for s in range(1, num + 1):
                # possible square
                square = s ** 2
                if num - square < 0:
                    break
                # choose min possible number of steps to sum up to the current num
                dp[num] = min(dp[num], 1 + dp[num - square])

        return dp[-1]