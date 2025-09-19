import numpy as np
import matplotlib.pyplot as plt

class Tepl:
    def __init__(self, a, x1, x2, t):
        """
        Params:
            a (float): коэффициент теплопроводности
            x1 (float): начальная граница отрезка
            x2 (float): конечная граница отрезка
            t (float): конечное время моделирования
        """
        self.a = a
        self.x1 = x1
        self.x2 = x2
        self.t = t
        self.U = None
        self.x = None
        self.dx = None
        self.dt = None

    def set_initial_condition(self, B, Nx):
        """Инициализирует сетку и задает начальное условие U(x,0) = Bx²"""
        self.x = np.linspace(self.x1, self.x2, Nx)  #  сетка
        self.dx = (self.x2 - self.x1) / (Nx - 1)
        self.U = B * self.x**2  

        self.U[0] = 0  # Граничное условие при x=0

    def calc_temp(self, Nt):
        """Решение уравнения теплопроводности явной схемой"""
        if self.x is None:
            raise ValueError("Сначала вызовите set_initial_condition для инициализации сетки.")
        self.dt = self.t / Nt

        # Проверка устойчивости
        CFL = self.a**2 * self.dt / self.dx**2
        if CFL > 0.5:
            print(f"Схема неустойчива! CFL = {CFL:.2f} > 0.5")
            return
        
        # Временные шаги
        for _ in range(Nt):
            U_new = self.U.copy()
            for i in range(1, len(self.x) - 1):
                U_new[i] = self.U[i] + (self.a**2 * self.dt / self.dx**2) * (
                    self.U[i+1] - 2*self.U[i] + self.U[i-1]
                )
            self.U = U_new

    def plot_solution(self, B):
        """Визуализация решения"""
        plt.figure(figsize=(10, 6))
        plt.plot(self.x, self.U, 'r-', linewidth=2, label=f'Решение при t = {self.t}')
        plt.plot(self.x, B*self.x**2, 'k--', label='Начальное условие (t=0)')
        plt.xlabel('x', fontsize=12)
        plt.ylabel('U(x, t)', fontsize=12)
        plt.title('Распределение температуры', fontsize=14)
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.show()


if __name__ == "__main__":
    model = Tepl(a=1.0, x1=0.0, x2=5.0, t=1.0)
    model.set_initial_condition(B=1.0, Nx=100)  # Инициализация сетки и начального условия
    model.calc_temp(Nt=1000)  # Расчет температуры
    model.plot_solution(B=1.0)  # Визуализация