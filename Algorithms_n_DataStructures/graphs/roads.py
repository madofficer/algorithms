N = int(input())

adjacency_matrix = [list(map(int, input().split())) for _ in range(N)]

roads = 0
for i in range(N):

    for j in range(i + 1, N):

        if adjacency_matrix[i][j] == 1:
            roads += 1

print(roads)