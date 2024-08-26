from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        m = len(queries)

        nums.sort()

        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]

        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        res = []
        for i in range(m):
            ans = 0
            l = 0
            r = n - 1
            while l <= r:
                mid = (l + r) // 2

                if prefix_sum[mid] <= queries[i]:
                    l = mid + 1
                    ans = mid + 1
                else:
                    r = mid - 1
            res.append(ans)
        return res


print(Solution().answerQueries([2, 3, 4, 5], [1]))
