N = int(input())

adjacency_matrix = [list(map(int, input().split())) for _ in range(N)]
edges = 0
adjacency_list = []
for i in range(N):

    for j in range(N):

        if adjacency_matrix[i][j] == 1:
            edges += 1
            adjacency_list.append([i + 1, j + 1])

print(N, edges)

for i in adjacency_list:
    print(*i)