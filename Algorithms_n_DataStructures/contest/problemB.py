N = int(input())
Q = list(map(int, input().split()))
C = list(map(int, input().split()))
A, B = map(int, input().split())

if A == B:
    D = [A] * N
else:
    D = [A + (C_i * (B - A)) / 255 for C_i in C]

dot_product = sum(Q_i * D_i for Q_i, D_i in zip(Q, D))
print(int(dot_product))