import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("AdvancedAssignment/data/filtered_employees.csv")

departments = df.groupby("Department")

# Calculate mean salary per dept
mean_salary = departments["Salary"].mean()

# Calculcate mean employee satisfaction per dept
mean_satisf = departments["EmpSatisfaction"].mean()

# Plot the results in a dual axis
fig, ax = plt.subplots(figsize=(8, 6))
twin_x = ax.twinx()

mean_salary.plot(kind="bar", ax=ax, color="red")
mean_satisf.plot(kind="line", ax=twin_x, color="blue", marker="o")

for i, value in enumerate(mean_satisf):
    twin_x.text(i, value, f"{value:.2f}", ha="center", va="bottom", fontsize=10)


ax.set_ylabel("Mean Salary")
twin_x.set_ylabel("Mean Employee Satisfaction")

ax.set_xticklabels(ax.get_xticklabels(), rotation=0, ha="center")
twin_x.legend(loc="upper left")

plt.tight_layout()
plt.show()
