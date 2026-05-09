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

