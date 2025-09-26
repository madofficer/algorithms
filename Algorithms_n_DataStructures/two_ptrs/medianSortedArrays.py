from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        A = nums1 if n1 <= n2 else nums2
        B = nums2 if n2 >= n1 else nums1

        n = n1 + n2
        median_idx = n // 2
        l, r = 0, len(A) - 1 # bin search throw the shortest list

        while True:
            i = (l + r) // 2 # index A
            j = median_idx - i - 2 # index B

            A_left = A[i] if i >= 0 else float("-inf")
            A_right = A[i + 1] if i + 1 < len(A) else float("inf")

            B_left = B[j] if j >= 0 else float("-inf")
            B_right = B[j + 1] if j + 1 < len(B) else float("inf")

            if A_left <= B_right and A_right >= B_left:
                if n & 1:
                    return min(A_right, B_right)
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
            elif A_left > B_right:
                r = i - 1
            else:
                l = i + 1






print(Solution().findMedianSortedArrays([1, 3, 4, 5, 8], [2, 7, 9]))
