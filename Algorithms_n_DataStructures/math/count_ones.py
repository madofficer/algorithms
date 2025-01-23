class Solution:
    def countDigitOne(self, n: int) -> int:
        n1 = n
        digit = n % 10
        res = 1 if digit > 0 else 0
        n //= 10
        power = 0

        while n > 0:
            digit = n % 10
            if digit > 1:
                res += digit * (power + 1) * (10 ** power) + 10 ** (power + 1)
            elif digit == 1:
                res += (power + 1) * 10 ** power + (n1 % (10 ** (power + 1))) + 1

            n //= 10
            power += 1

        return res

print(Solution().countDigitOne(124725))