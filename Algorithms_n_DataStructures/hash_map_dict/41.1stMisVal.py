from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hash_map = {x: 1 for x in nums}

        R = (10 ** 5) + 10

        for i in range(1, R):
            if i in hash_map:
                continue
            return i


print(Solution().firstMissingPositive([1, 1000]))
