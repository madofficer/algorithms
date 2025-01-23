from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        column = set()
        pos_diag = set()
        neg_diag = set()
        board = [['.'] * n for _ in range(n)]
        res = []


        def backtrack(row: int) -> None:
            if row == n:
                temp = ["".join(r) for r in board]
                res.append(temp)
                return

            for col in range(n):
                if col in column or row + col in pos_diag or row - col in neg_diag:
                    continue

                column.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)
                board[row][col] = 'Q'

                backtrack(row + 1)

                column.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)
                board[row][col] = '.'

        backtrack(0)
        return res


print(Solution().solveNQueens(8))