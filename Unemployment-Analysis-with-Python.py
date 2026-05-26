# Data handling
import pandas as pd
import numpy as np

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Ignore warnings
import warnings
warnings.filterwarnings('ignore')

# Load dataset
unemployment_df = pd.read_csv('Unemployment in India.csv')

# Display first 5 rows
print(unemployment_df.head())

# Dataset information
print(unemployment_df.info())

# Statistical summary
print(unemployment_df.describe())

# Column names
print(unemployment_df.columns)

# Remove Extra Spaces from Column Names
unemployment_df.columns = unemployment_df.columns.str.strip()

# Check for missing values
print(unemployment_df.isnull().sum())

# Remove Missing Values
unemployment_df.dropna(inplace=True)

# Convert Date Column into Datetime Format
unemployment_df['Date'] = pd.to_datetime(unemployment_df['Date'])


# Check Average Unemployment Rate
average_unemployment = unemployment_df['Estimated Unemployment Rate (%)'].mean()
print('Average Unemployment Rate:', average_unemployment)

# Highest Unemployment Regions
highest_unemployment_regions = unemployment_df.groupby('Region')['Estimated Unemployment Rate (%)'].mean().sort_values(ascending=False)
print('Highest Unemployment Regions:' , highest_unemployment_regions.head())

# Line Plot of Unemployment Rate Over Time
plt.figure(figsize=(12,6))

plt.plot(
    unemployment_df['Date'],
    unemployment_df['Estimated Unemployment Rate (%)']
)

plt.title('Unemployment Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.xticks(rotation=45)
plt.show()

# Covid-19 Impact Analysis
covid_data = unemployment_df[
    unemployment_df['Date'] >= '2020-03-01'
]

plt.figure(figsize=(12,6))

sns.lineplot(
    data=covid_data,
    x='Date',
    y='Estimated Unemployment Rate (%)'
)

plt.title('Impact of Covid-19 on Unemployment')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.xticks(rotation=45)
plt.show()

# State-wise Unemployment Rate
plt.figure(figsize=(14,8))

sns.barplot(
    data=unemployment_df,
    x='Region',
    y='Estimated Unemployment Rate (%)'
)

plt.xticks(rotation=90)
plt.title('State-wise Unemployment Rate')
plt.show()

# Heatmap for Correlation
plt.figure(figsize=(8,5))

sns.heatmap(
    unemployment_df.corr(numeric_only=True),
    annot=True,
    cmap='coolwarm'
)

plt.title('Correlation Heatmap')
plt.show()

# Extract Month and Year
unemployment_df['Month'] = unemployment_df['Date'].dt.month
unemployment_df['Year'] = unemployment_df['Date'].dt.year

# Monthly Average Unemployment
monthly_trend = unemployment_df.groupby('Month')['Estimated Unemployment Rate (%)'].mean()

plt.figure(figsize=(10,5))

monthly_trend.plot(marker='o')

plt.title('Monthly Unemployment Trend')
plt.xlabel('Month')
plt.ylabel('Average Unemployment Rate (%)')
plt.grid(True)
plt.show()