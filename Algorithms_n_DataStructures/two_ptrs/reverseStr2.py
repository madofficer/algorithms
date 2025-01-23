class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        if k >= n:
            return s[::-1]
        elif 2 * k > n > k:
            return s[:k + 1][::-1] + s[k + 1:]
        else:
            # s = list(s)
            res = ''
            for i in range(0, n, 2 * k):
                res += s[i:i + k][::-1] + s[i + k: i + 2 * k]
            idx = n - (n % (2 * k)) + 1
            return res

print(Solution().reverseStr("abcdefg", 2))