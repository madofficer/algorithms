n, k, d = [int(x) for x in input().split()]

for i in range(10):
    if (10 * n + i) % k == 0:
        print(str(10 * n + i) + '0' * (d - 1))
        break
else:
    print(-1)
