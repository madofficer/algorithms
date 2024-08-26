t = input()
p = input()
a = [int(x) - 1 for x in input().split()]


def ok(i: int, string: str) -> bool:
    string = list(string)
    for j in a[:i]:
        string[j] = '*'
    pos = 0
    for c in p:
        try:
            idx = string.index(c, pos)
        except:
            return False
        pos = idx + 1
    return True


l, r = 0, len(a)
ans = 0
while l <= r:
    mid = (l + r) // 2
    if ok(mid, t):
        l = mid + 1
        ans = mid
    else:
        r = mid - 1
print(ans)
