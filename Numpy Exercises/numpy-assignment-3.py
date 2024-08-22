import pandas as pd
import numpy as np

df = pd.read_csv(
    "https://s3.amazonaws.com/coderbyteprojectattachments/reatcodeltd-axldp-o14h1x17-NapolivsAjax.csv"
)


def get_num_of_substitutes(df):
    substitutes = df[df["gameStarted"] == 0]
    subs = substitutes.groupby("teamName")["gameStarted"].count()
    print(subs)


get_num_of_substitutes(df)
