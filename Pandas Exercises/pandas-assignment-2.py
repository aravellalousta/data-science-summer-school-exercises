import pandas as pd

# Load the data
# Do not change this line, this is the file you will be working on, if you want to check the contents of the file
# You can copy the link and download it, or you can use python to see the contents
url = "https://s3.amazonaws.com/coderbyteprojectattachments/reatcodeltd-axldp-lkxhr3hf-CelticsvsRbLeipzig.csv"
df = pd.read_csv(url)


def total_passes(df, team_name):
    accurate_pass = df[["teamName", "matchName", "accuratePass"]]
    team_data = accurate_pass[accurate_pass["teamName"] == team_name]
    total_passes = team_data["accuratePass"].sum()
    print(total_passes)


# Please do not touch this function, it is there to test if your answer is correct
def test_answer():
    assert (
        total_passes(df, "Celtic")
        == df[df["teamName"] == "Celtic"]["accuratePass"].sum()
    )
    assert (
        total_passes(df, "RB Leipzig")
        == df[df["teamName"] == "RB Leipzig"]["accuratePass"].sum()
    )
