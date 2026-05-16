import math

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

n_i = [sum(freq[j][i] for j in range(len(y_values))) for i in range(len(x_values))]
m_j = [sum(freq[j]) for j in range(len(y_values))]
n = sum(n_i)

print("Початкові дані:")
print("x_i =", x_values)
print("n_i =", n_i)
print("y_j =", y_values)
print("m_j =", m_j)
print("n =", n)

print("\nОбчислення вибіркового середнього для X:")

x_products = [x_values[i] * n_i[i] for i in range(len(x_values))]
x_sum = sum(x_products)
x_mean = x_sum / n

print("x_i * n_i =", x_products)
print("Σ x_i * n_i =", x_sum)
print(f"x̄ = {x_sum} / {n} = {x_mean:.4f}")

print("\nОбчислення вибіркового середнього для Y:")

y_products = [y_values[j] * m_j[j] for j in range(len(y_values))]
y_sum = sum(y_products)
y_mean = y_sum / n

print("y_j * m_j =", y_products)
print("Σ y_j * m_j =", y_sum)
print(f"ȳ = {y_sum} / {n} = {y_mean:.4f}")

print("\nОбчислення вибіркового лінійного коефіцієнта кореляції r:")

numerator = 0

for j in range(len(y_values)):
    for i in range(len(x_values)):
        numerator += freq[j][i] * (x_values[i] - x_mean) * (y_values[j] - y_mean)

sum_x = sum(n_i[i] * (x_values[i] - x_mean) ** 2 for i in range(len(x_values)))
sum_y = sum(m_j[j] * (y_values[j] - y_mean) ** 2 for j in range(len(y_values)))

denominator = math.sqrt(sum_x * sum_y)
r = numerator / denominator

print(f"ΣΣ n_ij(x_i - x̄)(y_j - ȳ) = {numerator:.4f}")
print(f"Σ n_i(x_i - x̄)^2 = {sum_x:.4f}")
print(f"Σ m_j(y_j - ȳ)^2 = {sum_y:.4f}")

print("\nПідстановка у формулу:")
print(f"r = {numerator:.4f} / sqrt({sum_x:.4f} * {sum_y:.4f})")
print(f"r = {numerator:.4f} / {denominator:.4f}")
print(f"r = {r:.4f}")

print("\nІнтерпретація:")

if r > 0:
    print("Оскільки r > 0, зв’язок між X та Y є додатний.")
elif r < 0:
    print("Оскільки r < 0, зв’язок між X та Y є від’ємний.")
else:
    print("Оскільки r = 0, лінійний зв’язок між X та Y відсутній.")

if abs(r) >= 0.7:
    print(f"Оскільки |r| = {abs(r):.4f}, зв’язок є сильним.")
elif abs(r) >= 0.3:
    print(f"Оскільки |r| = {abs(r):.4f}, зв’язок є помірним.")
else:
    print(f"Оскільки |r| = {abs(r):.4f}, зв’язок є слабким.")

print("\nПеревірка значущості коефіцієнта кореляції за t-критерієм Стьюдента:")

t_emp = r * math.sqrt(n - 2) / math.sqrt(1 - r ** 2)

df = n - 2
alpha = 0.05
t_crit = 1.972

print("Формула:")
print("t_емп = r * sqrt(n - 2) / sqrt(1 - r^2)")

print("\nПідстановка:")
print(f"t_емп = {r:.4f} * sqrt({n} - 2) / sqrt(1 - {r:.4f}^2)")
print(f"t_емп = {r:.4f} * sqrt({n - 2}) / sqrt(1 - {r ** 2:.4f})")
print(f"t_емп = {r:.4f} * {math.sqrt(n - 2):.4f} / sqrt({1 - r ** 2:.4f})")
print(f"t_емп = {r * math.sqrt(n - 2):.4f} / {math.sqrt(1 - r ** 2):.4f}")

print("\nРезультат:")
print(f"t_емп = {t_emp:.4f}")

print("\nКритичні значення:")
print(f"α = {alpha}")
print(f"df = n - 2 = {n} - 2 = {df}")
print(f"t_кр = {t_crit}")

print("\nПорівняння:")

if abs(t_emp) > t_crit:
    print(f"|t_емп| > t_кр")
    print(f"{abs(t_emp):.4f} > {t_crit}")
    print("Отже, H0 відхиляємо.")
    print("Коефіцієнт кореляції є статистично значущим.")
else:
    print(f"|t_емп| ≤ t_кр")
    print(f"{abs(t_emp):.4f} ≤ {t_crit}")
    print("Отже, H0 не відхиляємо.")
    print("Статистично значущого лінійного зв’язку не підтверджено.")