from collections import Counter

recipe = Counter(input())

n = list(map(int, input().split()))

p = list(map(int, input().split()))
budget = int(input())

l = 0
r = 10**18
ans = 0
while l <= r:
    mid = (l + r) // 2

    need_b = mid * recipe["B"] - n[0]
    need_s = mid * recipe["S"] - n[1]
    need_c = mid * recipe["C"] - n[2]

    money = max(need_b, 0) * p[0] + max(need_s, 0) * p[1] + max(need_c, 0) * p[2]

    if money <= budget:
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)
