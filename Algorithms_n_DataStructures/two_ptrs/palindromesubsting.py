class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def expand(left, right) -> int:
            while 0 <= left <= right < n and s[left] == s[right]:
                left -= 1
                right += 1

            return right - left - 1

        start, end = 0, 0
        # "babad"
        for i in range(n):
            odd = expand(i, i)
            if odd > end - start + 1:
                radius = odd // 2
                start, end = i - radius, i + radius

            even = expand(i, i + 1)
            if even > end - start + 1:
                radius = even // 2
                start, end = i - radius, i + radius + 1

        return s[start: end + 1]


print(Solution().longestPalindrome("babad"))
