from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        prefix_sum = [0] * (n + 2)
        suffix_sum = [0] * (n + 2)

        prefix_sum[1] = nums[0]
        suffix_sum[1] = nums[-1]

        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
            suffix_sum[n - i] = suffix_sum[n - i + 1] + nums[n - i - 1]

        print(prefix_sum)
        print(suffix_sum)

        for i in range(n):
            res[i] = (
                nums[i] * i
                - prefix_sum[i + 1]
                + suffix_sum[i + 1]
                - nums[i] * (n - i - 1)
            )

        return res


print(Solution().getSumAbsoluteDifferences([1, 4, 6, 8, 10]))
