from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        points = set()
        for i in nums:
            points |= set(range(i[0], i[1] + 1))
        return len(points)


print(Solution().numberOfPoints([[3, 6], [1, 5], [4, 7]]))
