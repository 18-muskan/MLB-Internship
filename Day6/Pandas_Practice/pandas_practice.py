import pandas as pd

# 1. Load the dataset
df = pd.read_csv("Day6/Pandas_Practice/students.csv")

print("===== STUDENT DATASET =====")
print(df)

# 2. Display the first five rows
print("\n===== FIRST FIVE ROWS =====")
print(df.head())

# 3. Display the last five rows
print("\n===== LAST FIVE ROWS =====")
print(df.tail())

# 4. Display dataset information
print("\n===== DATASET INFORMATION =====")
df.info()

# 5. Find missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# 6. Filter data based on a condition
print("\n===== STUDENTS WITH MARKS GREATER THAN 80 =====")
filtered_data = df[df["Marks"] > 80]
print(filtered_data)

# 7. Calculate summary statistics
print("\n===== SUMMARY STATISTICS =====")
print(df.describe())

print("\nPandas practice completed successfully!")