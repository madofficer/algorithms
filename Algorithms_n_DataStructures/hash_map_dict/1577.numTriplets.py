from typing import List


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        nums1_map = {}
        nums2_map = {}

        for i in range(m):
            if nums1[i] in nums1_map:
                nums1_map[nums1[i]] += 1

            else:
                nums1_map[nums1[i]] = 1

        for i in range(n):
            if nums2[i] in nums2_map:
                nums2_map[nums2[i]] += 1

            else:
                nums2_map[nums2[i]] = 1

        res = 0

        # nums1[i] * nums1[i] / nums2[k]

        for i in range(m):

            square = nums1[i] * nums1[i]

            for j in range(n):
                division = square / nums2[j]
                if division in nums2_map:
                    if nums2[j] == division and (nums2_map[nums2[j]] > 1):
                        res += nums2_map[nums2[j]] - 1
                    elif nums2[j] != (square / nums2[j]):
                        res += nums2_map[division]

        for i in range(n):

            square = nums2[i] * nums2[i]

            for j in range(m):
                division = square / nums1[j]
                if division in nums1_map:
                    if nums1[j] == division and (nums1_map[nums1[j]] > 1):
                        res += nums1_map[nums1[j]] - 1
                    elif nums1[j] != (square / nums1[j]):
                        res += nums1_map[division]

        return res // 2


print(Solution().numTriplets([3, 1, 2, 2], [1, 3, 4, 4]))
