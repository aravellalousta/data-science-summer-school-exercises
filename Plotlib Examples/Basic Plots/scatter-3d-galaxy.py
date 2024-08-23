import plotly.graph_objects as go
import numpy as np

# Simulate star data
np.random.seed(50)
n_stars = 500
x = np.random.normal(size=n_stars)
y = np.random.normal(size=n_stars)
z = np.random.normal(size=n_stars)

temp = np.random.randint(low=1000, high=8000, size=n_stars)
color = [
    "rgb({}, {}, 255)".format(int(t / 8000 * 255), int(t / 8000 * 255)) for t in temp
]

fig = go.Figure(
    data=[
        go.Scatter3d(
            x=x, y=y, z=z, mode="markers", marker=dict(size=6, color=color, opacity=0.8)
        )
    ]
)

fig.update_layout(
    title="Simulated Galaxy",
    scene=dict(xaxis=dict(title="X"), yaxis=dict(title="Y"), zaxis=dict(title="Z")),
    width=1000,
    height=1000,
    margin=dict(l=0, r=0, b=0, t=0),
)

fig.show()
