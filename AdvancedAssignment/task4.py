import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv("AdvancedAssignment/data/filtered_employees.csv")

emp_per_dept = df["Department"].value_counts()
print(emp_per_dept)

salary_stats = df.groupby("Department")["Salary"].describe()
print(salary_stats)

# Create a pie chart
colors = plt.get_cmap("viridis")(np.linspace(0, 1, len(emp_per_dept)))

plt.figure(figsize=(10, 6))
plt.pie(
    emp_per_dept,
    labels=emp_per_dept.index,
    autopct="%1.1f%%",
    colors=colors,
)
plt.title("Distribution of Employees by Department")
plt.show()
