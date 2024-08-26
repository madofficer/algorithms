from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[i - 1])
        local_min = min(prefix_sum)
        if local_min < 0:
            return 1 - local_min
        else:
            return 1



print(Solution().minStartValue([1, -2, -3]))
