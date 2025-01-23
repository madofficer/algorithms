from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        res = [10**5] * n
        l = 0

        curr_index = -1
        prev_index = -1

        for r in range(n):

            if s[r] == c:
                if curr_index != -1:
                    prev_index = curr_index
                curr_index = r
                res[r] = 0
            elif curr_index != -1:
                res[r] = abs(curr_index - r)

            while l <= r and s[r] == c:
                if prev_index != -1:
                    res[l] = min(abs(curr_index - l), abs(prev_index - l), res[l])
                else:
                    res[l] = min(abs(curr_index - l), res[l])
                l += 1

        return res


print(Solution().shortestToChar("aaba", "b"))
