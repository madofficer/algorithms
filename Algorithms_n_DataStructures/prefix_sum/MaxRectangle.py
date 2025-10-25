from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        # precompute current heights, leftmost and rightmost borders of rectangles
        heights = [[0] * cols for _ in range(rows + 1)]
        left_borders = [[0] * cols for _ in range(rows + 1)]
        right_borders = [[cols - 1] * cols for _ in range(rows + 1)]

        for r in range(1, rows + 1):
            lb, rb = 0, cols - 1
            for c in range(cols):
                # forward
                if matrix[r - 1][c] == "1":
                    heights[r][c] = heights[r - 1][c] + 1
                    left_borders[r][c] = max(lb, left_borders[r - 1][c])
                else:
                    lb = c + 1

                # backward (from the top right to the bottom left corners)
                if matrix[r - 1][cols - c - 1] == "1":
                    right_borders[r][cols - c - 1] = min(rb, right_borders[r - 1][cols - c - 1])
                else:
                    rb = cols - c - 2

        max_area = 0

        # calculate max area (r - l) * h
        for r in range(1, rows + 1):
            for c in range(cols):
                if matrix[r - 1][c] == "1":
                    max_area = max(max_area, (right_borders[r][c] - left_borders[r][c] + 1) * heights[r][c])

        return max_area


print(Solution().maximalRectangle(
    [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
