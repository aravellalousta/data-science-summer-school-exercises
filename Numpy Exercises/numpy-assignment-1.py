import pandas as pd
import numpy as np

# Load the data
# Do not change this line, this is the file you will be working on, if you want to check the contents of the file
# You can copy the link and download it, or you can use python to see the contents
df = pd.read_csv(
    "https://s3.amazonaws.com/coderbyteprojectattachments/reatcodeltd-axldp-o14h1x17-NapolivsAjax.csv"
)


def get_player_with_most_ball_recoveries(df):
    max_ball_recovery = df["ballRecovery"].max()
    max_row = df[df["ballRecovery"] == max_ball_recovery]
    player_name = max_row["matchName"].values[0]
    print(player_name)


get_player_with_most_ball_recoveries(df)
