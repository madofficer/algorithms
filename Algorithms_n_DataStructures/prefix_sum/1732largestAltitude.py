from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        top = 0
        current = 0
        for i in gain:
            current += i
            top = max(top, current)
        return top


print(Solution().largestAltitude([-4,-3,-2,-1,4,3,2]))
