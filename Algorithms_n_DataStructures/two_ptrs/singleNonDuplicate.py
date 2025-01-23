from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 1, len(nums) - 2
        if r < 0:
            return nums[r]


        while l <= r:
            mid = (l + r) // 2

            if mid % 2 == 0:
                if nums[mid] == nums[mid - 1]:
                    r = mid - 1
                elif nums[mid] == nums[mid + 1]:
                    l = mid + 1
                else:
                    return nums[mid]
            else:
                if nums[mid] == nums[mid - 1]:
                    l = mid + 1
                elif nums[mid] == nums[mid + 1]:
                    r = mid - 1
                else:
                    return nums[mid]
        if l == r:
            return nums[l]


print(Solution().singleNonDuplicate([1, 1, 2]))
