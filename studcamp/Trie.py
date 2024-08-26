class TrieNode:
    def __init__(self):
        self.children = {}
        self.pos = []
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, idx):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.pos.append(idx)

    def is_palindrome(self, s):
        return s == s[::-1]

    def find_palindromic_pairs(self, words):
        result = []
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i != j:
                    combined_word = word1 + word2
                    if self.is_palindrome(combined_word):
                        result.append((i, j))
        return result


def main():
    n = int(input())
    words = [input() for i in range(n)]

    trie = Trie()
    for idx, word in enumerate(words):
        trie.insert(word, idx)

    palindromic_pairs = trie.find_palindromic_pairs(words)

    if palindromic_pairs:
        for i, j in palindromic_pairs:
            print(i + 1, j + 1)


if __name__ == "__main__":
    main()