from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_control = {}
        res, counter = 0, 0
        n = len(fruits)
        l = 0
        for r in range(n):
            if fruits[r] not in fruit_control:
                fruit_control[fruits[r]] = 1
            else:
                fruit_control[fruits[r]] += 1

            while len(fruit_control) > 2 and l < r < n:
                if fruit_control[fruits[l]] > 0:
                    fruit_control[fruits[l]] -= 1
                if fruit_control[fruits[l]] == 0:
                    del fruit_control[fruits[l]]
                l += 1

            res = max(res, sum(fruit_control.values()))

        return res


print(Solution().totalFruit([1, 2, 3, 2, 2]))
