import math

# Значення Y
y_values = [1.5, 2.5, 3, 3.5, 4, 4.5]

# Кореляційна таблиця частот n_ij
# Рядки відповідають y_j, стовпці відповідають x_i
freq = [
    [21, 0, 0, 0, 0, 0, 0],
    [4, 31, 3, 0, 0, 0, 0],
    [0, 5, 28, 3, 4, 0, 0],
    [0, 0, 0, 25, 4, 3, 0],
    [0, 0, 0, 0, 17, 3, 5],
    [0, 0, 0, 0, 0, 29, 2]
]

# Загальна кількість спостережень
n = sum(sum(row) for row in freq)

# Частоти для кожного y_j
m_j = [sum(row) for row in freq]

# Середнє значення Y
y_mean = sum(y_values[j] * m_j[j] for j in range(len(y_values))) / n

# Повна варіація Qtotal
Q_total = 0

print("Обчислення Q_total:")
for j in range(len(y_values)):
    diff = y_values[j] - y_mean
    term = m_j[j] * diff ** 2
    Q_total += term

    print(
        f"y = {y_values[j]}, "
        f"m_j = {m_j[j]}, "
        f"(y_j - ȳ)^2 = ({y_values[j]} - {y_mean:.4f})^2 = {diff ** 2:.6f}, "
        f"m_j(y_j - ȳ)^2 = {term:.6f}"
    )

# Повна дисперсія Dtotal
D_total = Q_total / n

print("\nРезультати:")
print(f"n = {n}")
print(f"ȳ = {y_mean:.4f}")
print(f"Q_total = {Q_total:.4f}")
print(f"D_total = Q_total / n = {Q_total:.4f} / {n} = {D_total:.4f}")

# ----------------------------------------
# Доповнення: міжгрупова дисперсія за умовними середніми
# (блок, який ви надали, інтегровано так, щоб не дублювати значення)
# ----------------------------------------

# Нові значення X (з вашого блоку)
new_x_values = [3, 5, 6, 9, 12, 14, 19]

# Визначимо базовий порядок стовпців для freq (щоб зберегти відповідність колонок)
num_cols = len(freq[0]) if freq else 0

if 'x_values' in globals() and len(x_values) == num_cols:
    # якщо в файлі вже було визначено x_values і його довжина збігається з кількістю стовпців в freq,
    # вважаємо, що саме воно відповідає стовпцям таблиці частот
    base_col_x = x_values
else:
    # інакше використовуємо new_x_values як базовий порядок колонок
    base_col_x = new_x_values

# Побудуємо фінальний список x_values без дублікатів, зберігаючи порядок base_col_x спочатку
merged_x = []
for v in base_col_x + new_x_values:
    if v not in merged_x:
        merged_x.append(v)

# Якщо вже було x_values в модулі, об'єднаємо з merged_x уникнувши дублікації
if 'x_values' in globals():
    for v in x_values:
        if v not in merged_x:
            merged_x.append(v)

x_values = merged_x

# Використаємо існуючі y_values та freq (вони вже визначені вище)

# Загальна кількість спостережень (перерахувати для впевненості)
n = sum(sum(row) for row in freq)

# Частоти для кожного y_j
m_j = [sum(row) for row in freq]

# Середнє значення Y
y_mean = sum(y_values[j] * m_j[j] for j in range(len(y_values))) / n

# Частоти n_i для кожного x_i — враховуємо, що тільки ті x, які присутні в base_col_x, мають стовпці в freq
n_i = []
for x in x_values:
    if x in base_col_x:
        idx = base_col_x.index(x)
        n_i.append(sum(freq[j][idx] for j in range(len(y_values))))
    else:
        n_i.append(0)

# Умовні середні ȳ_xi (обчислюємо лише для тих n_i>0)
y_x_mean = []
for i, x in enumerate(x_values):
    if n_i[i] > 0:
        numerator = sum(freq[j][base_col_x.index(x)] * y_values[j] for j in range(len(y_values)))
        y_x_mean.append(numerator / n_i[i])
    else:
        y_x_mean.append(0.0)

# Обчислення Qp_emp
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

# Міжгрупова дисперсія Dp
D_p = Qp_emp / n if n != 0 else float('nan')

print("\nРезультати:")
print(f"n = {n}")
print(f"ȳ = {y_mean:.4f}")
print(f"Qp_emp = {Qp_emp:.4f}")
print(f"D_p = Qp_emp / n = {Qp_emp:.4f} / {n} = {D_p:.4f}")

# Обчислення кореляційного відношення η
eta = math.sqrt(D_p / D_total)

print(f"\nη = sqrt(D_p / D_total)")
print(f"η = sqrt({D_p:.4f} / {D_total:.4f})")
print(f"η = sqrt({D_p / D_total:.4f})")
print(f"η = {eta:.4f}")

eta_squared = eta ** 2

print(f"\nη² = {eta:.4f}² = {eta_squared:.4f}")

# Порівняння з коефіцієнтом кореляції Пірсона
r = 0.8973

r_squared = r ** 2

difference = eta_squared - r_squared

print(f"\nr = {r:.4f}")
print(f"r² = {r:.4f}² = {r_squared:.4f}")

print(f"\nη² - r² = {eta_squared:.4f} - {r_squared:.4f} = {difference:.4f}")

if difference > 0.1:
    print("\nВисновок:")
    print("Оскільки η² - r² > 0.1, лінійна модель недостатньо описує дані.")
    print("Тому доцільно будувати нелінійну регресію.")
else:
    print("\nВисновок:")
    print("Оскільки η² - r² <= 0.1, лінійна модель достатньо добре описує дані.")

# ----------------------------------------
# Блок: підготовка сум для параболічної моделі
# ----------------------------------------

# Значення X (впорядковані без дублікатів)
x_values = [3, 5, 6, 9, 12, 14, 19]

# Частоти та умовні середні (перераховуються відповідно до x_values)
n_i = []
y_x_mean = []

for i, x in enumerate(x_values):
    n_val = sum(freq[j][i] for j in range(len(y_values)))
    numerator = sum(freq[j][i] * y_values[j] for j in range(len(y_values)))
    y_mean_x = numerator / n_val if n_val != 0 else 0.0

    n_i.append(n_val)
    y_x_mean.append(y_mean_x)

sum_n = sum(n_i)
sum_nx = sum(n_i[i] * x_values[i] for i in range(len(x_values)))
sum_nx2 = sum(n_i[i] * x_values[i]**2 for i in range(len(x_values)))
sum_nx3 = sum(n_i[i] * x_values[i]**3 for i in range(len(x_values)))
sum_nx4 = sum(n_i[i] * x_values[i]**4 for i in range(len(x_values)))

sum_ny = sum(n_i[i] * y_x_mean[i] for i in range(len(x_values)))
sum_nxy = sum(n_i[i] * x_values[i] * y_x_mean[i] for i in range(len(x_values)))
sum_nx2y = sum(n_i[i] * x_values[i]**2 * y_x_mean[i] for i in range(len(x_values)))

print("\nПотрібні суми для параболічної моделі:")
print(f"Σ n_i = {sum_n}")
print(f"Σ n_i x_i = {sum_nx}")
print(f"Σ n_i x_i² = {sum_nx2}")
print(f"Σ n_i x_i³ = {sum_nx3}")
print(f"Σ n_i x_i⁴ = {sum_nx4}")
print(f"Σ n_i ȳ_xi = {sum_ny}")
print(f"Σ n_i x_i ȳ_xi = {sum_nxy}")
print(f"Σ n_i x_i² ȳ_xi = {sum_nx2y}")

import numpy as np
import pandas as pd

# Дані
x_values = [3, 5, 6, 9, 12, 14, 19]
n_i = [25, 36, 31, 28, 25, 35, 7]
y_x_mean = [1.6600, 2.5694, 2.9516, 3.4464, 3.7600, 4.3714, 4.1429]

# Матриця системи для параболічної моделі
A = np.array([
    [3023616, 219536, 17496],
    [219536, 17496, 1616],
    [17496, 1616, 187]
], dtype=float)

B = np.array([67789.5, 5825.5, 598], dtype=float)

# Розв'язання системи
a, b, c = np.linalg.solve(A, B)

print("Система нормальних рівнянь:")
print("3023616a + 219536b + 17496c = 67789.5")
print("219536a + 17496b + 1616c = 5825.5")
print("17496a + 1616b + 187c = 598")

print("\nРозв'язок системи:")
print(f"a = {a:.4f}")
print(f"b = {b:.4f}")
print(f"c = {c:.4f}")

print("\nРівняння параболічної регресії:")
print(f"y* = {a:.4f}x² + {b:.4f}x + {c:.4f}")

# Обчислення таблиці
rows = []
Q_o = 0

for x, n, y_emp in zip(x_values, n_i, y_x_mean):
    y_star = a * x**2 + b * x + c
    diff = y_emp - y_star
    weighted_square = n * diff**2
    Q_o += weighted_square

    rows.append({
        "x_i": x,
        "n_i": n,
        "ȳ_xi": y_emp,
        "y_i*": y_star,
        "ȳ_xi - y_i*": diff,
        "n_i(ȳ_xi - y_i*)²": weighted_square
    })

df = pd.DataFrame(rows)

# Округлення для гарного виводу
df_display = df.copy()
df_display["ȳ_xi"] = df_display["ȳ_xi"].map(lambda x: f"{x:.4f}")
df_display["y_i*"] = df_display["y_i*"].map(lambda x: f"{x:.4f}")
df_display["ȳ_xi - y_i*"] = df_display["ȳ_xi - y_i*"].map(lambda x: f"{x:.4f}")
df_display["n_i(ȳ_xi - y_i*)²"] = df_display["n_i(ȳ_xi - y_i*)²"].map(lambda x: f"{x:.4f}")

print("\nТаблиця для обчислення залишкової варіації Q_o:")
print(
    f"{'x_i':>4}  {'n_i':>4}  {'ȳ_xi':>8}  {'y_i*':>8}  {'ȳ_xi - y_i*':>12}  {'n_i(ȳ_xi - y_i*)²':>18}"
)
for row in df_display.itertuples(index=False):
    print(
        f"{row[0]:>4}  {row[1]:>4}  {row[2]:>8}  {row[3]:>8}  {row[4]:>12}  {row[5]:>18}"
    )

print("\nЗалишкова варіація параболічної моделі:")
print(f"Q_o = Σ n_i(ȳ_xi - y_i*)² = {Q_o:.4f}")

# ----------------------------------------
# Блок: гіперболічна модель регресії
# ----------------------------------------

import numpy as np

# Дані
x_values = [3, 5, 6, 9, 12, 14, 19]
n_i = [25, 36, 31, 28, 25, 35, 7]
y_x_mean = [1.6600, 2.5694, 2.9516, 3.4464, 3.7600, 4.3714, 4.1429]

# Обчислення потрібних сум
sum_n_div_x2 = sum(n / x**2 for x, n in zip(x_values, n_i))
sum_n_div_x = sum(n / x for x, n in zip(x_values, n_i))
sum_n = sum(n_i)
sum_ny_div_x = sum(n * y / x for x, n, y in zip(x_values, n_i, y_x_mean))
sum_ny = sum(n * y for n, y in zip(n_i, y_x_mean))

print("\nПотрібні суми для гіперболічної моделі:")
print(f"Σ n_i / x_i² = {sum_n_div_x2:.4f}")
print(f"Σ n_i / x_i = {sum_n_div_x:.4f}")
print(f"Σ n_i = {sum_n}")
print(f"Σ n_i ȳ_xi / x_i = {sum_ny_div_x:.4f}")
print(f"Σ n_i ȳ_xi = {sum_ny:.4f}")

# Система нормальних рівнянь
A = np.array([
    [sum_n_div_x2, sum_n_div_x],
    [sum_n_div_x, sum_n],
], dtype=float)

B = np.array([
    sum_ny_div_x,
    sum_ny,
], dtype=float)

# Розв'язання системи
a, b = np.linalg.solve(A, B)

print("\nСистема нормальних рівнянь:")
print(f"{sum_n_div_x2:.4f}a + {sum_n_div_x:.4f}b = {sum_ny_div_x:.4f}")
print(f"{sum_n_div_x:.4f}a + {sum_n}b = {sum_ny:.4f}")

print("\nРозв'язок системи:")
print(f"a = {a:.4f}")
print(f"b = {b:.4f}")

print("\nРівняння гіперболічної регресії:")
print(f"y* = {a:.4f} / x + {b:.4f}")

# ----------------------------------------
# Блок: таблиця залишків та R² для гіперболічної моделі
# ----------------------------------------

# Дані
x_values = [3, 5, 6, 9, 12, 14, 19]
n_i = [25, 36, 31, 28, 25, 35, 7]
y_x_mean = [1.6600, 2.5694, 2.9516, 3.4464, 3.7600, 4.3714, 4.1429]

# Параметри гіперболічної моделі
a = -9.7560
b = 4.6984

# Емпірична варіація
Q_total_emp = 139.3071

rows = []
Q_o = 0

for x, n, y_emp in zip(x_values, n_i, y_x_mean):
    y_star = a / x + b
    diff = y_emp - y_star
    weighted_square = n * diff ** 2
    Q_o += weighted_square

    rows.append({
        "x_i": x,
        "n_i": n,
        "ȳ_xi": y_emp,
        "y_i*": y_star,
        "ȳ_xi - y_i*": diff,
        "n_i(ȳ_xi - y_i*)²": weighted_square
    })

df = pd.DataFrame(rows)

# Гарний вивід таблиці
df_display = df.copy()
df_display["ȳ_xi"] = df_display["ȳ_xi"].map(lambda x: f"{x:.4f}")
df_display["y_i*"] = df_display["y_i*"].map(lambda x: f"{x:.4f}")
df_display["ȳ_xi - y_i*"] = df_display["ȳ_xi - y_i*"].map(lambda x: f"{x:.4f}")
df_display["n_i(ȳ_xi - y_i*)²"] = df_display["n_i(ȳ_xi - y_i*)²"].map(lambda x: f"{x:.4f}")

# R²
R_squared = 1 - Q_o / Q_total_emp

print("\nГіперболічна модель:")
print(f"y* = {a:.4f} / x + {b:.4f}")

print("\nТаблиця для обчислення залишкової варіації Q_o:")
print(df_display.to_string(index=False))

print("\nОбчислення Q_o:")
print(f"Q_o = Σ n_i(ȳ_xi - y_i*)² = {Q_o:.4f}")

print("\nОбчислення R²:")
print(f"R² = 1 - Q_o / Q_total_emp")
print(f"R² = 1 - {Q_o:.4f} / {Q_total_emp:.4f}")
print(f"R² = {R_squared:.4f}")

# Дані для оптимальної параболічної моделі
Q_o = 4.3735
Q_total_emp = 139.3071
n = 187
m = 3
alpha = 0.05

# Обчислення Qp
Q_p = Q_total_emp - Q_o

# Обчислення Fемп
F_emp = (Q_p * (n - m)) / (Q_o * (m - 1))

# Ступені свободи
k1 = m - 1
k2 = n - m

# Критичне значення F для alpha=0.05, k1=2, k2=184 з таблиці F-розподілу
F_crit = 3.05

print("\nПеревірка адекватності параболічної моделі за F-критерієм Фішера")
print()

print("Початкові дані:")
print(f"Q_o = {Q_o:.4f}")
print(f"Q_total_emp = {Q_total_emp:.4f}")
print(f"n = {n}")
print(f"m = {m}")
print(f"alpha = {alpha}")

print("\nОбчислення Q_p:")
print("Q_p = Q_total_emp - Q_o")
print(f"Q_p = {Q_total_emp:.4f} - {Q_o:.4f} = {Q_p:.4f}")

print("\nОбчислення F_емп:")
print("F_емп = Q_p(n - m) / (Q_o(m - 1))")
print(f"F_емп = {Q_p:.4f}({n} - {m}) / ({Q_o:.4f}({m} - 1))")
print(f"F_емп = {Q_p:.4f} * {n - m} / ({Q_o:.4f} * {m - 1})")
print(f"F_емп = {F_emp:.2f}")

print("\nСтупені свободи:")
print(f"k1 = m - 1 = {m} - 1 = {k1}")
print(f"k2 = n - m = {n} - {m} = {k2}")

print("\nКритичне значення:")
print(f"F_кр({alpha}; {k1}; {k2}) = {F_crit:.2f}")

print("\nПорівняння:")
print(f"F_емп = {F_emp:.2f}")
print(f"F_кр = {F_crit:.2f}")

if F_emp > F_crit:
    print("\nВисновок:")
    print(f"Оскільки F_емп = {F_emp:.2f} > F_кр = {F_crit:.2f},")
    print("нульову гіпотезу відхиляємо.")
    print("Параболічна модель є статистично значущою та адекватною.")
else:
    print("\nВисновок:")
    print(f"Оскільки F_емп = {F_emp:.2f} <= F_кр = {F_crit:.2f},")
    print("нульову гіпотезу не відхиляємо.")
    print("Параболічна модель не є статистично значущою.")

