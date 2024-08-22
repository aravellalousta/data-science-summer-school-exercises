import pandas as pd

# Do not change this line, this is the file you will be working on, if you want to check the contents of the file
# You can copy the link and download it, or you can use python to see the contents
url = "https://s3.amazonaws.com/coderbyteprojectattachments/reatcodeltd-axldp-lkxhr3hf-CelticsvsRbLeipzig.csv"

df = pd.read_csv(url)  # You can use this dataframe as is or you can change the name


def best_passer(df, team_name):
    accurate_pass = df[["teamName", "matchName", "accuratePass"]]
    team_data = accurate_pass[accurate_pass["teamName"] == team_name]

    idx = team_data["accuratePass"].idxmax()
    max_acc_pass = team_data.loc[idx, "matchName"]

    print(max_acc_pass)


best_passer(df, "Celtic")


# Please do not touch this function, it is there to test if your answer is correct
def test_answer():
    assert best_passer(df, "Celtic") == "M. Jenz"
    assert best_passer(df, "RB Leipzig") == "J. Gvardiol"
