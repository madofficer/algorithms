N, M = map(int, input().split())

adjacency_list = [[0, []] for _ in range(N)]

for i in range(M):

    vertex1, vertex2 = map(int, input().split())
    if len(adjacency_list[vertex1 - 1]) > 1:
        adjacency_list[vertex1 - 1][0] += 1
        adjacency_list[vertex1 - 1][1].append(vertex2)
    else:
        adjacency_list[vertex1 - 1][0] += 1
        adjacency_list[vertex1 - 1][1].append(vertex2)

print(N)

for i in adjacency_list:
    print(i[0], *sorted(i[1]))
