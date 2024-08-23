import plotly.graph_objects as go
import pandas as pd

data = {
    "Year": [2017, 2018, 2019, 2020],
    "Product A": [2000, 2500, 2700, 3000],
    "Product B": [1500, 1800, 2100, 2400],
    "Product C": [1800, 2100, 2300, 2500],
}

df = pd.DataFrame(data)

fig = go.Figure()

for product in ["Product A", "Product B", "Product C"]:
    fig.add_trace(
        go.Scatter(x=df["Year"], y=df[product], mode="lines+markers", name=product)
    )

fig.update_layout(title="Sales of the year", xaxis_title="Year", yaxis_title="Sales")
fig.show()
