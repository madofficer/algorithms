from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        vocab = {}

        for word in words:
            letters = frozenset(word)
            if letters in vocab.keys():
                vocab[letters] += 1
            else:
                vocab[letters] = 1

        res = 0
        for val in vocab.values():
            res += val * (val - 1) // 2
        return res


print(Solution().similarPairs(["aba", "aabb", "abcd", "bac", "aabc"]))
