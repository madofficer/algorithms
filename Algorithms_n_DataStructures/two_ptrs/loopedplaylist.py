n, p = map(int, input().split())
a = list(map(int, input().split()))

flag = False
total_mood = sum(a)
if p >= total_mood:

    loops = p // total_mood

    if p % total_mood == 0:
        print(1, loops * n)
        exit()
    else:
        p -= loops * total_mood
        flag = True

res = [0, float("inf")]
l = 0
mood = 0
a = 2 * a

for r in range(2 * n):
    mood += a[r]

    while mood >= p:
        tracks = r - l + 1
        if tracks < res[1]:
            res = [l, tracks]
        mood -= a[l]
        l += 1

res[0] += 1

if flag:
    res[1] += loops * n

print(*res)
