vocab = set(input().split())

text = input().split()

l = max(map(len, vocab))

answ = []

for word in text:
    for i in range(min(len(word), l)):
        if word[:i + 1] in vocab:
            answ.append(word[:i + 1])
            break
    else:
        answ.append(word)

print(*answ)
