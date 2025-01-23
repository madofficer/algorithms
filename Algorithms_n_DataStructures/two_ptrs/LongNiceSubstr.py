class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        vocab = set(s)
        curr_vocab = {}
        l = 0
        res = ''
        curr_len = 0
        for r in range(len(s)):
            if s[r].lower() in vocab and s[r].upper() in vocab:
                if s[r] in curr_vocab:
                    curr_vocab[s[r]] += 1
                else:
                    curr_vocab[s[r]] = 1
                curr_len += 1

            else:
                curr_vocab[s[l]] -= 1
                curr_len -= 1
                if curr_vocab[s[l]] == 0:
                    del curr_vocab[s[l]]
                l += 1
            if curr_len > len(res):
                res = ''
                for i in range(l, r + 1):
                    res += s[i]
                    curr_len = 0

        return res

print(Solution().longestNiceSubstring("YazaAay"))