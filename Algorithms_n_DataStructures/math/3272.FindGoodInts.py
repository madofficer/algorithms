from collections import Counter
from math import factorial


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        ans = 0
        if n == 1:
            for i in range(1, 10):
                if i % k == 0:
                    ans += 1
        elif n == 2:
            for i in range(11, 100, 11):
                if i % k == 0:
                    ans += 1

        else:
            prefix_fac = [factorial(i) for i in range(n + 1)]
            visited = set()
            symm = n & 1
            m = 10 ** ((n - 1) // 2)
            for i in range(m, m * 10):
                num = str(i)
                num += num[::-1][symm:]
                if int(num) % k == 0:
                    visited.add("".join(sorted(num)))

            for s in visited:
                cnt = [0] * 10
                for c in s:
                    cnt[int(c)] += 1

                tot = (n - cnt[0]) * prefix_fac[n - 1]
                for x in cnt:
                    tot //= prefix_fac[x]
                ans += tot
        return ans


print(Solution().countGoodIntegers(3, 5))