import pandas as pd

# Load the data
# Do not change this line, this is the file you will be working on, if you want to check the contents of the file
# You can copy the link and download it, or you can use python to see the contents
url = "https://s3.amazonaws.com/coderbyteprojectattachments/reatcodeltd-axldp-lkxhr3hf-CelticsvsRbLeipzig.csv"
df = pd.read_csv(url)


def best_performance(df):
    most_touches = df[df["touches"] == df["touches"].max()]["matchName"].values[0]
    print(most_touches)


best_performance(df)
