from typing import List


class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        prefix_sum = [nums[0] * 2]
        local_max = nums[0]
        for i in range(1, len(nums)):
            local_max = max(local_max, nums[i])
            prefix_sum.append(prefix_sum[i - 1] + local_max + nums[i])

        return prefix_sum


print(Solution().findPrefixScore([1, 1, 2, 4, 8, 16]))
