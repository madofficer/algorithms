from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i, j = 0, n - 1
        res = []
        if n == 1:
            return [nums[0] ** 2]

        while i < n and j > - 1:
            while i < n and nums[i] < 0:
                i += 1
            while j > -1 and nums[j] >= 0:
                j -= 1

            if i == n or j == -1:
                break

            if nums[i] > -nums[j]:
                res.append(nums[j] ** 2)
                j -= 1
            else:
                res.append(nums[i] ** 2)
                i += 1

        while i < n:
            if nums[i] >= 0:
                res.append(nums[i] ** 2)
            i += 1

        while j > -1:
            if nums[j] < 0:
                res.append(nums[j] ** 2)
            j -= 1

        return res


print(Solution().sortedSquares([-2, -1, 0, 1, 5]))
