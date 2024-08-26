k = int(input())

n = int(input())

students = sorted([int(input()) for _ in range(n)], reverse=True)


def ok(x) -> bool:
    s = 0
    for i in range(n):
        s += min(x, students[i])
    return x * k <= s


l = 0
r = sum(students) + 1
ans = 0
while l <= r:
    mid = (l + r) // 2

    if ok(mid):
        l = mid + 1
        ans = mid
    else:
        r = mid - 1

print(ans)
