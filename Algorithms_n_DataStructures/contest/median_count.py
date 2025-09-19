n, b = map(int, input().split())

a = list(map(int, input().split()))

pos = a.index(b)

count = 0
balance = 0
balance_counter = {0: 1}

for i in range(n):

    if a[i] > b:
        balance += 1
    elif a[i] < b:
        balance -= 1

    if i >= pos:
        if balance in balance_counter:
            count += balance_counter[balance]

    else:
        if balance in balance_counter:
            balance_counter[balance] += 1
        else:
            balance_counter[balance] = 1

print(count)