import matplotlib.pyplot as plt
import numpy as np

players = [
    "Lionel Messi",
    "Cristiano Ronaldo",
    "Robert Lewandowski",
    "Kylian Mbappe",
    "Erling Haaland",
]
player_indices = np.arange(len(players))
goals_scored = [45, 52, 48, 42, 50]
assists = [20, 15, 18, 23, 22]
mins_played = [2800, 2900, 2750, 2700, 2850]


def display_2d_plots():
    fig, axs = plt.subplots(2, 2, figsize=(14, 8))
    axs = axs.flatten()
    # Create a histogram of the number of goals scored by players.
    axs[0].hist(goals_scored, bins=5, edgecolor="black")
    axs[0].set_title("Histogram of Goals Scored by Players")
    axs[0].set_xlabel("Number of Goals Scored")
    axs[0].set_ylabel("Number of Players")
    axs[0].set_xticks(range(42, 55, 5))

    # Create a box plot of the number of assists provided by players.
    axs[1].boxplot(
        assists,
        vert=False,
        patch_artist=True,
        boxprops=dict(facecolor="blue", color="blue"),
        medianprops=dict(color="red"),
        whiskerprops=dict(color="green", linestyle="--"),
        capprops=dict(color="purple"),
        flierprops=dict(marker="o", markerfacecolor="yellow", markersize=8),
    )
    axs[1].set_xlabel("Assists")
    axs[1].set_title("Number of assists provided by players")

    # Create a heatmap of a correlation matrix between goals scored, assists provided, and minutes played.
    data = np.array([goals_scored, assists, mins_played])
    corr_matrix = np.corrcoef(data)
    axs[2].imshow(corr_matrix, cmap="hot")
    axs[2].set_title("Correlation Matrix")

    labels = ["Goals Scored", "Assists", "Minutes Played"]
    tick_marks = np.arange(len(labels))
    axs[2].set_xticks(tick_marks)
    axs[2].set_yticks(tick_marks)
    axs[2].set_xticklabels(labels)
    axs[2].set_yticklabels(labels)

    axs[3].axis("off")

    plt.tight_layout()
    plt.show()


def display_3d_plots():
    fig, axs = plt.subplots(1, 2, figsize=(14, 8))
    axs = axs.flatten()
    axs[0].axis("off")
    axs[1].axis("off")

    # Create a 3D scatterplot of goals scored, assists, and minutes played.
    ax3d = fig.add_subplot(121, projection="3d")  # Create a 3D subplot
    ax3d.scatter(goals_scored, assists, mins_played, c="red", marker="o")
    ax3d.set_title("3D Scatter Plot of Goals, Assists, and Minutes Played")
    ax3d.set_xlabel("Goals")
    ax3d.set_ylabel("Assists")
    ax3d.set_zlabel("Minutes Played")

    # Create a 3D bar plot to show the relationship between the players, the number of goals scored by them, and the assists made by them.
    ax = fig.add_subplot(122, projection="3d")  # Create a 3D subplot
    for i, player in enumerate(player_indices):
        ax.bar3d(i, goals_scored[i], 0, 0.4, 0.8, assists[i], color="b")

    ax.set_title("3D Bar Plot of Player Performance")
    ax.set_xticks(player_indices)
    ax.set_xticklabels(players, rotation=45, horizontalalignment="right")
    ax.set_xlabel("Players")
    ax.set_ylabel("Goals")
    ax.set_zlabel("Assists")
    plt.tight_layout()
    plt.show()


val = input("Enter 1 for displaying 2D plots / 2 for displaying 3D plots: ")
try:
    val = int(val)  # Convert input to integer
    if val == 1:
        display_2d_plots()
    elif val == 2:
        display_3d_plots()
except ValueError:
    print("Invalid input. Please enter a number.")
