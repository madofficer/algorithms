from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[:i]) for i in range(1, len(nums) + 1)]


print(Solution().runningSum([1, 1, 1, 1, 1]))
