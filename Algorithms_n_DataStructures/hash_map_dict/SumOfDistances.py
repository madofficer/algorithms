from typing import List


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        hash_map = {}

        for i, val in enumerate(nums):

            if val in hash_map:
                hash_map[val][0][i] = len(hash_map[val][0])
                hash_map[val][1].append(i + hash_map[val][1][-1])

            else:
                hash_map[val] = [{i: 0}, [0, i]]

        for key in hash_map:
            hash_map[key][1].append(0)
        print(hash_map)

        for i, val in enumerate(nums):
            n = len(hash_map[val][0])
            if n == 1:
                res[i] = 0

            else:
                index = hash_map[val][0][i]
                prefix = hash_map[val][1][index]
                suffix = hash_map[val][1][-2] - prefix - i
                res[i] = i * index - prefix + suffix - i * (n - 1 - index)

        return res


print(Solution().distance([0, 1, 4, 2, 1, 1, 9, 1]))
