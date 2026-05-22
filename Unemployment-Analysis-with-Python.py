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

