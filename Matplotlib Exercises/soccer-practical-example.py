import matplotlib.pyplot as plt

players = ["Harry Kane", "Mo Salah", "Bruno Fernandes", "Jamie Vardy", "Son Heung-min"]
teams = [
    "Tottenham Hotspur",
    "Liverpool",
    "Manchester United",
    "Leicester City",
    "Tottenham Hotspur",
]
goals_scored = [23, 25, 21, 22, 19]
assists = [8, 7, 11, 6, 10]
games_played = [34, 33, 34, 35, 33]
team_points = [65, 74, 70, 64, 65]

fig, axs = plt.subplots(2, 2, figsize=(16, 10))

# Create a line plot to show the number of goals scored by each player throughout the season.
axs[0, 0].plot(players, goals_scored, marker="o")
axs[0, 0].set_ylabel("Goals Scored")
axs[0, 0].set_title("Goals scored by EPL Players in a season")
axs[0, 0].grid()


# Create a scatter plot to represent the correlation between the number of games played and the number of goals scored.
axs[0, 1].scatter(games_played, goals_scored)
axs[0, 1].set_xlabel("Games Played")
axs[0, 1].set_ylabel("Goals Scored")
axs[0, 1].set_title("Games Played vs Goals Scored (Season)")
axs[0, 1].grid()


# Create a bar plot to show the total points earned by each team.
bar = axs[1, 0].bar(teams, team_points, color="blue")
axs[1, 0].grid()
bar[1].set_color("r")
bar[2].set_color("r")


# Create a pie chart to show the distribution of assists among the players.
axs[1, 1].pie(assists, labels=players, autopct="%1.1f%%")
axs[1, 1].set_title("Assists distribution among EPL players (Season)")
axs[1, 1].grid()

plt.tight_layout()
plt.show()
