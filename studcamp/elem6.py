from collections import Counter
_ = input()

counter = Counter(int(num) for num in input().split())
max_item, max_count = counter.most_common(1)[0]
for k, v in counter.items():
    if v == max_count:
        max_item = max(max_item, k)

print(max_item)

