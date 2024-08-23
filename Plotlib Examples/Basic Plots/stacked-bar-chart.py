import plotly.graph_objects as go
import pandas as pd

data = {
    "Player": ["Lionel Messi", "Cristiano Ronaldo", "Neymar", "Kylian Mbappé"],
    "Goals": [31, 36, 19, 27],
    "Assists": [27, 7, 12, 7],
}

df = pd.DataFrame(data)

fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=df["Player"],
        y=df["Goals"],
        text=df["Goals"],
        name="Goals",
        marker_color="blue",
    )
)

fig.add_trace(
    go.Bar(
        x=df["Player"],
        y=df["Assists"],
        text=df["Assists"],
        name="Assists",
        marker_color="hotpink",
    )
)

fig.update_layout(
    xaxis_title="Player", yaxis_title="Goals and Assists", barmode="stack"
)

fig.show()
