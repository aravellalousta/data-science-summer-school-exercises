import pandas as pd

# Load the data
# Do not change this line, this is the file you will be working on, if you want to check the contents of the file
# You can copy the link and download it, or you can use python to see the contents
url = "https://s3.amazonaws.com/coderbyteprojectattachments/reatcodeltd-axldp-lkxhr3hf-CelticsvsRbLeipzig.csv"
df = pd.read_csv(url)


def most_efficient_sub(df):

    filtered_df = df[
        [
            "teamName",
            "matchName",
            "position",
            "successfulFinalThirdPasses",
            "minsPlayed",
        ]
    ]

    filtered_df["pass_per_min"] = (
        filtered_df["successfulFinalThirdPasses"] / filtered_df["minsPlayed"]
    )

    filtered_df = filtered_df.dropna()

    team_data = filtered_df[filtered_df["position"] == "Substitute"]

    result = team_data.loc[team_data["pass_per_min"].idxmax(), "matchName"]
    print(result)



most_efficient_sub(df)


# Please do not touch this function, it is there to test if your answer is correct
def test_answer():
    assert most_efficient_sub(df) == "Hugo Novoa"
