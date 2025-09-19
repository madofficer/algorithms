import bisect
import array


class TrieNode:
    def __init__(self):
        self.children = {}
        self.indexes_of_words = array.array('I')
        self.is_end = False
        self.index_end = float('inf')


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, index_of_word):
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
            current.indexes_of_words.append(index_of_word)
        current.is_end = True
        if index_of_word < current.index_end:
            current.index_end = index_of_word

    def search_index(self, query):
        current = self.root
        for ch in query:
            if ch not in current.children:
                return -1
            current = current.children[ch]
        return current.index_end if current.is_end else -1

    def commmon_prefix(self, query, current_word_index):
        current = self.root
        actions = 0
        for ch in query:
            if ch not in current.children:
                break
            current = current.children[ch]
            if current_word_index == -1:
                actions += len(current.indexes_of_words)
            else:
                count = bisect.bisect_left(current.indexes_of_words, current_word_index + 1)
                actions += count
        return actions


n = int(input())
trie = Trie()
for i in range(n):
    word = input().strip()
    trie.insert(word, i)

q = int(input())
results = []
for _ in range(q):
    query = input().strip()
    idx = trie.search_index(query)
    word_actions = n if idx == -1 else idx + 1
    lcp_actions = trie.commmon_prefix(query, idx)
    results.append(word_actions + lcp_actions)

print('\n'.join(map(str, results)))


