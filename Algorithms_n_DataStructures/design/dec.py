import functools
from time import perf_counter
from typing import Callable, List

def time_log(func: Callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Wrapper started")
        start = perf_counter()
        res = func(*args, **kwargs)
        finish = perf_counter()

        print(finish - start)
        print("Wrapper finished")
        return res

    return wrapper

# @time_log
def fibonacci(n: int) -> List[int]:
    fib = [0] * n
    fib[0], fib[1] = 0, 1
    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib

# print(fibonacci(100))

wrapped = time_log(fibonacci)
print(wrapped)
wrapped(10)


