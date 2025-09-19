r, c = map(int, input().split())
crossword = [input() for _ in range(r)]
ans = 'z' * 21
for i in range(r):
    r_word = ''
    for j in range(c):
        if crossword[i][j] == '#':
            if len(r_word) > 1:
                ans = min(ans, r_word)
            r_word = ''
        else:
            r_word += crossword[i][j]

    if len(r_word) > 1:
        ans = min(ans, r_word)

for j in range(c):
    c_word = ''
    for i in range(r):
        if crossword[i][j] == '#':
            if len(c_word) > 1:
                ans = min(ans, c_word)
            c_word = ''
        else:
            c_word += crossword[i][j]

    if len(c_word) > 1:
        ans = min(ans, c_word)

print(ans)
