N = int(input())

adjacency_matrix = [list(map(int, input().split())) for _ in range(N)]

flag = True
for i in range(N):

    if adjacency_matrix[i][i]:
        print("NO")
        exit()

    for j in range(i + 1, N):

        if adjacency_matrix[i][j] != adjacency_matrix[j][i]:
            flag = False

print("NO" if flag else "YES")
