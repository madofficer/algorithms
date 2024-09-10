N = int(input())

adjacency_matix = [list(map(int, input().split())) for _ in range(N)]

res = float('inf')

for i in range(N):

    for j in range(i + 1, N):

        for k in range(j + 1, N):

            if adjacency_matix[i][j] and adjacency_matix[i][k] and adjacency_matix[j][k]:
                res = min(res, adjacency_matix[i][j] + adjacency_matix[i][k] + adjacency_matix[j][k])

print(res)