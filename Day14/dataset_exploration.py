
# Day 14 - Dataset Exploration
# Load and explore the Breast Cancer dataset

from sklearn.datasets import load_breast_cancer
import pandas as pd

# Step 1: Load the built-in dataset
data = load_breast_cancer()

print("Dataset loaded successfully!")

# Step 2: Convert dataset into a Pandas DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)

# Add target column
df["target"] = data.target

# Step 3: Display first five rows
print("\nFirst Five Rows:")
print(df.head())

# Step 4: Display dataset information
print("\nDataset Information:")
df.info()

# Step 5: Display statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Step 6: Check target class distribution
print("\nTarget Class Distribution:")
print(df["target"].value_counts())

# Display target class names
print("\nTarget Class Names:")
print(data.target_names)
