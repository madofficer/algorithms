N = int(input())

adjacency_matrix = [list(map(int, input().split())) for _ in range(N)]

sources = []
drains = []
vertices = [0] * N  # empty : 0
for i in range(N):
    for j in range(N):
        # source : 1
        if adjacency_matrix[i][j] == 1 and (
            vertices[i] == 1 or vertices[i] == 0
        ):  # if source or empty
            vertices[i] = 1

        elif adjacency_matrix[i][j] == 1 and vertices[i] == -1:
            vertices[i] = -7

        # drain : -1
        if adjacency_matrix[j][i] == 1 and (
            vertices[i] == -1 or vertices[i] == 0
        ):  # if drain or empty
            vertices[i] = -1

        elif adjacency_matrix[j][i] == 1 and vertices[i] == 1:
            vertices[i] = -7

for i, val in enumerate(vertices):
    if val == 1:
        sources.append(i + 1)
    elif val == 0:
        sources.append(i + 1)
        drains.append(i + 1)
    elif val == -1:
        drains.append(i + 1)

print(len(sources), *sources)
print(len(drains), *drains)
