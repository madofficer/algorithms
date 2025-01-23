class Solution:
    def pivotInteger(self, n: int) -> int:
        res = (n * (n + 1) / 2) ** 0.5

        if res % 1 != 0:
            return -1
        else:
            return int(res)


print(Solution().pivotInteger(8))
