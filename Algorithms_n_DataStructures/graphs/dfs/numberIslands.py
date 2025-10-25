from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)  # rows y
        m = len(grid[0])  # columns x
        # visited = [[False] * m for _ in range(n)]
        counter = 0
        dx = (-1, 0, 0, 1)
        dy = (0, 1, -1, 0)

        def is_grid(x: int, y: int) -> bool:
            return 0 <= x < m and 0 <= y < n

        def dfs(x: int, y: int) -> None:
            if not is_grid(x, y) or grid[y][x] == "0":
                return

            grid[y][x] = "0"

            for to in range(4):
                dfs(x + dx[to], y + dy[to])

        for y in range(n):
            for x in range(m):
                if grid[y][x] == "1":
                    dfs(x, y)
                    counter += 1

        return counter


print(Solution().numIslands(
    [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
