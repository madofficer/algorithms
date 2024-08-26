def fact(x: int) -> int:
    if x == 1:
        return 1
    return x * fact(x - 1)


print(fact(100))
