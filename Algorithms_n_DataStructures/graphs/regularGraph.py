N = int(input())

adjacency_matrix = [list(map(int, input().split())) for _ in range(N)]

degrees = [0] * N

for i in range(N):

    for j in range(i + 1, N):

        if adjacency_matrix[i][j] == 1:
            degrees[i] += 1
            degrees[j] += 1

print("YES" if len(set(degrees)) == 1 else "NO")
