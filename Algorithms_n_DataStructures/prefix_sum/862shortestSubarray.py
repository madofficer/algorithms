from collections import deque
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        l = len(nums)
        min_length = float('inf')
        min_sum = 0
        q = deque()
        prefix_sum = 0

        for i in range(l):
            prefix_sum += nums[i]

            if prefix_sum - min_sum >= k:
                min_length = min(min_length, i + 1)

            while q and prefix_sum - q[0][1] >= k:
                min_length = min(min_length, i - q[0][0])
                q.popleft()

            while q and prefix_sum <= q[-1][1]:
                q.pop()

            q.append((i, prefix_sum))
            min_sum = min(min_sum, prefix_sum)

        if min_length == float('inf'):
            return -1

        return min_length


print(Solution().shortestSubarray())
