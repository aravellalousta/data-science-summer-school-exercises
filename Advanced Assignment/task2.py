import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv("Advanced Assignment/data/filtered_employee_attrition.csv")

filtered_df = df[
    [
        "Age",
        "DailyRate",
        "DistanceFromHome",
        "MonthlyIncome",
        "NumCompaniesWorked",
        "PercentSalaryHike",
        "TotalWorkingYears",
        "TrainingTimesLastYear",
        "YearsAtCompany",
        "YearsInCurrentRole",
        "YearsSinceLastPromotion",
        "YearsWithCurrManager",
    ]
]

# Plotting correlation heatmap
fig, ax = plt.subplots(figsize=(10, 7))
sns.set_theme(font_scale=0.8)
dataplot = sns.heatmap(
    filtered_df.corr(numeric_only=True), cmap="coolwarm", annot=True, fmt=".2f"
)

# Displaying heatmap
plt.subplots_adjust(wspace=0, top=0.95, bottom=0.1, left=0.22, right=1)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="center")
plt.title("Correlation Matrix Heatmap of Employee Attributes")
plt.show()
