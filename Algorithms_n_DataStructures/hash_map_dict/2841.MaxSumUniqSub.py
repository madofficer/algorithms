from typing import List


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        ans = 0
        n = len(nums)
        hash_map = {}
        curr_sum = 0

        for i in range(k):
            if nums[i] in hash_map:
                hash_map[nums[i]] += 1
            else:
                hash_map[nums[i]] = 1
            curr_sum += nums[i]

        if len(hash_map) >= m:
            ans = curr_sum

        for i in range(k, n):
            hash_map[nums[i - k]] -= 1
            curr_sum -= nums[i - k]
            if hash_map[nums[i - k]] == 0:
                del hash_map[nums[i - k]]

            if nums[i] in hash_map:
                hash_map[nums[i]] += 1
            else:
                hash_map[nums[i]] = 1
            curr_sum += nums[i]

            if m <= len(hash_map) <= k:
                ans = max(ans, curr_sum)

        return ans


print(Solution().maxSum([1, 1, 1, 3], 2, 2))
