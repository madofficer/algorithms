class Solution:
    def toHex(self, num: int) -> str:
        digits = "0123456789abcdef"
        res = ""
        while num:
            res = digits[num % 16] + res
            num //= 16
        return res


print(Solution().toHex(-1))

