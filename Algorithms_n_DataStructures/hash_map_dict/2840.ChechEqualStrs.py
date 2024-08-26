class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)
        letters1 = set(s1)
        letters2 = set(s2)
        if letters1 != letters2:
            return False

        else:
            vocab_even = {char: 0 for char in letters1}
            vocab_odd = vocab_even.copy()

            for i in range(0, n, 2):
                vocab_even[s1[i]] += 1
                vocab_even[s2[i]] -= 1

            if any(val != 0 for val in vocab_even.values()):
                return False

            for i in range(1, n, 2):
                vocab_odd[s1[i]] += 1
                vocab_odd[s2[i]] -= 1

            return all(val == 0 for val in vocab_odd.values())


print(Solution().checkStrings("abcdba", "cabdab"))
