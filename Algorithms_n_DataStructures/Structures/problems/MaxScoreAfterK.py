from math import ceil
from typing import List
import heapq


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)
        score = 0
        for i in range(k):
            curr = heapq.heappushpop(nums, -ceil(nums[0] / -3))
            score += curr

        return -score


print(Solution().maxKelements([1, 10, 3, 3, 3], 3))
