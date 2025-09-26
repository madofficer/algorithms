import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Circle

a = 2.5
u = 2.0

x = np.linspace(-10, 10, 500)
y = np.linspace(-10, 10, 500)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y


def complex_potential(z, u, a):
    return u * z + u * a ** 2 / z


def stream_function(z, u, a):
    W = complex_potential(z, u, a)
    return np.imag(W)


path_name = r"E:\kurs3\new_ans\results\preM_ball.csv"
# path_name = 'ansys_streamlines.csv'


# Чтение данных из ANSYS
with open(path_name, 'r') as f:
    lines = f.readlines()

header_line = None
for i, line in enumerate(lines):
    if 'X [' in line and 'Y [' in line and 'Velocity [' in line:
        header_line = i
        break

if header_line is None:
    raise ValueError("Не удалось найти строку с заголовками в файле ANSYS")

ansys_data = pd.read_csv(path_name, skiprows=header_line + 1, header=None)
ansys_data.columns = ['X', 'Y', 'Z', 'Velocity']
ansys_x = ansys_data['X'].values
ansys_y = ansys_data['Y'].values
ansys_z = ansys_x + 1j * ansys_y
ansys_psi = stream_function(ansys_z, u, a)


plt.figure(figsize=(16, 8))
plt.subplot(1, 2, 1)
from matplotlib.tri import Triangulation

for level in np.linspace(-10, 10, 21):
    plt.tricontour(ansys_data['X'], ansys_data['Y'], ansys_psi, levels=[level], colors='blue', linewidths=1)

plt.gca().add_patch(Circle((0, 0), a, color='red', alpha=0.3))
plt.xlabel('X [m]')
plt.ylabel('Y [m]')
plt.title('Streamlines from ANSYS Data')
plt.grid(True)
plt.axis('equal')

plt.subplot(1, 2, 2)
psi = stream_function(Z, u, a)
for level in np.linspace(-10, 10, 21):
    plt.contour(X, Y, psi, levels=[level], colors='blue', linewidths=1, alpha=0.7)
plt.gca().add_patch(Circle((0, 0), a, color='red', alpha=0.3))
plt.xlabel('X [m]')
plt.ylabel('Y [m]')
plt.title('Analytical Streamlines (from W(z))')
plt.grid(True)
plt.axis('equal')

plt.tight_layout()
plt.show()


def velocity_field(z, u, a):
    return u * (1 - a ** 2 / z ** 2)


def compare_velocities(x_points, y_points, ansys_velocities, u, a):
    results = []
    for x, y, v_ansys in zip(x_points, y_points, ansys_velocities):
        z = x + 1j * y
        if abs(z) < a:
            continue

        W_prime = velocity_field(z, u, a)
        vx = np.real(W_prime)
        vy = -np.imag(W_prime)
        v_analytical = np.sqrt(vx ** 2 + vy ** 2)

        difference = abs(v_analytical - v_ansys)
        relative_diff = difference / v_ansys * 100

        results.append({
            'x': x, 'y': y,
            'ANSYS Velocity': v_ansys,
            'Analytical Velocity': v_analytical,
            'Difference': difference,
            'Relative Difference (%)': relative_diff
        })

    return pd.DataFrame(results)


sample_points = ansys_data.iloc[::20]
comparison = compare_velocities(
    sample_points['X'].values,
    sample_points['Y'].values,
    sample_points['Velocity'].values,
    u, a
)

# Вывод результатов сравнения
print("\nVelocity Comparison at Sample Points:")
print(comparison.head(10))

print("\nComparison Statistics:")
print(f"Mean Absolute Difference: {comparison['Difference'].mean():.4f} m/s")
print(f"Max Absolute Difference: {comparison['Difference'].max():.4f} m/s")
print(f"Mean Relative Difference: {comparison['Relative Difference (%)'].mean():.2f}%")
print(f"Max Relative Difference: {comparison['Relative Difference (%)'].max():.2f}%")

first_x = sample_points['X'].values[0]
first_y = sample_points['Y'].values[0]
first_v_ansys = sample_points['Velocity'].values[0]

first_z = first_x + 1j * first_y
W_prime = velocity_field(first_z, u, a)
vx_first = np.real(W_prime)
vy_first = -np.imag(W_prime)
first_v_analytical = np.sqrt(vx_first ** 2 + vy_first ** 2)

print(f"ANSYS Velocity: {first_v_ansys:.4f} m/s")
print(f"Analytical Velocity: {first_v_analytical:.4f} m/s")
