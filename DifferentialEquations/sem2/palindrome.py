def is_palindrome(s: str) -> bool:
    n = int(s)
    ns = ""
    while n > 0:
        ns += str(n % 10)
        n //= 10
    print(s, ns)
    return s == ns


def add_to_palindrome(a: int):
    a = str(a)
    if is_palindrome(a):
        return a

    for i in range(len(a)):
        if is_palindrome(a[i:]):
            to_add = a[:i][::-1]
            output = a + to_add
            print(i)
            print(output)
            return int(output) - int(a), int(output)
    return 0


if __name__ == "__main__":
    print(add_to_palindrome(196))
