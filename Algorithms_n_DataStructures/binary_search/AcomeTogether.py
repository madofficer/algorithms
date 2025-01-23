n = int(input())

people = [list(map(int, input().split())) for _ in range(n)]


def ok(t: int) -> bool:
    max_L = float("-inf")
    min_R = float("inf")
    for i in range(n):
        max_L = max(people[i][0] - t * people[i][1], max_L)
        min_R = min(people[i][0] + t * people[i][1], min_R)
    return max_L <= min_R


l = 0
r = 10**9
ans = 0

for i in range(200):
    mid = (l + r) / 2

    if ok(mid):
        r = mid
        ans = r
    else:

        l = mid

print(ans)
