
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Step 1: Locate the repository folder
base_path = Path(__file__).resolve().parent.parent

# Step 2: Load the dataset
csv_path = (
    base_path
    / "Day6"
    / "Student_Performance_Analysis"
    / "student_performance.csv"
)

df = pd.read_csv(csv_path)

# Step 3: Select subject columns
subjects = [
    "Python",
    "Mathematics",
    "Statistics",
    "Machine_Learning"
]

# Step 4: Create the target column
df["Average_Score"] = df[subjects].mean(axis=1)

# Step 5: Select features and target
X = df[subjects]
y = df["Average_Score"]

# Step 6: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Step 7: Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 8: Predict scores for test data
y_pred = model.predict(X_test)

# Step 9: Compare actual and predicted scores
comparison = pd.DataFrame({
    "Actual_Score": y_test.values,
    "Predicted_Score": y_pred.round(2)
})

print("Actual vs Predicted Scores:")
print(comparison.to_string(index=False))

# Step 10: Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation Metrics:")
print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"R2 Score: {r2:.4f}")
