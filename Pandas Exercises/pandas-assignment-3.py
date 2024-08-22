import pandas as pd

# Load the data
# Do not change this line, this is the file you will be working on, if you want to check the contents of the file
# You can copy the link and download it, or you can use python to see the contents
url = "https://s3.amazonaws.com/coderbyteprojectattachments/reatcodeltd-axldp-lkxhr3hf-CelticsvsRbLeipzig.csv"
df = pd.read_csv(url)


def total_goals(df, team_name):
    filtered_df = df[["teamName", "matchName", "goals"]]
    team_data = filtered_df[filtered_df["teamName"] == team_name]
    goals = team_data["goals"].sum()
    print(goals)


total_goals(df, "RB Leipzig")


# Please do not touch this function, it is there to test if your answer is correct
def test_answer():
    assert total_goals(df, "Celtic") == df[df["teamName"] == "Celtic"]["goals"].sum()
    assert (
        total_goals(df, "RB Leipzig")
        == df[df["teamName"] == "RB Leipzig"]["goals"].sum()
    )
