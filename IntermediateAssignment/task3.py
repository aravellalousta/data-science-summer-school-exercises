import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("IntermediateAssignment/data/filtered_employees.csv")

mean_absences = df.groupby("PerformanceScore")["Absences"].mean().reset_index()

mean_absences.columns = ["Performance Score", "Mean Number of Absences"]

# Bar plot
sns.barplot(
    x="Performance Score",
    y="Mean Number of Absences",
    data=mean_absences,
    palette="viridis",
)

plt.xlabel("Performance Score")
plt.ylabel("Mean Number of Absences")
plt.title("Mean Number of Absences by Performance Score")
plt.show()
