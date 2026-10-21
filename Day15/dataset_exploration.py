
# Day 15 - Iris Dataset Exploration

import pandas as pd
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()

# Convert dataset into a Pandas DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add actual flower species names for exploration
df["species"] = [iris.target_names[i] for i in iris.target]

# Display the first five rows
print("===== IRIS DATASET EXPLORATION =====")
print("\nFirst five rows:")
print(df.head())

# Display dataset information
print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nDataset information:")
df.info()

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Display statistical summary
print("\nStatistical summary:")
print(df.describe())

# Display flower species counts
print("\nFlower species counts:")
print(df["species"].value_counts())

print("\nDataset exploration completed successfully!")
