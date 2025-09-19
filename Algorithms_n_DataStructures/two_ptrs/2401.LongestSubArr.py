from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0
        res = 1

        for r in range(1, len(nums)):
            if nums[r] & nums[r - 1] != 0:
                res = max(res, r - l + 1)
                l = r

        return res


print(Solution().longestNiceSubarray([1, 3, 8, 48, 10]))
