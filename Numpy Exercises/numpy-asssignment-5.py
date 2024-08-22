import pandas as pd
import numpy as np

# Load the data
# Do not change this line, this is the file you will be working on, if you want to check the contents of the file
# You can copy the link and download it, or you can use python to see the contents
df = pd.read_csv(
    "https://s3.amazonaws.com/coderbyteprojectattachments/reatcodeltd-axldp-o14h1x17-NapolivsAjax.csv"
)


def calculate_average_ball_recovery(df):
    grouping = df.groupby(["teamName", "position"])["ballRecovery"].mean()
    print(grouping)


calculate_average_ball_recovery(df)


# Please do not touch this function, it is there to test if your answer is correct
def test_calculate_average_ball_recovery():
    average_ball_recovery_result = calculate_average_ball_recovery(df)
    # The expected result from your data
    expected_result = pd.Series(
        {
            ("Ajax", "Defender"): 3.5,
            ("Ajax", "Goalkeeper"): 5.0,
            ("Ajax", "Midfielder"): 3.0,
            ("Ajax", "Striker"): 3.67,
            ("Ajax", "Substitute"): 0.36,
            ("Napoli", "Defender"): 4.75,
            ("Napoli", "Goalkeeper"): 2.0,
            ("Napoli", "Midfielder"): 4.0,
            ("Napoli", "Striker"): 2.67,
            ("Napoli", "Substitute"): 0.33,
        }
    )
    assert average_ball_recovery_result.round(2).equals(expected_result)
