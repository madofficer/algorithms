chessboard = [[i for i in input()[:8]] for _ in range(8)]


def rook_attacks(y, x):
    for i in range(x):
        if chessboard[y][x - i - 1] in ('B', 'R'):
            break
        chessboard[y][x - i - 1] = 'X'
    for i in range(x + 1, 8):
        if chessboard[y][i] in ('B', 'R'):
            break
        chessboard[y][i] = 'X'
    for i in range(y + 1, 8):
        if chessboard[i][x] in ('B', 'R'):
            break
        chessboard[i][x] = 'X'
    for i in range(y):
        if chessboard[y - i - 1][x] in ('B', 'R'):
            break
        chessboard[y - i - 1][x] = 'X'


def bishop_attacks(y, x):
    i, j = 0, 0
    while (y - i + 1 > 0) and (x - j + 1 > 0):
        i += 1
        j += 1
        if (chessboard[y - i][x - j] in ('B', 'R')) or ((y - i) < 0 or (x - j) < 0):
            break
        chessboard[y - i][x - j] = 'X'
    i, j = 0, 0
    while (y - i + 1 > 1) and (x + j + 1 < 8):
        i += 1
        j += 1
        if (chessboard[y - i][x + j] in ('B', 'R')) or ((y - i) < 0 or (x + j) > 7):
            break
        chessboard[y - i][x + j] = 'X'
    i, j = 0, 0
    while (y + i + 1 < 8) and (x - j + 1 > 0):
        i += 1
        j += 1
        if (chessboard[y + i][x - j] in ('B', 'R')) or ((y + i) > 7 or (x - j) < 0):
            break
        chessboard[y + i][x - j] = 'X'
    i, j = 0, 0
    while (y + i + 1 < 8) and (x + j + 1 < 8):
        i += 1
        j += 1
        if (chessboard[y + i][x + j] in ('B', 'R')) or ((y + i) > 7 or (x + j) > 7):
            break
        chessboard[y + i][x + j] = 'X'


for i in range(8):
    for j in range(8):
        if chessboard[i][j] == 'R':
            rook_attacks(i, j)
        elif chessboard[i][j] == 'B':
            bishop_attacks(i, j)

count = 0
for i in chessboard:
    for j in i:
        if j in ('R', 'B', 'X'):
            count += 1
print(64 - count)
