import pandas as pd
import numpy as np

# Creating a made-up dataset
# We have 100 employees
employee_ids = np.arange(1, 101)

# The departments are randomly assigned
departments = np.random.choice(["HR", "Sales", "Finance", "Marketing"], 100)

# Generate random ages between 25 and 60 for our employees
ages = np.random.randint(25, 61, 100)

# Generate random salaries between 30000 and 120000 for our employees
salaries = np.random.randint(30000, 120001, 100)

# Create DataFrame
data = pd.DataFrame(
    {
        "EmployeeID": employee_ids,
        "Department": departments,
        "Age": ages,
        "Salary": salaries,
    }
)

# Convert the 'Department' column to a categorical data type
data["Department"] = data["Department"].astype("category")

sorted_data = data.sort_values(by="Department")
grouped_data = data.groupby("Department")

filtered_data = data[data["Department"] == "Finance"]
print(filtered_data)
