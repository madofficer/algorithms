t = int(input())

a = []
for i in range(t):
    _ = input()
    a.append(list(map(int, input().split())))


def cut_list(l: list) -> None:
    cut = []
    idx = 0

    while idx < len(l):
        piece = []
        min_val = float('inf')
        for _ in range(l[idx]):
            if idx < len(l):
                min_val = min(min_val, l[idx])
                if l[idx] >= len(piece) + 1 and min_val >= len(piece) + 1:
                    piece.append(l[idx])
                else:
                    break
                idx += 1
        cut.append(len(piece))
    print(len(cut))
    print(*cut)


for i in a:
    cut_list(i)
