import pandas as pd
import numpy as np

x_values = [3, 5, 6, 9, 12, 14, 19]
y_values = [1.5, 2.5, 3, 3.5, 4, 4.5]

freq = [
    [21, 0, 0, 0, 0, 0, 0],
    [4, 31, 3, 0, 0, 0, 0],
    [0, 5, 28, 3, 4, 0, 0],
    [0, 0, 0, 25, 4, 3, 0],
    [0, 0, 0, 0, 17, 3, 5],
    [0, 0, 0, 0, 0, 29, 2]
]

results = []

for j, x in enumerate(x_values):
    n_i = sum(freq[i][j] for i in range(len(y_values)))
    numerator = sum(freq[i][j] * y_values[i] for i in range(len(y_values)))
    y_mean = numerator / n_i

    results.append({
        "x_i": x,
        "n_i": n_i,
        "y_xi": y_mean,
        "x_i * n_i": x * n_i,
        "x_i^2 * n_i": x**2 * n_i,
        "n_i * y_xi": n_i * y_mean,
        "x_i * n_i * y_xi": x * n_i * y_mean
    })

df = pd.DataFrame(results)

print("Таблиця умовних середніх:")
print(df[["x_i", "n_i", "y_xi"]].to_string(index=False, formatters={
    "y_xi": "{:.4f}".format
}))

sum_n = df["n_i"].sum()
sum_xn = df["x_i * n_i"].sum()
sum_x2n = df["x_i^2 * n_i"].sum()
sum_ny = df["n_i * y_xi"].sum()
sum_xny = df["x_i * n_i * y_xi"].sum()

print("\nОбчислимо потрібні суми:")
print(f"Σ n_i = {sum_n}")

print(
    "Σ x_i n_i = "
    + " + ".join([f"{row['x_i']}·{row['n_i']}" for _, row in df.iterrows()])
    + f" = {sum_xn}"
)

print(
    "Σ x_i² n_i = "
    + " + ".join([f"{row['x_i']}²·{row['n_i']}" for _, row in df.iterrows()])
    + f" = {sum_x2n}"
)

print(f"Σ n_i ȳ_xi = {sum_ny:.1f}")
print(f"Σ x_i n_i ȳ_xi = {sum_xny:.1f}")

print("\nСистема нормальних рівнянь МНК:")
print("a·Σx_i²n_i + b·Σx_i n_i = Σx_i n_i ȳ_xi")
print("a·Σx_i n_i  + b·Σn_i     = Σn_i ȳ_xi")

print("\nПісля підстановки числових значень:")
print(f"{sum_x2n}a + {sum_xn}b = {sum_xny:.1f}")
print(f"{sum_xn}a + {sum_n}b = {sum_ny:.1f}")

A = np.array([
    [sum_x2n, sum_xn],
    [sum_xn, sum_n]
])

B = np.array([sum_xny, sum_ny])

a, b = np.linalg.solve(A, B)

print("\nРозв'язок системи:")
print(f"a = {a:.4f}")
print(f"b = {b:.4f}")

print("\nРівняння лінійної регресії:")
print(f"y = {a:.4f}x + {b:.4f}")
print(f"y ≈ {a:.2f}x + {b:.2f}")

df["y_i*"] = a * df["x_i"] + b

print("\nТеоретичні значення за лінійною моделлю:")
print("y_i* = ax_i + b")
print(f"y_i* = {a:.4f}x_i + {b:.4f}")

print("\nТаблиця теоретичних значень:")
print(df[["x_i", "n_i", "y_xi", "y_i*"]].to_string(index=False, formatters={
    "y_xi": "{:.4f}".format,
    "y_i*": "{:.4f}".format
}))

y_general_mean = sum_ny / sum_n

print("\nЗагальне середнє значення Y:")
print("ȳ = Σ n_i ȳ_xi / Σ n_i")
print(f"ȳ = {sum_ny:.1f} / {sum_n}")
print(f"ȳ = {y_general_mean:.4f}")

# Загальне середнє значення Y
y_general_mean = sum_ny / sum_n

print("\nЗагальне середнє значення Y:")
print("ȳ = Σ n_i ȳ_xi / Σ n_i")
print(f"ȳ = {sum_ny:.1f} / {sum_n}")
print(f"ȳ = {y_general_mean:.4f}")

# Обчислення варіацій
df["Q_total"] = df["n_i"] * (df["y_xi"] - y_general_mean) ** 2
df["Q_p"] = df["n_i"] * (df["y_i*"] - y_general_mean) ** 2
df["Q_o"] = df["n_i"] * (df["y_xi"] - df["y_i*"]) ** 2

print("\nТаблиця обчислення варіацій:")
print(df[["x_i", "n_i", "Q_total", "Q_p", "Q_o"]].to_string(index=False, formatters={
    "Q_total": "{:.4f}".format,
    "Q_p": "{:.4f}".format,
    "Q_o": "{:.4f}".format
}))

# Підсумки варіацій
Q_total = df["Q_total"].sum()
Q_p = df["Q_p"].sum()
Q_o = df["Q_o"].sum()

print("\nПідсумовуємо:")
print(f"Q_total = {Q_total:.4f}")
print(f"Q_p = {Q_p:.4f}")
print(f"Q_o = {Q_o:.4f}")

# Перевірка основного варіаційного рівняння
print("\nПеревірка основного варіаційного рівняння:")
print("Q_total = Q_p + Q_o")
print(f"{Q_total:.4f} = {Q_p:.4f} + {Q_o:.4f}")
print(f"{Q_total:.4f} = {Q_p + Q_o:.4f}")

if round(Q_total, 4) == round(Q_p + Q_o, 4):
    print("Висновок: основне варіаційне рівняння виконується.")
else:
    print("Висновок: основне варіаційне рівняння не виконується через округлення або помилку в обчисленнях.")

# Коефіцієнт детермінації
R2 = Q_p / Q_total
R2_percent = R2 * 100
unexplained_percent = 100 - R2_percent

print("\nКоефіцієнт детермінації:")
print("R² = Q_p / Q_total")
print(f"R² = {Q_p:.4f} / {Q_total:.4f}")
print(f"R² = {R2:.4f}")

print("\nУ відсотках:")
print(f"R² · 100% = {R2_percent:.2f}%")

print("\nВисновок:")
print(
    f"Отже, лінійна модель пояснює приблизно {R2_percent:.2f}% "
    f"варіації результативної ознаки Y. "
    f"Це означає, що лінійна модель має достатньо добру якість опису даних, "
    f"але не є ідеальною, оскільки приблизно {unexplained_percent:.2f}% "
    f"варіації залишається непоясненою."
)

# Вибіркові середні значення X та Y
x_mean = sum_xn / sum_n
y_mean_general = sum_ny / sum_n

print("\nВибіркове середнє для X:")
print("x̄ = Σ x_i n_i / n")
print(f"x̄ = {sum_xn} / {sum_n}")
print(f"x̄ = {x_mean:.4f}")

print("\nСереднє для Y вже було знайдено:")
print("ȳ = Σ n_i ȳ_xi / n")
print(f"ȳ = {sum_ny:.1f} / {sum_n}")
print(f"ȳ = {y_mean_general:.4f}")

m_j_values = [sum(row) for row in freq]

numerator_r = 0

for i, y in enumerate(y_values):
    for j, x in enumerate(x_values):
        n_ij = freq[i][j]
        numerator_r += n_ij * (x - x_mean) * (y - y_mean)

sum_x_part = sum(
    df.loc[i, "n_i"] * (df.loc[i, "x_i"] - x_mean) ** 2
    for i in range(len(df))
)

sum_y_part = sum(
    m_j_values[i] * (y_values[i] - y_mean) ** 2
    for i in range(len(y_values))
)

denominator_r = (sum_x_part * sum_y_part) ** 0.5

r = numerator_r / denominator_r

print("\nВибірковий лінійний коефіцієнт кореляції:")
print(f"x̄ = {x_mean:.4f}")
print(f"ȳ = {y_mean:.4f}")
print(f"ΣΣ n_ij(x_i - x̄)(y_j - ȳ) = {numerator_r:.4f}")
print(f"Σ n_i(x_i - x̄)² = {sum_x_part:.4f}")
print(f"Σ m_j(y_j - ȳ)² = {sum_y_part:.4f}")
print(f"√(Σ n_i(x_i - x̄)² · Σ m_j(y_j - ȳ)²) = {denominator_r:.4f}")
print(f"r = {numerator_r:.4f} / {denominator_r:.4f}")
print(f"r = {r:.4f}")

print("\nВисновок:")
print(f"Оскільки r = {r:.4f}, між X та Y існує сильний додатний лінійний зв'язок.")


import math

r = 0.8973
n = 187

t_emp = (r * math.sqrt(n - 2)) / math.sqrt(1 - r**2)

print("Перевірка значущості коефіцієнта кореляції:")
print("t_емп = r√(n - 2) / √(1 - r²)")
print(f"t_емп = {r}√({n} - 2) / √(1 - {r}²)")
print(f"t_емп = {t_emp:.4f}")




