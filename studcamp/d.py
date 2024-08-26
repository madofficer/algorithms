import pandas as pd
import torch
import numpy as np

# Функция для проверки слова в словаре
def check_in_dictionary(word, dictionary):
    return word in dictionary

# Функция для исправления опечаток в слове
def correct_spelling(word, dictionary):
    possible_corrections = []
    for dict_word in dictionary:
        if len(dict_word) == len(word):
            diff_count = sum(1 for a, b in zip(dict_word, word) if a != b)
            if diff_count <= 1:
                possible_corrections.append(dict_word)
    return possible_corrections

# Преобразование слова в вектор
def word_to_tensor(word, vocab):
    tensor = torch.zeros(len(word), dtype=torch.long)
    for i, char in enumerate(word):
        tensor[i] = vocab[char]
    return tensor

# Загрузка словаря
with open('../studcamp/dict.txt', 'r', encoding='utf-8') as f:
    dictionary = set(word.strip() for word in f.readlines())

# Загрузка списка запросов с ошибками
with open('../studcamp/queries.txt', 'r', encoding='utf-8') as f:
    queries = [word.strip() for word in f.readlines()]

# Создание словаря для кодирования символов
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
vocab = {char: idx for idx, char in enumerate(alphabet)}

results = []
for query in queries:
    corrections = correct_spelling(query, dictionary)
    if check_in_dictionary(query, dictionary):
        results.append(f'"{query}" 0')
    elif corrections:
        result_str = f'"{query}"'
        for correction in corrections:
            result_str += f' 1 "{correction}"'
        results.append(result_str)
    else:
        results.append(f'"{query}" 3+')

# Создание DataFrame и запись результатов в файл
df = pd.DataFrame(results, columns=['Результат проверки'])
df.to_csv('spell_check_results.txt', index=False, header=False)
