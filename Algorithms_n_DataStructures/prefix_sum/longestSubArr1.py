from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        right_prefix = [0] * n
        right_prefix[0] = 0
        left_prefix = [0] * n
        left_prefix[-1] = 0
        counter = 0

        for l in range(1, n):
            if nums[l - 1]:
                counter += 1
            else:
                counter = 0
            left_prefix[l] = counter

        counter = 0
        for r in range(n - 2, -1, -1):
            if nums[r + 1]:
                counter += 1
            else:
                counter = 0
            right_prefix[r] = counter

        print(right_prefix)
        print(left_prefix)

        res = -1

        for i in range(n):
            if not nums[i]:
                res = max(res, right_prefix[i] + left_prefix[i])

        return res if res > -1 else n - 1


print(Solution().longestSubarray([0, 0, 0]))
