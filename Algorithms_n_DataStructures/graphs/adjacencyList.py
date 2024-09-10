N = int(input())

adjacency_list = [list(map(int, input().split())) for _ in range(N)]
adjacency_matrix = [[0] * N for _ in range(N)]

for i, vertices in enumerate(adjacency_list):

    for vertex in vertices[1:]:
        adjacency_matrix[i][vertex - 1] = 1

print(N)

for i in adjacency_matrix:
    print(*i)
