import matplotlib.pyplot as plt

def extract_step_and_result(filename):
    dh = None
    result = None
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("Integrate step:"):
                dh = float(line.split(":")[1].strip())
            elif line.startswith("Output Integral:"):
                result = float(line.split(":")[1].strip())
    if dh is None or result is None:
        raise ValueError(f"cant load data: {filename}")
    return dh, result

global_path = r'D:\Users\Boris\CLionProjects\ASM2\cmake-build-debug'
files = [r'\data1.txt', r'\data2.txt', r'\data3.txt']
files = [global_path + name for name in files]


steps = []
results = []

print(files)
for file in files:
    dh, result = extract_step_and_result(file)
    steps.append(dh)
    results.append(result)


plt.plot(steps, results, marker='o', label='Интеграл')
plt.xlabel('Step dh')
plt.ylabel('Integral val')
plt.title('Step Vs Val')
plt.xscale('log')  
plt.grid(True)
plt.legend()
plt.show()