p, v = [int(x) for x in input().split()]
q, m = [int(y) for y in input().split()]

if ((p - v) <= (q - m) and (p + v) >= (q + m)) or ((q - m) <= (p - v) and (q + m) >= (p + v)):
    print(len(range(min(p - v, q - m), max(p + v, q + m) + 1)))
elif ((p - v) <= (q - m) <= (p + v) <= (q + m)) or ((q - m) <= (p - v) <= (q + m) <= (p + v)):
    print(len(range(min(p - v, q - m), max(p + v, q + m) + 1)))
elif ((p + v) <= (q - m)) or ((q + m) <= (p - v)):
    print(len(range(p - v, p + v + 1)) + len(range(q - m, q + m + 1)))
