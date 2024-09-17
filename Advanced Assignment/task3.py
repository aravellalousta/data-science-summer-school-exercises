import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv("Advanced Assignment/data/filtered_employee_attrition.csv")
filtered_df = df.loc[
    (
        (df["JobRole"] >= "Sales Executive")
        | (df["JobRole"] <= "Research Scientist")
        | (df["JobRole"] <= "Laboratory Technician")
    )
    & ((df["Department"] >= "Sales") | (df["Department"] >= "Research & Development"))
]

grouped_df = (
    filtered_df.groupby(["YearsAtCompany", "JobRole", "Department"])
    .agg({"MonthlyIncome": ["mean", "std", "count"]})
    .reset_index()
)
grouped_df.columns = [
    "YearsAtCompany",
    "JobRole",
    "Department",
    "MeanMonthlyIncome",
    "StdMonthlyIncome",
    "Count",
]

grouped_df = grouped_df[grouped_df["Count"] >= 5]

plt.figure(figsize=(10, 6))
line_plot = sns.lineplot(
    data=grouped_df,
    x="YearsAtCompany",
    y="MeanMonthlyIncome",
    hue="Department",
    style="JobRole",
    markers=True,
)

for job_role in grouped_df["JobRole"].unique():
    role_data = grouped_df[grouped_df["JobRole"] == job_role]
    plt.errorbar(
        role_data["YearsAtCompany"],
        role_data["MeanMonthlyIncome"],
        yerr=role_data["StdMonthlyIncome"],
        fmt="o",
    )

# Customize the plot
plt.title("Trend of Monthly Income Over Years at Company by Job Role and Department")
plt.xlabel("Years at Company")
plt.ylabel("Average Monthly Income")
plt.legend(title="Department and Job Role", loc="upper right")

plt.show()
