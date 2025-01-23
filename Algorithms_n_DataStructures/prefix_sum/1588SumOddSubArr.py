from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = 0
        for i in range(1, len(arr) + 1, 2):
            for j in range(len(arr)):
                if j + i <= len(arr):
                    s += sum(arr[j : j + i])
        return s


print(Solution().sumOddLengthSubarrays([1, 4, 2, 5, 3]))
