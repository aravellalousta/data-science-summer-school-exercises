import pandas as pd
import plotly.graph_objects as go

data = {
    "ID": [
        "ID1",
        "ID2",
        "ID3",
        "ID4",
        "ID5",
        "ID6",
        "ID7",
        "ID8",
        "ID9",
        "ID10",
    ],
    "Age": [22, 24, 35, 45, 67, 72, 51, 48, 56, 33],
}

df = pd.DataFrame(data)

trace = go.Histogram(x=df["Age"], nbinsx=5, name="Age Distribution")

layout = go.Layout(title="Population Age Distribution")

fig = go.Figure(data=[trace], layout=layout)
fig.show()
