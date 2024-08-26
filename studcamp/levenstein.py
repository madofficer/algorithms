def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def find_closest_word(word, dictionary):
    min_distance = float('inf')
    closest_word = None

    for dict_word in dictionary:
        distance = levenshtein_distance(word, dict_word)
        if distance < min_distance:
            min_distance = distance
            closest_word = dict_word

    return closest_word, min_distance

def spell_check(dictionary_file, queries_file):
    with open(dictionary_file, 'r', encoding='utf-8') as f:
        dictionary = set(word.strip() for word in f.readlines())

    with open(queries_file, 'r', encoding='utf-8') as f:
        queries = [word.strip() for word in f.readlines()]

    results = []
    for query in queries:
        closest_word, min_distance = find_closest_word(query, dictionary)
        results.append((query, closest_word, min_distance))

    return results

dictionary_file = 'dict.txt'
queries_file = 'queries.txt'
results = spell_check(dictionary_file, queries_file)
for query, closest_word, min_distance in results:
    print(f'Query: {query}, Closest Word: {closest_word}, Distance: {min_distance}')
