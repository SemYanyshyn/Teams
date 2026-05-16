import matplotlib.pyplot as plt

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

m_j = [sum(row) for row in freq]
n_i = [sum(freq[r][c] for r in range(len(freq))) for c in range(len(freq[0]))]
total_n = sum(m_j)

print("Суми за рядками m_j =", m_j)
print("Суми за стовпцями n_i =", n_i)
print("Загальна кількість спостережень n =", total_n)

col_labels = [str(x) for x in x_values] + ["m_j"]
row_labels = [str(y) for y in y_values] + ["n_i"]

cell_text = []

for i in range(len(y_values)):
    row = [str(freq[i][j]) for j in range(len(x_values))]
    row.append(str(m_j[i]))
    cell_text.append(row)

last_row = [str(v) for v in n_i]
last_row.append(str(total_n))
cell_text.append(last_row)

plt.style.use("dark_background")
fig, ax = plt.subplots(figsize=(12, 6), dpi=150)
fig.patch.set_facecolor("#0f1720")
ax.set_facecolor("#0f1720")
ax.set_axis_off()

the_table = ax.table(
    cellText=cell_text,
    colLabels=col_labels,
    rowLabels=row_labels,
    cellLoc="center",
    colLoc="center",
    loc="center"
)

the_table.auto_set_font_size(False)
the_table.set_fontsize(12)
the_table.scale(1.15, 1.6)

header_bg = "#0b1220"
header_fg = "#ffffff"
last_row_bg = "#111827"
highlight_bg = "#1f2937"
highlight_fg = "#a3e635"
edge_color = "#1f2937"

for (row, col), cell in the_table.get_celld().items():
    cell.set_edgecolor(edge_color)
    txt = cell.get_text().get_text().strip()

    if row == 0:
        cell.set_facecolor(header_bg)
        cell.get_text().set_color(header_fg)
        cell.get_text().set_fontweight("bold")
        cell.set_height(0.06)

    elif col == -1:
        cell.get_text().set_fontweight("bold")
        cell.get_text().set_color("#e6eef8")
        cell.set_facecolor("#0f1720")

    if row == len(row_labels):
        cell.set_facecolor(last_row_bg)
        cell.get_text().set_fontweight("bold")
        cell.get_text().set_color("#f8fafc")

    if row > 0 and col >= 0 and txt not in ("", "0"):
        try:
            if int(txt) != 0:
                cell.set_facecolor(highlight_bg)
                cell.get_text().set_color(highlight_fg)
        except Exception:
            pass

plt.title(
    "Кореляційна таблиця частот",
    fontsize=16,
    fontweight="bold",
    pad=12,
    color="#e6eef8"
)

out_path = "kor_table_new.png"
plt.savefig(out_path, bbox_inches="tight", dpi=220, facecolor=fig.get_facecolor())
print(f"Збережено: {out_path}")
plt.show()