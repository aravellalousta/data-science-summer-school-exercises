import pandas as pd
import numpy as np

# Load the data
# Do not change this line, this is the file you will be working on, if you want to check the contents of the file
# You can copy the link and download it, or you can use python to see the contents
df = pd.read_csv(
    "https://s3.amazonaws.com/coderbyteprojectattachments/reatcodeltd-axldp-o14h1x17-NapolivsAjax.csv"
)


def get_average_successful_final_third_passes(df):
    # Group teams
    groups = df.groupby("teamName")["successfulFinalThirdPasses"].mean()
    print(groups)


get_average_successful_final_third_passes(df)
