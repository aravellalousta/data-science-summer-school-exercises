import matplotlib.pyplot as plt


players = [
    "Lionel Messi",
    "Cristiano Ronaldo",
    "Robert Lewandowski",
    "Kylian Mbappe",
    "Erling Haaland",
]
teams = ["PSG", "Manchester United", "Bayern Munich", "PSG", "Borussia Dortmund"]
goals_scored = [12, 15, 16, 13, 14]
assists = [5, 6, 4, 7, 5]
games_played = [10, 10, 10, 10, 10]
colors = ["#ff34ff", "#f428ea", "#589ef1", "#14fd4a", "#f451ab"]
markers = ["o", "s", "D", "X", "*"]

fig, axs = plt.subplots(2, 2, figsize=(14, 6))

# Create a line plot to show the number of goals scored by each player throughout the Champions League. Make sure to appropriately label your x and y axis, give your plot a title, and provide a legend.
axs[0, 0].plot(players, goals_scored, marker="o")
axs[0, 0].set_ylabel("Goals Scored")
axs[0, 0].set_title("Goals scored by Players in the Champions league")
axs[0, 0].grid()
axs[0, 0].legend("Goals")


# Create a scatter plot to represent the correlation between the number of games played and the number of goals scored, using different colors and markers for different players.
for i in range(len(players)):
    axs[0, 1].scatter(
        games_played[i],
        goals_scored[i],
        color=colors[i],
        marker=markers[i],
        label=players[i],
    )

axs[0, 1].set_xlabel("Games Played")
axs[0, 1].set_ylabel("Goals Scored")
axs[0, 1].set_title("Games Scored vs Goals Played")
axs[0, 1].grid()


# Create a bar plot to show the total assists provided by each player. Adjust the ticks and limits of the y-axis for better visualization.
bar = axs[1, 0].bar(players, assists, color="skyblue")
axs[1, 0].set_xticklabels(players, rotation=20)
axs[1, 0].set_ylim(0, 10)
axs[1, 0].grid()

axs[1, 1].axis("off")
plt.tight_layout()
plt.show()
