n, k = map(int, input().split())  # n: num of vals; k: target value

a = list(map(int, input().split()))
hash_map = {}

l = 0
count = 0
for r in range(n):

    if a[r] in hash_map:
        hash_map[a[r]] += 1
    else:
        hash_map[a[r]] = 1

    while len(hash_map) > k:
        hash_map[a[l]] -= 1
        if hash_map[a[l]] == 0:
            del hash_map[a[l]]
        l += 1
    else:
        count += r - l + 1

print(count)
