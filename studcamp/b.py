from collections import defaultdict


def is_palindrome(s):
    return s == s[::-1]


def find_palindromic_pairs(words):
    results = []
    word_to_indexes = defaultdict(list)

    for i, word in enumerate(words):
        rev_word = word[::-1]
        word_to_indexes[rev_word].append(i + 1)

    for i, word in enumerate(words):
        for j in range(len(word) + 1):
            prefix, suffix = word[:j], word[j:]
            if is_palindrome(prefix) and suffix in word_to_indexes:
                results.extend([(index, i + 1) for index in word_to_indexes[suffix] if index != i + 1])
            if is_palindrome(suffix) and prefix in word_to_indexes:
                results.extend([(i + 1, index) for index in word_to_indexes[prefix] if index != i + 1])

    return sorted(set(results))


n = int(input())
r = find_palindromic_pairs([input() for _ in range(n)])

for i, j in r:
    print(i, j)
