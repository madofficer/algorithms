import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve
from numba import jit
import time

# ==================== Параметры модели ====================
L = 1.0  # Длина области (м)
Nx = 150  # Число узлов по пространству (уменьшено для скорости)
Tm = 0.0  # Температура плавления (°C)
T_left = -20.0  # Температура слева (°C)
T_right = 10.0  # Температура справа (°C)
sim_time = 300.0  # Общее время моделирования (сек)
output_interval = 0.5  # Интервал сохранения кадров (сек)


# Теплофизические свойства (лёд/вода)
def thermal_conductivity(T):
    """Теплопроводность с плавным переходом между фазами"""
    return np.where(T <= Tm, 2.2 * (1 + 0.01 * (T - Tm)), 0.56 * (1 + 0.001 * (T - Tm)))


def heat_capacity(T):
    """Теплоёмкость с пиком вблизи точки плавления"""
    delta_T = 1.0
    return np.where(T < Tm - delta_T, 2100,
                    np.where(T > Tm + delta_T, 4200,
                             3150 + 1050 * np.sin((T - Tm) / delta_T * np.pi / 2)))


rho_ice = 917  # Плотность льда (кг/м³)
rho_water = 1000  # Плотность воды (кг/м³)
Lh = 334000  # Удельная теплота плавления (Дж/кг)

# ==================== Инициализация ====================
x = np.linspace(0, L, Nx)
dx = x[1] - x[0]

# Начальное распределение температуры
U = np.linspace(T_left, T_right, Nx)
s_pos = L / 2
s_idx = np.argmin(np.abs(x - s_pos))
U[:s_idx] = np.linspace(T_left, Tm, s_idx)
U[s_idx:] = np.linspace(Tm, T_right, Nx - s_idx)

# Массивы для хранения результатов
U_history = [U.copy()]
front_positions = [s_pos]
front_velocities = [0.0]
times = [0.0]
next_output_time = output_interval


# ==================== Функции для ускорения ====================
@jit(nopython=True)
def find_front_position(U, x, Tm):
    """Быстрый поиск положения фронта с линейной интерполяцией"""
    for i in range(len(U) - 1):
        if (U[i] - Tm) * (U[i + 1] - Tm) <= 0:
            weight = (Tm - U[i]) / (U[i + 1] - U[i])
            return x[i] + weight * (x[i + 1] - x[i])
    return x[len(U) // 2]


# ==================== Главный цикл ====================
start_time = time.time()
current_time = 0.0
dt = 0.1  # Начальный шаг по времени

while current_time < sim_time:
    # 1. Определяем теплофизические параметры
    k = thermal_conductivity(U)
    cp = heat_capacity(U)
    rho = np.where(U <= Tm, rho_ice, rho_water)
    alpha = k / (rho * cp)

    # 2. Строим и решаем систему уравнений
    diagonals = np.zeros((3, Nx))
    diagonals[1, :] = 1 / dt + 2 * alpha / dx ** 2
    diagonals[0, 1:] = -alpha[:-1] / dx ** 2
    diagonals[2, :-1] = -alpha[1:] / dx ** 2

    # Граничные условия
    diagonals[1, 0] = 1.0
    diagonals[0, 0] = 0.0
    diagonals[1, -1] = 1.0
    diagonals[2, -1] = 0.0

    A = diags(diagonals, [0, 1, -1], format='csc')
    b = U.copy()
    b[0], b[-1] = T_left, T_right

    U_new = spsolve(A, b)

    # 3. Находим новое положение фронта
    s_pos_new = find_front_position(U_new, x, Tm)
    s_idx = np.argmin(np.abs(x - s_pos_new))

    # 4. Расчёт скорости фронта (условие Стефана)
    if 1 < s_idx < Nx - 2:
        dT_left = (U_new[s_idx] - U_new[s_idx - 1]) / dx
        dT_right = (U_new[s_idx + 1] - U_new[s_idx]) / dx
        k_left = thermal_conductivity(Tm - 0.1)
        k_right = thermal_conductivity(Tm + 0.1)
        ds_dt = (k_left * dT_left - k_right * dT_right) / (rho_ice * Lh)
    else:
        ds_dt = 0.0

    # 5. Адаптивный шаг по времени
    max_dt = 0.5 * dx / (np.max(alpha) + 1e-6)
    dt = min(0.1, max_dt, sim_time - current_time)

    # 6. Сохранение результатов
    current_time += dt
    U = U_new.copy()
    s_pos = s_pos_new

    if current_time >= next_output_time:
        U_history.append(U.copy())
        front_positions.append(s_pos)
        front_velocities.append(ds_dt)
        times.append(current_time)
        next_output_time += output_interval
        print(f"Time: {current_time:.1f}s, Front pos: {s_pos:.3f}m")

# ==================== Визуализация ====================
print(f"Calculation time: {time.time() - start_time:.2f} seconds")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), height_ratios=[3, 1])

# Настройка графиков
ax1.set_xlim(0, L)
ax1.set_ylim(T_left - 2, T_right + 2)
ax1.set_ylabel('Temperature (°C)')
ax1.grid(True)
line, = ax1.plot([], [], 'b-', lw=2, label='Temperature')
front_line = ax1.axvline(0, color='r', linestyle='--', label='Phase front')

ax2.set_xlim(0, sim_time)
ax2.set_ylim(0, L)
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Front position (m)')
ax2.grid(True)
ax2_twin = ax2.twinx()
ax2_twin.set_ylabel('Front velocity (m/s)', color='m')
pos_line, = ax2.plot([], [], 'g-', lw=2, label='Position')
vel_line, = ax2_twin.plot([], [], 'm--', lw=2, label='Velocity')


def init():
    line.set_data([], [])
    front_line.set_xdata([0, 0])
    pos_line.set_data([], [])
    vel_line.set_data([], [])
    return line, front_line, pos_line, vel_line


def animate(i):
    line.set_data(x, U_history[i])
    front_line.set_xdata([front_positions[i], front_positions[i]])

    # Обрезаем массивы до текущего кадра
    t = times[:i + 1]
    pos = front_positions[:i + 1]
    vel = front_velocities[:i + 1]

    pos_line.set_data(t, pos)
    vel_line.set_data(t, vel)
    ax2.set_ylim(0, max(1.0, max(pos) * 1.1))
    ax2_twin.set_ylim(min(-0.01, min(vel) * 1.1), max(0.01, max(vel) * 1.1))

    return line, front_line, pos_line, vel_line


ani = FuncAnimation(fig, animate, frames=len(U_history),
                    init_func=init, blit=False, interval=50)

plt.tight_layout()
plt.show()