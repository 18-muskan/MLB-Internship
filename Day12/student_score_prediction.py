
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Step 1: Locate the repository and required files
base_path = Path(__file__).resolve().parent.parent
graphs_path = Path(__file__).resolve().parent / "graphs"
graphs_path.mkdir(parents=True, exist_ok=True)

csv_path = (
    base_path
    / "Day6"
    / "Student_Performance_Analysis"
    / "student_performance.csv"
)

# Step 2: Load the dataset
df = pd.read_csv(csv_path)

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)

# Step 3: Select subject columns
subjects = [
    "Python",
    "Mathematics",
    "Statistics",
    "Machine_Learning"
]

# Step 4: Create Average_Score
df["Average_Score"] = df[subjects].mean(axis=1)

print("\nAverage scores:")
print(df[["Name", "Average_Score"]].head())

# Step 5: Select features and target
X = df[subjects]
y = df["Average_Score"]

# Step 6: Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Step 7: Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

print("\nModel trained successfully!")

# Step 8: Predict average scores
y_pred = model.predict(X_test)

# Step 9: Compare actual and predicted scores
comparison = pd.DataFrame({
    "Actual_Score": y_test.values,
    "Predicted_Score": y_pred.round(2)
})

print("\nActual vs Predicted Scores:")
print(comparison.to_string(index=False))

# Step 10: Calculate evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"R2 Score: {r2:.4f}")

# Step 11: Create Actual vs Predicted scatter plot
plt.figure(figsize=(8, 6))

plt.scatter(y_test, y_pred, alpha=0.8, label="Predictions")

# Reference line for perfect predictions
min_score = min(y_test.min(), y_pred.min())
max_score = max(y_test.max(), y_pred.max())

plt.plot(
    [min_score, max_score],
    [min_score, max_score],
    linestyle="--",
    label="Perfect Prediction"
)

plt.xlabel("Actual Average Score")
plt.ylabel("Predicted Average Score")
plt.title("Actual vs Predicted Student Scores")
plt.legend()
plt.grid(True)

# Step 12: Save the graph
graph_file = graphs_path / "actual_vs_predicted.png"
plt.savefig(graph_file, dpi=300, bbox_inches="tight")
plt.close()

print("\nGraph saved at:", graph_file)
print("\nStudent Score Prediction System completed!")
