from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if k == 1:
            return max(nums)
        res = 0
        current_sum = 0
        digits_dict = {}

        l = 0
        for r in range(len(nums)):

            if len(digits_dict) < k:
                if nums[r] not in digits_dict:
                    digits_dict[nums[r]] = 1
                else:
                    digits_dict[nums[r]] += 1
                    while digits_dict[nums[r]] > 1:
                        digits_dict[nums[l]] -= 1
                        current_sum -= nums[l]
                        if digits_dict[nums[l]] == 0:
                            del digits_dict[nums[l]]
                        l += 1
                current_sum += nums[r]
            elif len(digits_dict) > k:
                digits_dict[nums[l]] -= 1
                current_sum -= nums[l]
                if digits_dict[nums[l]] == 0:
                    del digits_dict[nums[l]]
            if len(digits_dict) == k:
                res = max(res, current_sum)
                if nums[l] in digits_dict:
                    digits_dict[nums[l]] -= 1
                    current_sum -= nums[l]
                    if digits_dict[nums[l]] == 0:
                        del digits_dict[nums[l]]
                l += 1

        return res


print(Solution().maximumSubarraySum([1,1,1,7,8,9], 3))
