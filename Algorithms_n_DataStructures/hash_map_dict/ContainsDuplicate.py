from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        n = len(nums)
        if k >= n:
            return n != len(set(nums))

        hash_map = {}
        for index, value in enumerate(nums):

            if value in hash_map and index - hash_map[value] <= k:
                return True

            hash_map[value] = index

        return False


print(Solution().containsNearbyDuplicate([4, 1, 2, 3, 1, 5], 3))
