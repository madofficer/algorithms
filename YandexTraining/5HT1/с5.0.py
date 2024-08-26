n = int(input())
t = [int(input()) for _ in range(n)]
count = 0
for i in t:
    if i >= 4:
        count += (i // 4)
        i %= 4
    match i:
        case 3:
            count += 2
        case 2:
            count += 2
        case 1:
            count += 1
        case 0:
            count += 0

print(count)
