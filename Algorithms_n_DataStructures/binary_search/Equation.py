c = float(input())

l = 0

r = 10 ** 10
x = 0


for _ in range(1000):
    mid = (l + r) / 2

    if mid * mid + mid ** 0.5 <= c:
        l = mid + 1
        x = mid
    else:
        r = mid - 1

print(x)