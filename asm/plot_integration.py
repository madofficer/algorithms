import matplotlib.pyplot as plt

# Функция для извлечения шага dh и результата интеграла из файла
def extract_step_and_result(filename):
    dh = None
    result = None
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("Шаг интегрирования:"):
                dh = float(line.split(":")[1].strip())
            elif line.startswith("Итоговый интеграл:"):
                result = float(line.split(":")[1].strip())
    if dh is None or result is None:
        raise ValueError(f"Не удалось извлечь данные из файла: {filename}")
    return dh, result

# Файлы с результатами
global_path = r'D:\Users\Boris\CLionProjects\ASM2\cmake-build-debug'
files = [r'\accem2.2.txt', r'\accem2.2_small.txt', r'\accem2.2_smal.txt']
files = [global_path + name for name in files]


steps = []
results = []

print(files)
for file in files:
    dh, result = extract_step_and_result(file)
    steps.append(dh)
    results.append(result)


plt.plot(steps, results, marker='o', label='Интеграл')
plt.xlabel('Шаг dh')
plt.ylabel('Значение интеграла')
plt.title('Зависимость значения интеграла от шага')
plt.xscale('log')  
plt.grid(True)
plt.legend()
plt.show()