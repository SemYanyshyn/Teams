# Значення X та їхні частоти n_i
x_values = [3, 5, 6, 9, 12, 14, 19]
n_i = [25, 36, 31, 28, 25, 35, 7]

# Значення Y та їхні частоти m_j
y_values = [1.5, 2.5, 3, 3.5, 4, 4.5]
m_j = [21, 38, 40, 32, 25, 31]

# Загальна кількість спостережень
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