N, M = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(M)]
edges_map = set()
if N * (N - 1) / 2 == len(edges):
    for vertex1, vertex2 in edges:

        if (vertex1, vertex2) in edges_map:
            print('NO')
            exit()
        else:
            edges_map.add((vertex1, vertex2))

        if (vertex2, vertex1) in edges:
            print('NO')
            exit()
    else:
        print('YES')
else:
    print('NO')
