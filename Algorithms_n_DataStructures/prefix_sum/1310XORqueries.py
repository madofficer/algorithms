from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = [arr[0]]
        for i in range(1, len(arr)):
            prefix_xor.append(prefix_xor[i - 1] ^ arr[i])
        res = []
        print(prefix_xor)
        for start, end in queries:
            if start == end:
                res.append(arr[start])
            elif start == 0 and end == len(prefix_xor) - 1:
                res.append(prefix_xor[-1])
            elif start == 0 and end > start:
                res.append(prefix_xor[end])
            elif start < end:
                res.append(prefix_xor[start - 1] ^ prefix_xor[end])
        return res


print(Solution().xorQueries([1, 11, 14, 10, 7], [[0, 2], [0, 0], [2, 3], [1, 4]]))
