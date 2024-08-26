from typing import List
from unittest import result


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        l = len(hours)
        prefix = [1 if i > 8 else -1 for i in hours]
        max_length = 0
        current_sum = 0
        pos = {}
        for i in range(l):
            current_sum += prefix[i]
            if current_sum > 0:
                max_length = max(max_length, i + 1)
            else:
                if not (current_sum in pos):
                    pos[current_sum] = i
                if current_sum - 1 in pos:
                    max_length = max(max_length, i - pos[current_sum - 1])

        return max_length


print(Solution().longestWPI([9, 6, 6]))
