a = list(map(int, input().split()))


def monotonic_count(x, y, curr_len, idx):
    if x >= y:
        curr_len += 1
    else:
        update_res(curr_len, idx)
        curr_len = 1
    return curr_len


def update_res(curr_len, idx):
    global res
    if curr_len > res[0]:
        res = curr_len, idx - curr_len, idx - 1


res = [1, [0, 0]]
l = 0
curr_len_max = 1
curr_len_min = 1
for i in range(1, len(a)):
    curr_len_max = monotonic_count(a[i], a[i - 1], curr_len_max, i)
    curr_len_min = monotonic_count(a[i - 1], a[i], curr_len_min, i)

update_res(curr_len_max, len(a))
update_res(curr_len_min, len(a))
print(*res)
