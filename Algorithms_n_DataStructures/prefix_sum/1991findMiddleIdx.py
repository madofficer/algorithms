from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        a = [1 if abs(sum(nums[:i]) - sum(nums[i + 1:])) == 0 else 0 for i in range(len(nums))]
        try:
            return a.index(1)
        except:
            return -1


print(Solution().findMiddleIndex([2, 5]))
