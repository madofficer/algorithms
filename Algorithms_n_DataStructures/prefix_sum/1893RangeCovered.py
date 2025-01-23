from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        interval = set()
        for i in ranges:
            interval.update(list(range(i[0], i[1] + 1)))
        for i in range(left, right + 1):
            if i not in interval:
                return False
        else:
            return True


print(Solution().isCovered([[1, 2], [3, 4], [5, 6]], 2, 5))
