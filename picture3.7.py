import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import math

plt.style.use("seaborn-v0_8-darkgrid")

rcParams["figure.facecolor"] = "#f8f9fa"
rcParams["axes.facecolor"] = "#ffffff"
rcParams["font.size"] = 11
rcParams["font.family"] = "sans-serif"

x_values = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)
y_x_mean = np.array([
    1.19565217,
    5.50000000,
    11.25000000,
    16.93548387,
    25.31914894,
    34.88372093,
    44.00000000
], dtype=float)

a_linear = 6.788701684836472
b_linear = -0.5733399405351837

a_parabola = 0.6139479127529097
b_parabola = 3.580975958619456
c_parabola = 1.2062115107383296

a_root = 14.411356623524473
b_root = -1.9531105224252305

a_forecast = 0.6139
b_forecast = 3.5810
c_forecast = 1.2062

x_forecast = np.array([14, 15], dtype=float)
y_forecast = a_forecast * x_forecast ** 2 + b_forecast * x_forecast + c_forecast

x_smooth = np.linspace(min(x_values), max(x_forecast), 500)

y_linear = a_linear * x_smooth + b_linear
y_parabola = a_parabola * x_smooth ** 2 + b_parabola * x_smooth + c_parabola
y_root = a_root * np.sqrt(x_smooth) + b_root

fig, ax = plt.subplots(figsize=(14, 8), dpi=120)

color_scatter = "#FF6B6B"
color_empirical = "#4ECDC4"
color_linear = "#45B7D1"
color_parabola = "#F7B731"
color_root = "#9B59B6"
color_forecast = "#2ECC71"

ax.scatter(
    x_values,
    y_x_mean,
    s=250,
    label="Умовні середні ȳ_xi",
    color=color_scatter,
    alpha=0.8,
    edgecolors="darkred",
    linewidth=2.5,
    zorder=5
)

ax.plot(
    x_values,
    y_x_mean,
    marker="o",
    markersize=10,
    linewidth=2.5,
    label="Емпірична лінія регресії",
    color=color_empirical,
    alpha=0.9,
    zorder=4
)

ax.plot(
    x_smooth,
    y_linear,
    linestyle="--",
    linewidth=3,
    label="Лінійна регресія: y = 6.7887x - 0.5733",
    color=color_linear,
    alpha=0.85,
    zorder=3
)

ax.plot(
    x_smooth,
    y_parabola,
    linewidth=4,
    label="Параболічна регресія: y = 0.6139x² + 3.5810x + 1.2062",
    color=color_parabola,
    alpha=0.9,
    zorder=2
)

ax.plot(
    x_smooth,
    y_root,
    linestyle="-.",
    linewidth=3,
    label="Коренева регресія: y = 14.4114√x - 1.9531",
    color=color_root,
    alpha=0.85,
    zorder=2
)

ax.scatter(
    x_forecast,
    y_forecast,
    s=300,
    label="Прогнозні точки за параболічною моделлю",
    color=color_forecast,
    edgecolors="darkgreen",
    linewidth=2.5,
    marker="*",
    zorder=6
)

for x, y in zip(x_values, y_x_mean):
    ax.text(
        x,
        y + 1.0,
        f"({x:.0f}; {y:.2f})",
        ha="center",
        fontsize=9,
        fontweight="bold",
        bbox=dict(
            boxstyle="round,pad=0.3",
            facecolor="white",
            alpha=0.7,
            edgecolor="gray"
        )
    )

for index, (x, y) in enumerate(zip(x_forecast, y_forecast), start=1):
    ax.text(
        x,
        y + 4,
        f"P{index}({x:.0f}; {y:.4f})",
        ha="center",
        fontsize=10,
        fontweight="bold",
        color="darkgreen",
        bbox=dict(
            boxstyle="round,pad=0.35",
            facecolor="white",
            alpha=0.85,
            edgecolor="darkgreen"
        )
    )

ax.set_xlabel("X", fontsize=14, fontweight="bold", labelpad=10)
ax.set_ylabel("Y", fontsize=14, fontweight="bold", labelpad=10)

ax.set_title(
    "Поле кореляції, емпірична лінія, регресійні моделі та прогноз",
    fontsize=16,
    fontweight="bold",
    pad=20,
    color="#2C3E50"
)

ax.grid(True, linestyle="--", alpha=0.3, linewidth=0.8)
ax.set_axisbelow(True)

legend = ax.legend(
    fontsize=10,
    loc="upper left",
    framealpha=0.95,
    edgecolor="black",
    fancybox=True,
    shadow=True
)

legend.get_frame().set_linewidth(1.5)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_linewidth(1.5)
ax.spines["bottom"].set_linewidth(1.5)

ax.tick_params(axis="both", which="major", labelsize=11, width=1.5, length=6)
ax.tick_params(axis="both", which="minor", labelsize=10, width=1, length=3)

ax.set_facecolor("#ffffff")
fig.patch.set_facecolor("#f8f9fa")

ax.set_xlim(min(x_values) - 0.5, max(x_forecast) + 0.8)
ax.set_ylim(min(y_x_mean) - 3, max(y_forecast) + 20)

plt.tight_layout()

out_path = "plot_regression_with_forecast.png"
plt.savefig(out_path, dpi=150, bbox_inches="tight")

print(f"✓ Графік збережено в: {out_path}")

print("\nПрогнозні точки:")
for index, (x, y) in enumerate(zip(x_forecast, y_forecast), start=1):
    print(f"P{index}({x:.0f}; {y:.4f})")

plt.show()