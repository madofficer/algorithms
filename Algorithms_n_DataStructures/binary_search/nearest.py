n = int(input())
a = list(map(int, input().split()))
x = int(input())
res = float("inf")
curr_dist = float("inf")
for i in a:
    if abs(i - x) < curr_dist:
        curr_dist = abs(i - x)
        res = i
print(res)
