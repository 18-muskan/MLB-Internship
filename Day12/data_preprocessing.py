
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split

# Step 1: Find the repository folder
base_path = Path(__file__).resolve().parent.parent

# Step 2: Load the dataset
csv_path = (
    base_path
    / "Day6"
    / "Student_Performance_Analysis"
    / "student_performance.csv"
)

df = pd.read_csv(csv_path)

print("Original Dataset:")
print(df.head())

print("\nDataset Shape:", df.shape)

# Step 3: Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 4: Select subject columns
subjects = [
    "Python",
    "Mathematics",
    "Statistics",
    "Machine_Learning"
]

# Step 5: Create Average_Score
df["Average_Score"] = df[subjects].mean(axis=1)

print("\nAverage Scores:")
print(df[["Name", "Average_Score"]].head())

# Step 6: Select features (X) and target (y)
X = df[subjects]
y = df["Average_Score"]

# Step 7: Split into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Step 8: Display split information
print("\nTraining Features Shape:", X_train.shape)
print("Testing Features Shape:", X_test.shape)
print("Training Target Shape:", y_train.shape)
print("Testing Target Shape:", y_test.shape)

print("\nData preprocessing completed successfully!")
