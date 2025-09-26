from typing import List


class Solution:
    def is_reflected(self, points: List[List[int]]) -> bool:
        min_x = float("inf")
        max_x = float("-inf")

        visited = set()

        for x, y in points:
            min_x = min(x, min_x)
            max_x = max(x, max_x)
            visited.add((x, y))

        two_mid = min_x + max_x

        for x, y in points:
            reflected_point = two_mid - x
            if (reflected_point, y) not in visited:
                return False

        return True


print(Solution().is_reflected([[-3, 3], [-2, 5], [2, 5], [3, 3], [5, 4], [6, 5], [10, 5], [11, 3]]))
