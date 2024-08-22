import pandas as pd

# Define data
data = {
    "Name": [
        "John Doe",
        "Jane Smith",
        "Bill Gates",
        "Elon Musk",
        "John Doe",
        None,
        "Steve Jobs",
        "Mark Zuckerberg",
        "Jack Dorsey",
        "Sundar Pichai",
    ],
    "Previous_Team": [
        "Team Alpha",
        "Team Bravo",
        "Team Charlie",
        "Team Delta",
        "Team Alpha",
        "Team Echo",
        "Team Foxtrot",
        "Team Golf",
        "Team Hotel",
        None,
    ],
    "Current_Team": [
        "Team Bravo",
        "Team Charlie",
        "Team Delta",
        "Team Echo",
        "Team Bravo",
        "Team Foxtrot",
        "Team Golf",
        "Team Hotel",
        "Team India",
        "Team Juliet",
    ],
    "Contract_Fee_Millions": [0, 15, 222, 180, 0, 37, 35, 76, 85, 42],
    "Contract_Transition_Date": [
        "2021-08-10",
        "2021-08-31",
        "2017-08-03",
        "2018-07-01",
        "2021-08-10",
        None,
        "2014-07-01",
        "2015-08-30",
        "2018-07-01",
        "2017-07-01",
    ],
}

# Create DataFrame
df = pd.DataFrame(data)
print(df, "\n")

print("Finding missing values:")
print(df.isnull().sum(), "\n")

# Fill null values with unknown for columns Name and Previous_Team
df["Name"] = df["Name"].fillna("Unknown")
df["Previous_Team"] = df["Previous_Team"].fillna("Unknown")


# Drop rows with missing contract transition dates
df = df.dropna(subset=["Contract_Transition_Date"])

print("Number of duplicates: ")
print(df.duplicated().sum(), "\n")

# removing duplicates
df.drop_duplicates(inplace=True)

# Define new column names
new_column_names = {
    "Name": "name",
    "Previous_Team": "previous_team",
    "Current_Team": "current_team",
    "Contract_Fee_Millions": "contract_fee_millions",
    "Contract_Transition_Date": "contract_transition_date",
}

# Rename columns
df = df.rename(columns=new_column_names)

# Replace 'Unknown' names with 'Undisclosed'
df["previous_team"] = df["previous_team"].replace("Unknown", "Undisclosed")

print("\nFinal DataFrame")
print(df)
