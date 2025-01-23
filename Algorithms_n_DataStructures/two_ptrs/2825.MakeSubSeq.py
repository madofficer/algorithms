class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n, m = len(str1), len(str2)

        alphabet = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k',
                    'k': 'l', 'l': 'm', 'n': 'o', 'o': 'p', 'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u', 'u': 'v',
                    'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': 'a'}
        i, j = 0, 0

        while i < n and j < m:
            if str1[i] == str2[j] or str2[j] == alphabet[str1[i]]:
                i += 1
                j += 1
            else:
                i += 1

            if j == m:
                return True
        return False


print(Solution().canMakeSubsequence("abc", "ad"))