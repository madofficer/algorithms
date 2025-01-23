from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        print([sum(nums[:i]) for i in range(len(nums))])
        print([sum(nums[i + 1 :]) for i in range(len(nums))])
        return [abs(sum(nums[:i]) - sum(nums[i + 1 :])) for i in range(len(nums))]


print(Solution().leftRightDifference([10, 4, 8, 3]))
