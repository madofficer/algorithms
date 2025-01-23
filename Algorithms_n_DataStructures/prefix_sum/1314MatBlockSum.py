from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        prefix_sum = [[0] * n for _ in range(m)]
        prefix_sum[0][0] = mat[0][0]

        for i in range(1, n):
            prefix_sum[0][i] = prefix_sum[0][i - 1] + mat[0][i]
        for j in range(1, m):
            prefix_sum[j][0] = prefix_sum[j - 1][0] + mat[j][0]

        for i in range(1, m):
            for j in range(1, n):
                prefix_sum[i][j] = (
                    prefix_sum[i - 1][j]
                    + prefix_sum[i][j - 1]
                    - prefix_sum[i - 1][j - 1]
                    + mat[i][j]
                )

        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                top = max(i - k, 0)
                left = max(j - k, 0)
                bottom = min(i + k, m - 1)
                right = min(j + k, n - 1)
                res[i][j] = prefix_sum[bottom][right]
                if top > 0:
                    res[i][j] -= prefix_sum[top - 1][right]

                if left > 0:
                    res[i][j] -= prefix_sum[bottom][left - 1]

                if top > 0 and left > 0:
                    res[i][j] += prefix_sum[top - 1][left - 1]
        return res


for i in Solution().matrixBlockSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1):
    print(i)
