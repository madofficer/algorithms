from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        num_distinct = len(set(nums))

        distinct_map = {}
        l = 0
        res = 0

        for r in range(len(nums)):

            if nums[r] in distinct_map:
                distinct_map[nums[r]] += 1

            else:
                distinct_map[nums[r]] = 1

            while l <= r and len(distinct_map) == num_distinct:
                res += n - r
                distinct_map[nums[l]] -= 1
                if distinct_map[nums[l]] == 0:
                    del distinct_map[nums[l]]
                l += 1

        return res


print(Solution().countCompleteSubarrays([1, 3, 1, 2, 2]))
