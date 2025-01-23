from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        start = 0
        i = 0
        n = len(chars)
        if n == 1:
            return 1

        while i < len(chars):
            current = chars[i]
            counter = 1
            while i < n - 1 and current == chars[i + 1]:
                counter += 1
                i += 1
            if counter > 1:
                chars[start] = current
                counter_str = str(counter)
                chars[start + 1] = str(counter)
                for j in range(len(counter_str)):
                    chars[start + j + 1] = counter_str[j]
                start += len(counter_str)  + 1
                i = start if i < start else i + 1
            else:
                chars[start] = current
                i += 1
                start += 1
            if i == n:
                return start


print(Solution().compress(["a","a","b","b","c","c","c"]))
