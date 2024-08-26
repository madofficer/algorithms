n = int(input())
a = list(map(int, input().split()))

i = 0
while a[i] % 2 == 0:
    i += 1
if all(x % 2 == 1 for x in a[i:]):
    print('+' * i + 'x' * (n - i - 1))
else:
    print('+' * (i + 1) + 'x' * (n - i - 2))
