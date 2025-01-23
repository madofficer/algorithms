from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        l = len(s)
        prefix = [0] * (l + 1)

        for start, end, d in shifts:
            if d == 1:
                prefix[start] += 1
                prefix[end + 1] -= 1
            else:
                prefix[start] -= 1
                prefix[end + 1] += 1
        for i in range(1, l):
            prefix[i] += prefix[i - 1]

        transform = lambda c, i: chr((ord(c) - ord("a") + prefix[i]) % 26 + ord("a"))
        return "".join(transform(c, i) for i, c in enumerate(s))


print(Solution().shiftingLetters("abc", [[0, 1, 0], [1, 2, 1], [0, 2, 1]]))
