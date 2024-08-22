import pandas as pd

# Load the data
# Do not change this line, this is the file you will be working on, if you want to check the contents of the file
# You can copy the link and download it, or you can use python to see the contents
url = "https://s3.amazonaws.com/coderbyteprojectattachments/reatcodeltd-axldp-lkxhr3hf-CelticsvsRbLeipzig.csv"
df = pd.read_csv(url)


def most_active_team(df):
    filtered_df = df[["teamName", "matchName", "totalPass"]]
    most_active = df.groupby("teamName")["totalPass"].sum().idxmax()
    print(most_active)


most_active_team(df)


# Please do not touch this function, it is there to test if your answer is correct
def test_answer():
    assert most_active_team(df) == df.groupby("teamName")["totalPass"].sum().idxmax()
