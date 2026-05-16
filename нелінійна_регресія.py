import math
import numpy as np
import pandas as pd

x_values = [0, 1, 2, 3, 4, 5, 6]
y_values = [1, 10, 20, 25, 30, 44]

freq = [
    [45, 4, 5, 0, 0, 0, 0],
    [1, 4, 8, 10, 0, 0, 0],
    [0, 0, 7, 20, 0, 0, 0],
    [0, 0, 0, 1, 44, 0, 0],
    [0, 0, 0, 0, 3, 28, 0],
    [0, 0, 0, 0, 0, 15, 11]
]

n = sum(sum(row) for row in freq)
m_j = [sum(row) for row in freq]
n_i = [sum(freq[j][i] for j in range(len(y_values))) for i in range(len(x_values))]

y_mean = sum(y_values[j] * m_j[j] for j in range(len(y_values))) / n

print("Початкові дані:")
print("x_i =", x_values)
print("y_j =", y_values)
print("n_i =", n_i)
print("m_j =", m_j)
print("n =", n)
print(f"ȳ = {y_mean:.4f}")

Q_total_full = 0

print("\nОбчислення Q_total за всіма значеннями Y:")
for j in range(len(y_values)):
    diff = y_values[j] - y_mean
    term = m_j[j] * diff ** 2
    Q_total_full += term

    print(
        f"y = {y_values[j]}, "
        f"m_j = {m_j[j]}, "
        f"(y_j - ȳ)^2 = ({y_values[j]} - {y_mean:.4f})^2 = {diff ** 2:.6f}, "
        f"m_j(y_j - ȳ)^2 = {term:.6f}"
    )

D_total = Q_total_full / n

print("\nРезультати для повної варіації:")
print(f"Q_total = {Q_total_full:.4f}")
print(f"D_total = Q_total / n = {Q_total_full:.4f} / {n} = {D_total:.4f}")

y_x_mean = []

for i in range(len(x_values)):
    numerator = sum(freq[j][i] * y_values[j] for j in range(len(y_values)))
    y_mean_x = numerator / n_i[i]
    y_x_mean.append(y_mean_x)

print("\nУмовні середні:")
for i in range(len(x_values)):
    print(f"x = {x_values[i]}, n_i = {n_i[i]}, ȳ_xi = {y_x_mean[i]:.4f}")

Qp_emp = 0

print("\nОбчислення Qp_emp:")
for i in range(len(x_values)):
    diff = y_x_mean[i] - y_mean
    term = n_i[i] * diff ** 2
    Qp_emp += term

    print(
        f"x = {x_values[i]}, "
        f"n_i = {n_i[i]}, "
        f"ȳ_xi = {y_x_mean[i]:.4f}, "
        f"(ȳ_xi - ȳ)^2 = ({y_x_mean[i]:.4f} - {y_mean:.4f})^2 = {diff ** 2:.6f}, "
        f"n_i(ȳ_xi - ȳ)^2 = {term:.6f}"
    )

D_p = Qp_emp / n
eta = math.sqrt(D_p / D_total)
eta_squared = eta ** 2

print("\nРезультати для міжгрупової дисперсії:")
print(f"Qp_emp = {Qp_emp:.4f}")
print(f"D_p = Qp_emp / n = {Qp_emp:.4f} / {n} = {D_p:.4f}")
print(f"η = sqrt(D_p / D_total)")
print(f"η = sqrt({D_p:.4f} / {D_total:.4f}) = {eta:.4f}")
print(f"η² = {eta_squared:.4f}")

print("\nОбчислення коефіцієнта кореляції r:")

x_mean = sum(x_values[i] * n_i[i] for i in range(len(x_values))) / n

numerator_r = 0

for j in range(len(y_values)):
    for i in range(len(x_values)):
        numerator_r += freq[j][i] * (x_values[i] - x_mean) * (y_values[j] - y_mean)

sum_x_part = sum(n_i[i] * (x_values[i] - x_mean) ** 2 for i in range(len(x_values)))
sum_y_part = sum(m_j[j] * (y_values[j] - y_mean) ** 2 for j in range(len(y_values)))

r = numerator_r / math.sqrt(sum_x_part * sum_y_part)
r_squared = r ** 2
difference = eta_squared - r_squared

print(f"x̄ = {x_mean:.4f}")
print(f"r = {r:.4f}")
print(f"r² = {r_squared:.4f}")
print(f"η² - r² = {eta_squared:.4f} - {r_squared:.4f} = {difference:.4f}")

if difference > 0.1:
    print("\nВисновок:")
    print("Оскільки η² - r² > 0.1, лінійна модель недостатньо описує дані.")
    print("Тому доцільно будувати нелінійну регресію.")
else:
    print("\nВисновок:")
    print("Оскільки η² - r² <= 0.1, лінійна модель достатньо добре описує дані.")
    print("Але нижче все одно побудовано нелінійні моделі для повного аналізу.")

print("\n" + "=" * 70)
print("ПАРАБОЛІЧНА МОДЕЛЬ")
print("=" * 70)

sum_n = sum(n_i)
sum_nx = sum(n_i[i] * x_values[i] for i in range(len(x_values)))
sum_nx2 = sum(n_i[i] * x_values[i] ** 2 for i in range(len(x_values)))
sum_nx3 = sum(n_i[i] * x_values[i] ** 3 for i in range(len(x_values)))
sum_nx4 = sum(n_i[i] * x_values[i] ** 4 for i in range(len(x_values)))

sum_ny = sum(n_i[i] * y_x_mean[i] for i in range(len(x_values)))
sum_nxy = sum(n_i[i] * x_values[i] * y_x_mean[i] for i in range(len(x_values)))
sum_nx2y = sum(n_i[i] * x_values[i] ** 2 * y_x_mean[i] for i in range(len(x_values)))

print("\nПотрібні суми для параболічної моделі:")
print(f"Σ n_i = {sum_n}")
print(f"Σ n_i x_i = {sum_nx}")
print(f"Σ n_i x_i² = {sum_nx2}")
print(f"Σ n_i x_i³ = {sum_nx3}")
print(f"Σ n_i x_i⁴ = {sum_nx4}")
print(f"Σ n_i ȳ_xi = {sum_ny:.4f}")
print(f"Σ n_i x_i ȳ_xi = {sum_nxy:.4f}")
print(f"Σ n_i x_i² ȳ_xi = {sum_nx2y:.4f}")

A = np.array([
    [sum_nx4, sum_nx3, sum_nx2],
    [sum_nx3, sum_nx2, sum_nx],
    [sum_nx2, sum_nx, sum_n]
], dtype=float)

B = np.array([sum_nx2y, sum_nxy, sum_ny], dtype=float)

a_par, b_par, c_par = np.linalg.solve(A, B)

print("\nСистема нормальних рівнянь:")
print(f"{sum_nx4}a + {sum_nx3}b + {sum_nx2}c = {sum_nx2y:.4f}")
print(f"{sum_nx3}a + {sum_nx2}b + {sum_nx}c = {sum_nxy:.4f}")
print(f"{sum_nx2}a + {sum_nx}b + {sum_n}c = {sum_ny:.4f}")

print("\nРозв'язок системи:")
print(f"a = {a_par:.4f}")
print(f"b = {b_par:.4f}")
print(f"c = {c_par:.4f}")

print("\nРівняння параболічної регресії:")
print(f"y* = {a_par:.4f}x² + {b_par:.4f}x + {c_par:.4f}")

rows = []
Q_o_par = 0

for x, ni, y_emp in zip(x_values, n_i, y_x_mean):
    y_star = a_par * x ** 2 + b_par * x + c_par
    diff = y_emp - y_star
    weighted_square = ni * diff ** 2
    Q_o_par += weighted_square

    rows.append({
        "x_i": x,
        "n_i": ni,
        "ȳ_xi": y_emp,
        "y_i*": y_star,
        "ȳ_xi - y_i*": diff,
        "n_i(ȳ_xi - y_i*)²": weighted_square
    })

df_par = pd.DataFrame(rows)

print("\nТаблиця для обчислення залишкової варіації Q_o параболічної моделі:")
print(df_par.to_string(index=False, formatters={
    "ȳ_xi": "{:.4f}".format,
    "y_i*": "{:.4f}".format,
    "ȳ_xi - y_i*": "{:.4f}".format,
    "n_i(ȳ_xi - y_i*)²": "{:.4f}".format
}))

R2_par = 1 - Q_o_par / Qp_emp

print("\nЯкість параболічної моделі:")
print(f"Q_o = Σ n_i(ȳ_xi - y_i*)² = {Q_o_par:.4f}")
print("R² = 1 - Q_o / Q_total_emp")
print(f"R² = 1 - {Q_o_par:.4f} / {Qp_emp:.4f}")
print(f"R² = {R2_par:.4f}")

print("\nПеревірка адекватності параболічної моделі за F-критерієм Фішера:")

m = 3
alpha = 0.05
Q_p_par = Qp_emp - Q_o_par
F_emp_par = (Q_p_par * (n - m)) / (Q_o_par * (m - 1))
k1 = m - 1
k2 = n - m
F_crit = 3.04

print(f"Q_o = {Q_o_par:.4f}")
print(f"Q_total_emp = {Qp_emp:.4f}")
print(f"Q_p = Q_total_emp - Q_o = {Qp_emp:.4f} - {Q_o_par:.4f} = {Q_p_par:.4f}")
print("F_емп = Q_p(n - m) / (Q_o(m - 1))")
print(f"F_емп = {Q_p_par:.4f} * ({n} - {m}) / ({Q_o_par:.4f} * ({m} - 1))")
print(f"F_емп = {F_emp_par:.4f}")
print(f"k1 = {k1}")
print(f"k2 = {k2}")
print(f"F_кр = {F_crit:.2f}")

if F_emp_par > F_crit:
    print("Оскільки F_емп > F_кр, параболічна модель є статистично значущою.")
else:
    print("Оскільки F_емп <= F_кр, параболічна модель не є статистично значущою.")

print("\n" + "=" * 70)
print("КОРЕНЕВА МОДЕЛЬ")
print("=" * 70)

sqrt_x = [math.sqrt(x) for x in x_values]

sum_nz2 = sum(n_i[i] * sqrt_x[i] ** 2 for i in range(len(x_values)))
sum_nz = sum(n_i[i] * sqrt_x[i] for i in range(len(x_values)))
sum_n = sum(n_i)
sum_nyz = sum(n_i[i] * y_x_mean[i] * sqrt_x[i] for i in range(len(x_values)))
sum_ny = sum(n_i[i] * y_x_mean[i] for i in range(len(x_values)))

print("\nПотрібні суми для кореневої моделі y* = a√x + b:")
print(f"Σ n_i z_i² = {sum_nz2:.4f}")
print(f"Σ n_i z_i = {sum_nz:.4f}")
print(f"Σ n_i = {sum_n}")
print(f"Σ n_i ȳ_xi z_i = {sum_nyz:.4f}")
print(f"Σ n_i ȳ_xi = {sum_ny:.4f}")

A = np.array([
    [sum_nz2, sum_nz],
    [sum_nz, sum_n]
], dtype=float)

B = np.array([sum_nyz, sum_ny], dtype=float)

a_root, b_root = np.linalg.solve(A, B)

print("\nСистема нормальних рівнянь:")
print(f"{sum_nz2:.4f}a + {sum_nz:.4f}b = {sum_nyz:.4f}")
print(f"{sum_nz:.4f}a + {sum_n}b = {sum_ny:.4f}")

print("\nРозв'язок системи:")
print(f"a = {a_root:.4f}")
print(f"b = {b_root:.4f}")

print("\nРівняння кореневої регресії:")
print(f"y* = {a_root:.4f}√x + {b_root:.4f}")

rows = []
Q_o_root = 0

for x, ni, y_emp in zip(x_values, n_i, y_x_mean):
    y_star = a_root * math.sqrt(x) + b_root
    diff = y_emp - y_star
    weighted_square = ni * diff ** 2
    Q_o_root += weighted_square

    rows.append({
        "x_i": x,
        "n_i": ni,
        "ȳ_xi": y_emp,
        "y_i*": y_star,
        "ȳ_xi - y_i*": diff,
        "n_i(ȳ_xi - y_i*)²": weighted_square
    })

df_root = pd.DataFrame(rows)

print("\nТаблиця для обчислення залишкової варіації Q_o кореневої моделі:")
print(df_root.to_string(index=False, formatters={
    "ȳ_xi": "{:.4f}".format,
    "y_i*": "{:.4f}".format,
    "ȳ_xi - y_i*": "{:.4f}".format,
    "n_i(ȳ_xi - y_i*)²": "{:.4f}".format
}))

R2_root = 1 - Q_o_root / Qp_emp

print("\nЯкість кореневої моделі:")
print(f"Q_o = Σ n_i(ȳ_xi - y_i*)² = {Q_o_root:.4f}")
print("R² = 1 - Q_o / Q_total_emp")
print(f"R² = 1 - {Q_o_root:.4f} / {Qp_emp:.4f}")
print(f"R² = {R2_root:.4f}")

print("\nПорівняння моделей:")
print(f"Параболічна модель: Q_o = {Q_o_par:.4f}, R² = {R2_par:.4f}")
print(f"Коренева модель:     Q_o = {Q_o_root:.4f}, R² = {R2_root:.4f}")

if Q_o_par < Q_o_root:
    print("Кращою є параболічна модель, бо має менше Q_o і більше R².")
else:
    print("Кращою є коренева модель, бо має менше Q_o і більше R².")

print("\nПрогнозування за оптимальною параболічною моделлю:")

x_star = 3.5
y_star = a_par * x_star ** 2 + b_par * x_star + c_par

print(f"x* = {x_star}")
print(f"y* = {a_par:.4f} · {x_star}² + {b_par:.4f} · {x_star} + {c_par:.4f}")
print(f"y* = {y_star:.4f}")