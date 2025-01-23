from math import floor


class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 0:
            return 0
        else:
            x_n = x * 0.5
            x1 = x_n
            while True:
                x_n = 0.5 * (x_n + x / x_n)

                if abs(x_n - x1) < 1e-6:
                    break
                x1 = x_n
        return floor(x_n)


print(Solution().mySqrt(8))