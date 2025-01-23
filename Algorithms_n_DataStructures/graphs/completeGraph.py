N, M = map(int, input().split())

edges_num = len(set([tuple(map(int, input().split())) for _ in range(M)]))

print("YES" if N * (N - 1) / 2 == edges_num else "NO")
