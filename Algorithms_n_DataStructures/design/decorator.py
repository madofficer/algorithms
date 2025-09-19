import functools
import time


def func_timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Wrapper started')
        start_t = time.perf_counter()
        res = func(*args, **kwargs)
        end_t = time.perf_counter()
        print(f'Exec time:{end_t - start_t}')
        return res

    return wrapper


@func_timer
def foo(n: int) -> int:
    """
    foo docstring
    :param n: number
    :return: factorial of n
    """
    res = 1
    for i in range(1, n):
        res *= i

    return res


print(foo(5))

def res_decorator(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f'Результат функции: ')
        return res
    return wrapper

@res_decorator
def a_plus_b(a, b):
    return a + b

def result_accumulator(func):
    q = []
    def wrapper(*args, method, **kwargs):
        if method == "accumulate":
            q.append(func(*args, **kwargs))
        elif method == "drop":
            res = q
            q.clear()
            return res
    return wrapper


print(a_plus_b(1, 2))

@result_accumulator
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5, 'accumulate'))