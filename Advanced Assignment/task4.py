import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn import linear_model
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv("Advanced Assignment/data/filtered_employee_attrition.csv")

filtered_df = df[["Age", "TotalWorkingYears", "MonthlyIncome"]]
filtered_df.dropna()

# Stack the independent variables to form a 2D array
X = np.column_stack((df["Age"], df["TotalWorkingYears"]))
X = np.hstack([np.ones((X.shape[0], 1)), X])

# Perform the multiple linear regression
coefficients, residuals, rank, s = np.linalg.lstsq(X, df["MonthlyIncome"], rcond=None)


# Define the regression equation
def regression_plane(age, total_working_years, coefficients):
    return (
        coefficients[0] + coefficients[1] * age + coefficients[2] * total_working_years
    )


# Create a meshgrid for Age and TotalWorkingYears
age_range = np.linspace(df["Age"].min(), df["Age"].max(), 10)
total_working_years_range = np.linspace(
    df["TotalWorkingYears"].min(), df["TotalWorkingYears"].max(), 10
)
age_grid, twy_grid = np.meshgrid(age_range, total_working_years_range)

# Calculate the MonthlyIncome values on the regression plane
monthly_income_plane = regression_plane(age_grid, twy_grid, coefficients)

# Plot the data points and the regression plane
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")

# Plot the original data points
ax.scatter(
    df["Age"],
    df["TotalWorkingYears"],
    df["MonthlyIncome"],
    color="red",
    label="Data Points",
)

# Plot the regression plane
ax.plot_surface(
    age_grid,
    twy_grid,
    monthly_income_plane,
    color="blue",
    alpha=0.5,
    rstride=100,
    cstride=100,
)

# Labels and title
ax.set_xlabel("Age")
ax.set_ylabel("Total Working Years")
ax.set_zlabel("Monthly Income")
ax.set_title("Regression Plane")

plt.legend()
plt.show()
