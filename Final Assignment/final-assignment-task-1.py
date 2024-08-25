import pandas as pd
import numpy as np
import plotly.graph_objects as go
import datetime


# Load the dataset
df = pd.read_csv("https://storage.googleapis.com/courses_data/Assignment%20CSV/finance_liquor_sales.csv")

# Filter out the dates outside the timeframe 2016-2019
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
filtered_df = df[(df['date'] > pd.Timestamp('2016-01-01')) & (df['date'] < pd.Timestamp('2020-01-01'))]

# Keep only essential columns for analysis
data = filtered_df[['zip_code', 'item_number', 'bottles_sold']]

# Convert zip code from float to int
data['zip_code'] = data['zip_code'].apply(np.int64)

# Group and aggregate
grouped_data = data.groupby(['zip_code', 'item_number'])['bottles_sold'].sum().reset_index()
sorted_grouped = grouped_data.sort_values(['zip_code', 'bottles_sold'], ascending=[True, False])
most_popular_items = sorted_grouped.drop_duplicates(subset='zip_code', keep='first') #keeping the first because it has the biggest value after sorting

color_values = most_popular_items['bottles_sold']

# Create hover text
hover_text = most_popular_items.apply(
    lambda row: f'Zip Code: {row["zip_code"]}<br>Item Number: {row["item_number"]}<br>Bottles Sold: {row["bottles_sold"]}',
    axis=1
)


# Visualizing using Plotlib
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=most_popular_items["zip_code"],
        y=most_popular_items["bottles_sold"],
        mode="markers",
        marker=dict(
            size=10,
            color=color_values,        
            colorscale='rainbow',  
            colorbar=dict(title='Amount Sold'),  
            showscale=True         
        ),
        text=hover_text
    )
)

fig.update_layout(
    title="Most Popular Item in each Zip code",
    xaxis_title="Zip Code",
    yaxis_title="Bottles Sold",
    legend=dict(x=0, y=1, bgcolor="rgba(255, 255, 255, 0.5)"),
    plot_bgcolor="rgba(0, 0, 0, 0)",
    hovermode="x unified",
)

fig.show()