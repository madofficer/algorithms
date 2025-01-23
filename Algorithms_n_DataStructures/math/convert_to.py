def convert_to(number, base):
    digits = list(range(101))
    if base > len(digits):
        return None
    result = 0
    while number > 0:
        curr_digit = digits[number % base]
        result += curr_digit ** 2
        number //= base
    return result


def b_sorted(arr, b):
    return sorted(arr, key=lambda x: convert_to(x, b))


if __name__ == "__main__":
    n, b = map(int, input().split())
    a = list(map(int, input().split()))
    res = b_sorted(a, b)
    print(*res)
