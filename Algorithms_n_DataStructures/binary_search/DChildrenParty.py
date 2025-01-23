m, n = map(int, input().split())

workers = [list(map(int, input().split())) for _ in range(n)]


def getCount(T: int, t: int, z: int, y: int) -> int:
    count = 0
    block = t * z + y
    countBlock = T // block
    count += countBlock * z
    count += min((T % block) // t, z)
    return count


l = 0
r = 10**18
T = 0

while l <= r:
    mid = (l + r) // 2

    res = 0
    for i in range(n):
        res += getCount(mid, workers[i][0], workers[i][1], workers[i][2])

    if res >= m:
        r = mid - 1
        T = mid
    else:
        l = mid + 1

print(T)

answ = []
for i in range(n):
    count = getCount(T, workers[i][0], workers[i][1], workers[i][2])
    answ.append(min(m, count))
    m -= count
    m = max(m, 0)

print(*answ)
