import pandas as pd
import plotly.graph_objects as go

data = {
    "Employee": [
        "John",
        "Maria",
        "Steve",
        "Helen",
        "Tom",
        "Rose",
        "Mark",
        "Jenny",
        "Greg",
        "Sophia",
    ],
    "Salary": [34000, 36000, 29000, 22000, 28000, 30000, 40000, 35000, 37000, 32000],
}

df = pd.DataFrame(data)

trace = go.Box(y=df["Salary"], name="Employee Salary")

layout = go.Layout(title="Employee Salary Distribution")

fig = go.Figure(data=[trace], layout=layout)
fig.show()
