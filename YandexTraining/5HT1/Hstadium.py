L, x1, v1, x2, v2 = [int(x) for x in input().split()]

if v1 == 0 and v2 == 0:
    if x1 == x2 or x1 == L - x2:
        print("YES")
        print(0)
    else:
        print("NO")
elif x1 == x2 or x1 == L - x2:
    print("YES")
    print(0)
else:
    t = float('inf')
    if v1 - v2 != 0:
        d = 0
        if v1 - v2 > 0:
            dl = L
        else:
            dl = -L
        while (d - dl + x2 - x1) / (v1 - v2) > 0:
            d -= dl
        while (d + x2 - x1) / (v1 - v2) < 0:
            d += dl
        t = (d + x2 - x1) / (v1 - v2)
    if v1 + v2 != 0:
        d = 0
        if v1 + v2 > 0:
            dl = L
        else:
            dl = -L
        while (d - dl - x2 - x1) / (v1 + v2) > 0:
            d -= dl
        while (d - x2 - x1) / (v1 + v2) < 0:
            d += dl
        t = min(t, (d - x2 - x1) / (v1 + v2))
    print("YES")
    print(t)
