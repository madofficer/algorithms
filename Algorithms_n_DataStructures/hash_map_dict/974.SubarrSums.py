from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)

        prefix_sum = [0] * (n + 1)
        ans = 0
        d = {}

        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

        for i in range(n + 1):
            prefix_sum[i] = (prefix_sum[i] + k) % k  # create non-negative sum

            if prefix_sum[i] in d:
                ans += d[prefix_sum[i]]
            print(ans)

            if prefix_sum[i] in d:
                d[prefix_sum[i]] += 1
            else:
                d[prefix_sum[i]] = 1
            print(d)

        return ans


print(Solution().subarraysDivByK([4, 5, 0, -2, -3, 1], 5))
