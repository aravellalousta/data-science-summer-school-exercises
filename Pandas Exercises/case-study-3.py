import pandas as pd

# Define player data
player_data = {
    "Player": [
        "Lionel Messi",
        "Cristiano Ronaldo",
        "Neymar Jr.",
        "Kylian Mbappé",
        "Robert Lewandowski",
        "Kevin De Bruyne",
        "Virgil van Dijk",
        "Mohamed Salah",
        "Karim Benzema",
        "Harry Kane",
    ],
    "Team": [
        "Inter Miami",
        "Al-Nassr",
        "Al-Hilal",
        "PSG",
        "Barcelona",
        "Manchester City",
        "Liverpool",
        "Liverpool",
        "Al-Ittihad",
        "Bayern Munich",
    ],
    "Position": [
        "Forward",
        "Forward",
        "Forward",
        "Forward",
        "Forward",
        "Midfielder",
        "Defender",
        "Forward",
        "Forward",
        "Forward",
    ],
}


# Create player DataFrame
df_player = pd.DataFrame(player_data)

# Define performance data
performance_data = {
    "Player": [
        "Lionel Messi",
        "Cristiano Ronaldo",
        "Neymar Jr.",
        "Kylian Mbappé",
        "Robert Lewandowski",
        "Kevin De Bruyne",
        "Virgil van Dijk",
        "Mohamed Salah",
        "Karim Benzema",
        "Harry Kane",
    ],
    "Goals": [
        30,
        31,
        27,
        33,
        36,
        10,
        5,
        25,
        24,
        28,
    ],
    "Assists": [
        15,
        12,
        17,
        15,
        9,
        22,
        3,
        11,
        8,
        5,
    ],
}


# Create performance DataFrame
df_performance = pd.DataFrame(performance_data)

# Display the DataFrames
print("Player DataFrame:")
print(df_player)
print("\nPerformance DataFrame:")
print(df_performance)


def calculate_goal_assist_ratio(goals, assists):
    if assists == 0:
        return goals
    else:
        return goals / assists


# Create column displaying goal - assist ratio
df_performance["Goal_Assist_Ratio"] = df_performance.apply(
    lambda row: calculate_goal_assist_ratio(row["Goals"], row["Assists"]), axis=1
)

# Print the updated DataFrame
print("\nPerformance DataFrame with Goal-Assist Ratio:")
print(df_performance)

# Sorting and ranking by goals
df_sorted_goals = df_performance.sort_values("Goals", ascending=False)
df_sorted_goals["Goal_Rank"] = df_sorted_goals["Goals"].rank(ascending=False)

# Display number of players per team by grouping
df_grouped = df_player.groupby("Team").size()
print("Number of players per team: ")
print(df_grouped)

# Merging DataFrames
df_merged = pd.merge(df_player, df_performance, on="Player")
print(df_merged)
