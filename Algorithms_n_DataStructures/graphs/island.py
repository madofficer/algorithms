from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _ in range(n)]

        dx = (-1, 0, 0, 1)
        dy = (0, 1, -1, 0)

        def is_grid(x: int, y: int) -> bool:
            return 0 <= x < m and 0 <= y < n

        def dfs(x: int, y: int) -> int:
            if not is_grid(x, y) or grid[y][x] == 0:
                return 1

            if visited[y][x]:
                return 0

            visited[y][x] = True

            perimeter = 0

            for to in range(4):
                perimeter += dfs(x + dx[to], y + dy[to])

            return perimeter

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return dfs(j, i)

        return 0


print(
    Solution().islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]])
)
