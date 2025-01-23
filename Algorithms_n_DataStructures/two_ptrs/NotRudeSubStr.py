n, c = map(int, input().split())

a = input()


max_length = 0
l = 0
a_count = 0
b_count = 0
rude_count = 0

for r in range(n):
    if a[r] == "a":
        a_count += 1
    elif a[r] == "b":
        b_count += 1
        rude_count += a_count

    while rude_count > c:
        if a[l] == "a":
            a_count -= 1
            rude_count -= b_count
        elif a[l] == "b":
            b_count -= 1
        l += 1
    else:
        max_length = max(max_length, r - l + 1)

print(max_length)
