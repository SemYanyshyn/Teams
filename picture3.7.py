import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import rcParams

# Налаштування стилю
plt.style.use('seaborn-v0_8-darkgrid')
rcParams['figure.facecolor'] = '#f8f9fa'
rcParams['axes.facecolor'] = '#ffffff'
rcParams['font.size'] = 11
rcParams['font.family'] = 'sans-serif'

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

# Побудова графіка з більшим розміром
fig, ax = plt.subplots(figsize=(14, 8), dpi=120)

# Колірна схема
color_scatter = '#FF6B6B'
color_empirical = '#4ECDC4'
color_linear = '#45B7D1'
color_parabola = '#F7B731'

# 1. Поле кореляції (більші точки з прозорістю)
ax.scatter(x_values, y_x_mean, s=250, label="Поле кореляції", 
           color=color_scatter, alpha=0.8, edgecolors='darkred', linewidth=2.5, zorder=5)

# 2. Емпірична лінія регресії
ax.plot(x_values, y_x_mean, marker="o", markersize=10, linewidth=2.5, 
        label="Емпірична лінія регресії", color=color_empirical, alpha=0.9, zorder=4)

# 3. Лінійна регресія
ax.plot(x_smooth, y_linear, linestyle="--", linewidth=3, 
        label="Лінійна регресія: y = 0.1863x + 1.5881", color=color_linear, alpha=0.85, zorder=3)

# 4. Оптимальна нелінійна параболічна крива
ax.plot(x_smooth, y_parabola, linewidth=4, 
        label="Параболічна регресія: y = -0.0139x² + 0.4558x + 0.5618", 
        color=color_parabola, alpha=0.9, zorder=2)

# Підписи точок з поліпшеним стилем
for x, y in zip(x_values, y_x_mean):
    ax.text(x, y + 0.12, f"({x:.0f}; {y:.2f})", ha="center", 
            fontsize=9, fontweight='bold', 
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7, edgecolor='gray'))

# Оформлення осей
ax.set_xlabel("X", fontsize=14, fontweight='bold', labelpad=10)
ax.set_ylabel("Y", fontsize=14, fontweight='bold', labelpad=10)
ax.set_title("Поле кореляції, емпірична лінія та регресійні моделі", 
             fontsize=16, fontweight='bold', pad=20, color='#2C3E50')

# Покращення сітки
ax.grid(True, linestyle='--', alpha=0.3, linewidth=0.8)
ax.set_axisbelow(True)

# Покращена легенда
legend = ax.legend(fontsize=11, loc='upper left', framealpha=0.95, 
                   edgecolor='black', fancybox=True, shadow=True)
legend.get_frame().set_linewidth(1.5)

# Стиль осей
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

# Покращені відмітки на осях
ax.tick_params(axis='both', which='major', labelsize=11, width=1.5, length=6)
ax.tick_params(axis='both', which='minor', labelsize=10, width=1, length=3)

# Додати легкий фон для графіка
ax.set_facecolor('#ffffff')
fig.patch.set_facecolor('#f8f9fa')

# Налаштування меж осей з невеликим запасом
ax.set_xlim(min(x_values) - 1, max(x_values) + 1)
ax.set_ylim(min(y_parabola) - 0.3, max(y_x_mean) + 0.5)

plt.tight_layout()

# Зберегти графік у файл
plt.savefig('/Users/a860/Documents/IT-Pracitce/Proga/plot_regression.png', dpi=150, bbox_inches='tight')
print("✓ Графік збережено в: /Users/a860/Documents/IT-Pracitce/Proga/plot_regression.png")