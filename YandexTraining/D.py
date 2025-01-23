n = int(input())
wonder_table = {}

for i in range(n):
    num = input()[1:4]
    pairs = [num[:2], num[1:3]]

    if pairs[0] != pairs[1]:

        for pair in pairs:
            if pair in wonder_table:
                wonder_table[pair][1] += wonder_table[pair][0]
                wonder_table[pair][0] += 1
            else:
                wonder_table[pair] = [1, 0]
    else:
        if pairs[0] in wonder_table:
            wonder_table[pairs[0]][1] += wonder_table[pairs[0]][0] * 2
            wonder_table[pairs[0]][0] += 2
        else:
            wonder_table[pairs[0]] = [2, 0]

ans = 0
for val in wonder_table.values():
    ans += val[1]
print(ans)
