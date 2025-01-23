def main():
    n, m, k = map(int, input().split())

    class Coords:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    mine_field = [[0] * m for _ in range(n)]
    for i in range(k):
        coord = Coords(*map(int, input().split()))
        mine_field[coord.x - 1][coord.y - 1] = "*"

    def field(coord) -> bool:
        return 0 <= coord.x < n and 0 <= coord.y < m

    def mine_count(coord) -> int:
        res = 0
        dx = (-1, 0, 1, -1, 1, -1, 0, 1)
        dy = (1, 1, 1, 0, 0, -1, -1, -1)
        for i in range(8):
            c = Coords(coord.x + dx[i], coord.y + dy[i])
            if field(c):
                if mine_field[c.x][c.y] == "*":
                    res += 1
        return res

    for i in range(n):
        for j in range(m):
            curr_c = Coords(i, j)
            if mine_field[curr_c.x][curr_c.y] != "*":
                mine_field[curr_c.x][curr_c.y] = mine_count(curr_c)
        print(*mine_field[i])


if __name__ == "__main__":
    main()
