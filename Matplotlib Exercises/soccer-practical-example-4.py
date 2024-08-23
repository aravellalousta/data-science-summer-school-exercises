import matplotlib.pyplot as plt
import numpy as np

players = [
    "Lionel Messi",
    "Cristiano Ronaldo",
    "Neymar Jr.",
    "Kylian Mbappe",
    "Robert Lewandowski",
]
goals = [36, 34, 21, 33, 41]
assists = [12, 7, 10, 7, 5]
dribbles = [174, 89, 142, 90, 41]

# Create a single output with a grid layout of three plots showing the statistics of the players in terms of goals, assists, and successful dribbles.
# In the same layout, you need to annotate the player with the highest number of goals, assists, and successful dribbles in each respective plot.
# Use subplots and ensure the plots share the same x-axis for better comparison.

fig, axs = plt.subplots(3, 1, figsize=(12, 8))

axs[0].bar(players, goals, color="blue")
axs[0].set_ylim(0, 45)
axs[0].set_ylabel("Goals")
axs[0].grid(axis="y")
max_index_goals = np.argmax(goals)
max_goals = goals[max_index_goals]
max_goals_player = players[max_index_goals]
axs[0].annotate(
    f"Max: {max_goals_player}",
    xy=(max_goals_player, max_goals),
    arrowprops=dict(facecolor="red", shrink=0.05),
    ha="center",
)

axs[1].bar(players, assists, color="blue")
axs[1].set_ylim(0, 15)
axs[1].set_ylabel("Assists")
axs[1].grid(axis="y")
max_index_assists = np.argmax(assists)
max_assists = assists[max_index_assists]
max_assists_player = players[max_index_assists]
axs[1].annotate(
    f"Max: {max_assists_player}",
    xy=(max_assists_player, max_assists),
    arrowprops=dict(facecolor="red", shrink=0.05),
    ha="center",
)

axs[2].bar(players, dribbles, color="blue")
axs[2].set_ylim(0, 200)
axs[2].set_ylabel("Dribbles")
axs[2].grid(axis="y")
max_index_dribbles = np.argmax(dribbles)
max_dribbles = dribbles[max_index_dribbles]
max_dribbles_player = players[max_index_dribbles]
axs[2].annotate(
    f"Max: {max_dribbles_player}",
    xy=(max_dribbles_player, max_dribbles),
    arrowprops=dict(facecolor="red", shrink=0.05),
    ha="center",
)

plt.tight_layout()
plt.show()
