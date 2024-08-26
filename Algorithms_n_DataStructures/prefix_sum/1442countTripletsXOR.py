from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        result = 0
        for i in range(len(arr)):
            ss = 0
            for j in range(i, len(arr)):
                ss ^= arr[j]
                if ss == 0:
                    result += j - i
        return result


print(Solution().countTriplets([2, 3, 1, 6, 7]))
