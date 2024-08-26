n = int(input())

coords = [list(map(int, input().split())) for _ in range(n)]

chessboard = [[1 if [x, y] in coords else 0 for x in range(10)] for y in range(10)]

perimetr = 0
for y in range(1, 9):
    for x in range(1, 9):
        if chessboard[y][x] == 1:
            perimetr += (4 - sum([chessboard[y][x + 1], chessboard[y][x - 1], chessboard[y + 1][x],
                                  chessboard[y - 1][x]]))

print(perimetr)
