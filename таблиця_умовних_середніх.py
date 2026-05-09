import pandas as pd

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