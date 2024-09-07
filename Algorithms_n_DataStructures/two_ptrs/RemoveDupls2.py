from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        curr_count = 1

        for r in range(1, len(nums)):
            if nums[r] == nums[r - 1]:
                curr_count += 1
            else:
                curr_count = 1

            if curr_count <= 2:
                nums[l] = nums[r]
                l += 1
        return l


print(Solution().removeDuplicates([1, 1, 1, 2, 2, 2, 3, 3]))
