from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:m].copy()

        i, j = 0, 0

        while i < m or j < n:

            if j == n or (i < m and temp[i] < nums2[j]):
                nums1[i + j] = temp[i]
                i += 1
            else:
                nums1[i + j] = nums2[j]
                j += 1


Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
