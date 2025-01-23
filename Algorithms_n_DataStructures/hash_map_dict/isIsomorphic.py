class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_map_s = {}
        hash_map_t = {}
        n = len(s)
        for i in range(n):
            if s[i] in hash_map_s:
                if hash_map_s[s[i]] != t[i]:
                    return False
            else:
                hash_map_s[s[i]] = t[i]

            if t[i] in hash_map_t:
                if hash_map_t[t[i]] != s[i]:
                    return False
            else:
                hash_map_t[t[i]] = s[i]

        return True


print(Solution().isIsomorphic("paper", "title"))
