N = int(input())
adjacency_matrix = [list(map(int, input().split())) for _ in range(N)]
_ = input()
colors = list(map(int, input().split()))
res = 0
for i in range(N):

    for j in range(i + 1, N):

        if adjacency_matrix[i][j] and colors[i] != colors[j]:
            res += 1

print(res)