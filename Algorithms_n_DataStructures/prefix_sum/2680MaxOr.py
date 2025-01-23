from typing import List


class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        l = len(nums)
        prefix_bitwise = [nums[0]]
        for i in range(1, l):
            prefix_bitwise.append(prefix_bitwise[i - 1] | nums[i])
        suffix_bitwise = [0] * l
        suffix_bitwise[-1] = nums[-1]

        for i in range(l - 2, -1, -1):
            suffix_bitwise[i] = suffix_bitwise[i + 1] | nums[i]

        res = 0

        for i in range(l):
            k_num = nums[i] * (2**k)

            if i > 0:
                k_num |= prefix_bitwise[i - 1]
            if i + 1 < l:
                k_num |= suffix_bitwise[i + 1]
            res = max(k_num, res)

        return res


print(Solution().maximumOr([8, 1, 2], 2))
