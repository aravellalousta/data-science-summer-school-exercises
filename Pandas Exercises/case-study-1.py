import pandas as pd

# Define data
data = {
    'Name': ['John Doe', 'Jane Smith', 'Mike Brown', 'Alice Johnson', 'Charlie Davis', 'Elizabeth Green', 'James White', 'Linda Miller', 'David Clark', 'Jennifer Rodriguez'],
    'Occupation': ['Engineer', 'Doctor', 'Lawyer', 'Artist', 'Scientist', 'Teacher', 'Nurse', 'Journalist', 'Actor', 'Architect'],
    'Age': [30, 28, 29, 32, 31, 30, 32, 33, 32, 30],
    'Experience': [5, 3, 4, 2, 5, 2, 3, 1, 2, 4],
    'Projects': [12, 7, 15, 11, 7, 16, 2, 10, 11, 6],
    'Sick_Days': [1, 3, 4, 2, 1, 2, 3, 1, 2, 2],
    'Vacation_Days': [10, 12, 15, 12, 10, 9, 11, 13, 10, 14]
}

# Create & Print DataFrame
df = pd.DataFrame(data)
print(df)

# Print the descriptive statistics for the DataFrame
print('DataFrame Statistics:')
print(df.describe(), '\n')

# Print the mean number of years of experience
print('Mean Experience:', df['Experience'].mean(), '\n')

# Print the individual with the most projects
print('Individual with Most Projects:', df['Name'][df['Projects'].idxmax()], '\n')

# Print the 'Name' and 'Experience' columns for all individuals who have more than 5 years of experience
print('Individuals with More Than 5 Years of Experience:')
print(df.loc[df['Experience'] > 5, ['Name', 'Experience']], '\n')

# Print the row for 'John Doe'
print('Row for John Doe:')
print(df.loc[df['Name'] == 'John Doe'])