import pandas as pd
import plotly.graph_objects as go

# Create a sample DataFrame
data = {
    "Year": [2020, 2020, 2020, 2021, 2021, 2021, 2022, 2022, 2022],
    "Player": [
        "Lionel Messi",
        "Cristiano Ronaldo",
        "Neymar",
        "Lionel Messi",
        "Cristiano Ronaldo",
        "Neymar",
        "Lionel Messi",
        "Cristiano Ronaldo",
        "Neymar",
    ],
    "Team": [
        "FC Barcelona",
        "Juventus",
        "Paris Saint-Germain",
        "FC Barcelona",
        "Juventus",
        "Paris Saint-Germain",
        "Paris Saint-Germain",
        "Manchester United",
        "Paris Saint-Germain",
    ],
    "Goals": [25, 28, 20, 30, 33, 26, 32, 31, 29],
}

df = pd.DataFrame(data)

# Create figure
fig = go.Figure()

for year in df["Year"].unique():
    fig.add_trace(
        go.Scatter(
            visible=False,
            name="𝜈 = " + str(year),
            x=df.loc[df["Year"] == year, "Player"],
            y=df.loc[df["Year"] == year, "Goals"],
        )
    )
fig.data[0].visible = True

steps = []
for i in range(len(fig.data)):
    step = dict(
        method="update",
        args=[
            {"visible": [False] * len(fig.data)},
            {"title": "Slider switched to year: " + str(df["Year"].unique()[i])},
        ],
    )
    step["args"][0]["visible"][i] = True
    steps.append(step)

sliders = [
    dict(active=0, currentvalue={"prefix": "Year: "}, pad={"t": 50}, steps=steps)
]

fig.update_layout(sliders=sliders)

fig.show()
