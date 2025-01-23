MOD = 10**9 + 7

def count_interesting_sequences(s):
    n = len(s)
    result = 0
    last_zero_pair = -1

    for i in range(1, n):
        if s[i-1] == '0' and s[i] == '0':
            new_sequences = i - last_zero_pair
            result += new_sequences
            result %= MOD
            last_zero_pair = i

    return result

def main():
    C = int(input())
    for i in range(C):
        data = input()

    results = []

    for i in data:
        results.append(count_interesting_sequences(i))

    print(results)
if __name__ == "__main__":
    main()
