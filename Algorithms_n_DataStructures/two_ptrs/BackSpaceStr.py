class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1

        backspacesS, backspacesT = 0, 0

        while i >= 0 or j >= 0:

            while i >= 0:

                if s[i] != "#":

                    if backspacesS > 0:
                        i -= 1
                        backspacesS -= 1
                    else:
                        break

                else:
                    backspacesS += 1
                    i -= 1

            while j >= 0:

                if t[j] != "#":

                    if backspacesT > 0:
                        j -= 1
                        backspacesT -= 1
                    else:
                        break
                else:
                    backspacesT += 1
                    j -= 1

            if i < 0 and j < 0:
                return True

            if i < 0 or j < 0:
                return False

            if s[i] != t[j]:
                return False

            i -= 1
            j -= 1

        return True


print(Solution().backspaceCompare("ab#c", "ad#c#c"))
