from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        if k >= n:
            return arr

        l, r = 0, n - k
        while l < r:

            mid = (l + r) // 2

            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid

        return arr[l:r + 1]


print(Solution().findClosestElements([1, 3], 2, 2))
