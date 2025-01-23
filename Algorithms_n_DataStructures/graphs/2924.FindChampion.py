import sys
from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        is_defeated = [False] * n

        for u, v in edges:
            is_defeated[v] = True

        champ = -1
        counter = 0

        for i in range(n):
            if not is_defeated[i]:
                champ = i
                counter += 1
            if counter > 1:
                return -1

        return champ


print(Solution().findChampion(7, [[1, 0], [2, 1], [2, 6], [3, 2], [3, 5], [4, 3]]))
