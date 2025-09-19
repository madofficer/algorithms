class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        res = float('inf')
        white_counter = 0
        for r in range(len(blocks)):

            if blocks[r] == 'W':
                white_counter += 1

            if r - l + 1 > k:
                if blocks[l] == "W":
                    white_counter -= 1
                l += 1

            if r - l + 1 == k:
                res = min(res, white_counter)

        return res


print(Solution().minimumRecolors("WBWW", 2))