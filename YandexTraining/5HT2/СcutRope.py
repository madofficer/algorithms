_ = int(input())
ropes = sorted(list(map(int, input().split())))

if ropes[-1] <= sum(ropes[:-1]):
    print(sum(ropes))
else:
    print(ropes[-1] - sum(ropes[:-1]))
