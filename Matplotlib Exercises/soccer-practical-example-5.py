import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Player": [
        "Lionel Messi",
        "Cristiano Ronaldo",
        "Neymar Jr.",
        "Kylian Mbappe",
        "Robert Lewandowski",
    ],
    "Games Played": [38, 40, 35, 39, 34],
    "Goals": [36, 34, 21, 33, 41],
    "Assists": [12, 7, 10, 7, 5],
    "Successful Dribbles": [174, 89, 142, 90, 41],
    "Yellow Cards": [3, 5, 6, 2, 1],
}
colors = ["#56445D", "#FE621D", "#5A7684", "#00CFC1", "#AAD922"]


df = pd.DataFrame(data)

fig, axs = plt.subplots(3, 1, figsize=(12, 9))


for i in range(0, 3):
    axs[i].grid()

axs[0].bar(df["Player"], df["Goals"])
axs[0].set_title("Number of Goals Scored by each Player")

axs[1].hist(df["Yellow Cards"], 5, (1, 6), color="pink")
axs[1].set_title("Distribution of Yellow Cards")
axs[1].set_ylabel("Frequency")
axs[1].set_xlabel("Yellow Cards")

for player in df["Player"]:
    axs[2].scatter(
        df[df["Player"] == player]["Games Played"],
        df[df["Player"] == player]["Successful Dribbles"],
        label=player,
    )
axs[2].set_title("Relationship between Games Played and Successful Dribbles")
axs[2].set_ylabel("Successful Dribbles")
axs[2].set_xlabel("Games Played")
axs[2].legend(df["Player"])
plt.tight_layout()
plt.show()
