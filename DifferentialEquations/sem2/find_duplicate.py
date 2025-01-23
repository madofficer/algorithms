def absolute_value(a):
    return (a * a) ** 0.5


def min_value(a, b):
    return (a + b - absolute_value(a - b)) / 2

def max_value(a, b):
    return (a + b + absolute_value(a - b)) / 2

def min_of_three(a, b, c):
    return min_value(min_value(a, b), c)

def max_of_three(a, b, c):
    return max_value(max_value(a, b), c)

def find_unique(n1, n2, n3):
    minimum = min_of_three(a, b, c)
    maximum = max_of_three(a, b, c)
    return -a - b - c + 2 * minimum + 2 * maximum

a = 7
b = 4
c = 7

result = find_unique(a, b, c)
print(f'Unique: {result}')
