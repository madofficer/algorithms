N, M = map(int, input().split())

adjacency_list = [0 for _ in range(N)]


for i in range(M):

    vertex1, vertex2 = map(int, input().split())

    adjacency_list[vertex1 - 1] += 1
    adjacency_list[vertex2 - 1] += 1

print(*adjacency_list)
