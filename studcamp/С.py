def count_hooks(n, k, ls):
    ls.append(1)
    hs = [ls[i] - ls[i + 1] + 1 for i in range(n)]

    l, r, s, c = 0, 0, 0, 0

    while r < n:
        if k - s <= hs[r]:
            if r == n - 1 or ls[r] - k + s >= ls[r + 1]:
                c += 1
            s -= hs[l]
            l += 1
        else:
            s += hs[r]
            r += 1

    return c

def main():
    n, k = map(int, input().split())
    ls = [int(input()) for _ in range(n)]
    print(count_hooks(n, k, ls))

if __name__ == "__main__":
    main()
