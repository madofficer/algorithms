from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        prefix_xor = [nums[0]]
        for i in range(1, len(nums)):
            prefix_xor.append((prefix_xor[i - 1] ^ nums[i]))

        return [prefix_xor[len(nums) - i - 1] ^ ((1 << maximumBit) - 1) for i in range(len(nums))]


print(Solution().getMaximumXor([0, 1, 1, 3], 2))
