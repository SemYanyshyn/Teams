import numpy as np
import matplotlib.pyplot as plt

# Дані
x_values = np.array([3, 5, 6, 9, 12, 14, 19], dtype=float)
y_x_mean = np.array([1.6600, 2.5694, 2.9516, 3.4464, 3.7600, 4.3714, 4.1429], dtype=float)

# Параметри лінійної регресії
a_linear = 0.1863
b_linear = 1.5881

# Параметри оптимальної параболічної моделі
a_parabola = -0.0139
b_parabola = 0.4558
c_parabola = 0.5618

# Значення x для плавних ліній
x_smooth = np.linspace(min(x_values), max(x_values), 300)

# Лінійна регресія
y_linear = a_linear * x_smooth + b_linear

# Параболічна регресія
y_parabola = a_parabola * x_smooth**2 + b_parabola * x_smooth + c_parabola

# Побудова графіка
plt.figure(figsize=(10, 6))

# 1. Поле кореляції
plt.scatter(x_values, y_x_mean, s=80, label="Поле кореляції")

# 2. Емпірична лінія регресії
plt.plot(x_values, y_x_mean, marker="o", label="Емпірична лінія регресії")

# 3. Лінійна регресія
plt.plot(
    x_smooth,
    y_linear,
    linestyle="--",
    label="Лінійна регресія: y = 0.1863x + 1.5881"
)

# 4. Оптимальна нелінійна параболічна крива
plt.plot(
    x_smooth,
    y_parabola,
    linewidth=2,
    label="Параболічна регресія: y = -0.0139x² + 0.4558x + 0.5618"
)

# Підписи точок
for x, y in zip(x_values, y_x_mean):
    plt.text(x, y + 0.08, f"({x:.0f}; {y:.2f})", ha="center")

# Оформлення
plt.title("Поле кореляції, емпірична лінія та регресійні моделі")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.legend()
plt.tight_layout()

# Показати графік
plt.show()