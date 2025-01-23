from typing import List



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        vocab = {}
        for i in strs:
            counter = ''
            if counter in vocab:
                vocab[counter].append(i)
            else:
                vocab[counter] = [i]
        res = []
        for val in vocab.values():
            res.append(val)

        return res


print(Solution().groupAnagrams(["ddddddddddg", "dgggggggggg"]))
