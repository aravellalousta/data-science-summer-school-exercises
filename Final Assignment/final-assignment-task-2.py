import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime


# Load the dataset
df = pd.read_csv("https://storage.googleapis.com/courses_data/Assignment%20CSV/finance_liquor_sales.csv")

# Filter out the dates outside the timeframe 2016-2019
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
filtered_df = df[(df['date'] > pd.Timestamp('2016-01-01')) & (df['date'] < pd.Timestamp('2020-01-01'))]

# Keep only essential columns for analysis
data = filtered_df[['store_name', 'sale_dollars']]

# Total sales per store
store_sales = data.groupby('store_name')['sale_dollars'].sum().reset_index()
print(store_sales)

# Overall sales
total_sales = data['sale_dollars'].sum()

# Percentage of sales per store
store_sales['percentage_of_sales'] = (store_sales['sale_dollars'] * 100 / total_sales).round(2)

# Sorting by asceding order and keeping the 20 bottom rows 
sorted_df = store_sales.sort_values(['percentage_of_sales'], ascending=True).tail(20)

# Adjusting the plot size and labels, adding labels to each bar 
plt.figure(figsize=(15,6))
plt.barh(sorted_df['store_name'], sorted_df['percentage_of_sales'], color='orange')
plt.xlabel("Percentage of sales")
plt.ylabel("Store Name")
plt.title("Sales percentage per store")

for index, value in enumerate(sorted_df['percentage_of_sales']):
    plt.text(value, index,
             str(value))

plt.tight_layout()
plt.show()
