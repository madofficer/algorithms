def word_encode(word):
    code = ""
    for char in word:
        for drum, letters in drum_to_letters.items():
            if char in letters:
                code += str(drum) * (letters.index(char) + 1)
                break
    return code

drum_to_letters = {
    2: "ABC",
    3: "DEF",
    4: "GHI",
    5: "JKL",
    6: "MNO",
    7: "PQRS",
    8: "TUV",
    9: "WXYZ"
}

message = input()
n = int(input())
vocab = {}
for _ in range(n):
    word = input()
    word_code = word_encode(word)
    vocab[word] = word_code

dp = [None] * (len(message) + 1)
dp[0] = []

for i in range(len(message) + 1):
    if dp[i] is not None:
        for word, code in vocab.items():
            if message.startswith(code, i):
                if dp[i + len(code)] is None:
                    dp[i + len(code)] = []
                dp[i + len(code)].append(word)

result = []
current_length = len(message)
while current_length > 0:
    for word in dp[current_length]:
        result.append(word)
        current_length -= len(vocab[word])
        break

print(' '.join(result[::-1]))
