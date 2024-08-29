class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}

        for char in s:
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1

        for char in t:
            if char in hash_map:
                hash_map[char] -= 1
            else:
                return False

        return all(x == 0 for x in hash_map.values())


print(Solution().isAnagram("rat", "car"))