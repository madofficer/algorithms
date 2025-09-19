from typing import List
from collections import Counter


def digit_permutation(a: List) -> List[List[int]]:
    counters = {}

    for i in a:
        counter = Counter(str(i))
        if "0" in counter:
            del counter['0']
        key = str(sorted(counter.values()))
        if key in counters:
            counters[key].append(i)
        else:
            counters[key] = [i]
    print(a)
    a.clear()
    for val in counters.values():
        a.append(val)

    return a


print(digit_permutation([1230, 99, 23001, 123, 111, 300021, 101010, 90000009, 9]))
