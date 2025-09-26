import numpy as np
import math

x1, y1 = 2.20293, 0.092872
x2, y2 = 2.50406, 0.165059

print(f'difx {x2 - x1}')
graph_tg = (y2 - y1) / (x2 - x1)
graph_angle_rad = math.atan(graph_tg)
graph_angle_deg = math.degrees(graph_angle_rad)

gamma, p0, ro0 = 1.41, 101325, 1.17666
v_s = np.sqrt(gamma * p0 / ro0)
v0 = 1041.27
M = v0 / v_s

mach_angle_rad = math.asin(1 / M)
mach_angle_deg = math.degrees(mach_angle_rad)
anal_tg = 1 / (np.sqrt(M ** 2 - 1))
alpha = np.sin(1 / 3) ** (-1)

print(f'Тангенс угла наклона (графический): {graph_tg}')
print(f'Угол наклона (графический): {graph_angle_deg:.2f}°')
print(f'Тангенс угла Маха (аналитический): {anal_tg}')
print(f'alpha: {alpha}')
