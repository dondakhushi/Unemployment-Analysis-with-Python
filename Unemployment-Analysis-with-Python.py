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