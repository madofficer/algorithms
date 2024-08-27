from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        hash_map = {}
        if k == 0:
            return False
        if k >= n:
            return n != len(set(nums))

        l = 0
        for i in range(n):
            if nums[i] in hash_map:
                distance = i - hash_map[nums[i]]
                if distance <= k:
                    return True
                else:
                    hash_map[nums[i]] = i
            else:
                hash_map[nums[i]] = i

        return False


print(Solution().containsNearbyDuplicate([4, 1, 2, 3, 1, 5], 3))
