
import pandas as pd
from pathlib import Path

# Get the folder where this script is saved
BASE_DIR = Path(__file__).resolve().parent

# Path of the original dataset
DATA_PATH = (
    BASE_DIR.parent
    / "Day6"
    / "Student_Performance_Analysis"
    / "student_performance.csv"
)

# Load the dataset
df = pd.read_csv(DATA_PATH)

print("Original Dataset Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Rename columns
df = df.rename(columns={
    "Student_ID": "Student_ID",
    "Machine_Learning": "Machine_Learning"
})

# Identify subject columns
subjects = ["Python", "Mathematics", "Statistics", "Machine_Learning"]

# Handle missing subject marks using the subject average
for subject in subjects:
    df[subject] = pd.to_numeric(df[subject], errors="coerce")
    df[subject] = df[subject].fillna(df[subject].mean())

# Create Average_Score column
df["Average_Score"] = df[subjects].mean(axis=1).round(2)

# Create Performance category
def get_performance(score):
    if score >= 90:
        return "Excellent"
    elif score >= 80:
        return "Good"
    elif score >= 70:
        return "Average"
    else:
        return "Needs Improvement"

df["Performance"] = df["Average_Score"].apply(get_performance)

# Sort students by average score
df = df.sort_values(by="Average_Score", ascending=False)

# Save the cleaned dataset
output_path = BASE_DIR / "cleaned_student_performance.csv"
df.to_csv(output_path, index=False)

print("\nCleaned Dataset Shape:", df.shape)
print("\nPerformance Distribution:")
print(df["Performance"].value_counts())

print("\nCleaned Dataset Preview:")
print(df.head())

print("\nCleaned dataset saved at:")
print(output_path)
