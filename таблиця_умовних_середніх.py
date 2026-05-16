import pandas as pd
import numpy as np

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
        "x_i^2 * n_i": x ** 2 * n_i,
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

print("\nСистема нормальних рівнянь МНК для лінійної регресії:")
print("a·Σx_i²n_i + b·Σx_i n_i = Σx_i n_i ȳ_xi")
print("a·Σx_i n_i  + b·Σn_i     = Σn_i ȳ_xi")

print("\nПісля підстановки числових значень:")
print(f"{sum_x2n}a + {sum_xn}b = {sum_xny:.1f}")
print(f"{sum_xn}a + {sum_n}b = {sum_ny:.1f}")

A = np.array([
    [sum_x2n, sum_xn],
    [sum_xn, sum_n]
], dtype=float)

B = np.array([sum_xny, sum_ny], dtype=float)

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

df["Q_total"] = df["n_i"] * (df["y_xi"] - y_general_mean) ** 2
df["Q_p"] = df["n_i"] * (df["y_i*"] - y_general_mean) ** 2
df["Q_o"] = df["n_i"] * (df["y_xi"] - df["y_i*"]) ** 2

print("\nТаблиця обчислення варіацій:")
print(df[["x_i", "n_i", "Q_total", "Q_p", "Q_o"]].to_string(index=False, formatters={
    "Q_total": "{:.4f}".format,
    "Q_p": "{:.4f}".format,
    "Q_o": "{:.4f}".format
}))

Q_total = df["Q_total"].sum()
Q_p = df["Q_p"].sum()
Q_o = df["Q_o"].sum()

print("\nПідсумовуємо:")
print(f"Q_total = {Q_total:.4f}")
print(f"Q_p = {Q_p:.4f}")
print(f"Q_o = {Q_o:.4f}")

print("\nПеревірка основного варіаційного рівняння:")
print("Q_total = Q_p + Q_o")
print(f"{Q_total:.4f} = {Q_p:.4f} + {Q_o:.4f}")
print(f"{Q_total:.4f} = {Q_p + Q_o:.4f}")

if round(Q_total, 4) == round(Q_p + Q_o, 4):
    print("Висновок: основне варіаційне рівняння виконується.")
else:
    print("Висновок: основне варіаційне рівняння не виконується через округлення або помилку в обчисленнях.")

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
    f"Приблизно {unexplained_percent:.2f}% варіації залишається непоясненою."
)