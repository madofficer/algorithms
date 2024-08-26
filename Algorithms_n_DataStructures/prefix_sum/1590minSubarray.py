from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        l = len(nums)
        prefix_sum = [0] * l
        prefix_sum[0] = nums[0]
        for i in range(1, l):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        remainder = prefix_sum[-1] % p

        if remainder == 0:
            return 0

        prefix_sums = {0: -1}
        min_length = l

        for i in range(l):
            curr_remainder = prefix_sum[i] % p
            complement_remainder = (curr_remainder - remainder) % p
            if complement_remainder in prefix_sums:
                min_length = min(min_length, i - prefix_sums[complement_remainder])
            prefix_sums[curr_remainder] = i

        return min_length if min_length < l else -1


print(Solution().minSubarray([3, 1, 4, 2]

                             , 6))
