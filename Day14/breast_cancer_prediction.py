
# Day 14 - Breast Cancer Prediction System
# Complete Machine Learning Pipeline

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)
import matplotlib.pyplot as plt

# Step 1: Load the dataset
data = load_breast_cancer()

X = data.data
y = data.target

print("=" * 50)
print("BREAST CANCER PREDICTION SYSTEM")
print("=" * 50)

print("\nDataset loaded successfully!")
print("Total samples:", X.shape[0])
print("Total features:", X.shape[1])

# Step 2: Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])

# Step 3: Create the baseline pipeline
baseline_model = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(max_iter=5000))
])

# Step 4: Train the baseline model
baseline_model.fit(X_train, y_train)

# Step 5: Make baseline predictions
baseline_pred = baseline_model.predict(X_test)

# Step 6: Evaluate the baseline model
baseline_accuracy = accuracy_score(y_test, baseline_pred)
baseline_precision = precision_score(
    y_test, baseline_pred, pos_label=1
)
baseline_recall = recall_score(
    y_test, baseline_pred, pos_label=1
)
baseline_f1 = f1_score(
    y_test, baseline_pred, pos_label=1
)

print("\n===== BASELINE MODEL RESULTS =====")
print("Accuracy:", round(baseline_accuracy, 4))
print("Precision (benign):", round(baseline_precision, 4))
print("Recall (benign):", round(baseline_recall, 4))
print("F1-Score (benign):", round(baseline_f1, 4))

print("\nBaseline Confusion Matrix:")
print(confusion_matrix(y_test, baseline_pred))

# Step 7: Create the hyperparameter grid
param_grid = {
    "model__C": [0.01, 0.1, 1, 10, 100],
    "model__solver": ["liblinear", "lbfgs"]
}

# Step 8: Apply GridSearchCV
grid_search = GridSearchCV(
    estimator=Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=5000))
    ]),
    param_grid=param_grid,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)

# Step 9: Train and tune the model
grid_search.fit(X_train, y_train)

best_model = grid_search.best_estimator_
tuned_pred = best_model.predict(X_test)

# Step 10: Evaluate the tuned model
tuned_accuracy = accuracy_score(y_test, tuned_pred)
tuned_precision = precision_score(
    y_test, tuned_pred, pos_label=1
)
tuned_recall = recall_score(
    y_test, tuned_pred, pos_label=1
)
tuned_f1 = f1_score(
    y_test, tuned_pred, pos_label=1
)

print("\n===== HYPERPARAMETER TUNING =====")
print("Best Parameters:", grid_search.best_params_)
print("Best Cross-Validation Accuracy:",
      round(grid_search.best_score_, 4))

print("\n===== TUNED MODEL RESULTS =====")
print("Accuracy:", round(tuned_accuracy, 4))
print("Precision (benign):", round(tuned_precision, 4))
print("Recall (benign):", round(tuned_recall, 4))
print("F1-Score (benign):", round(tuned_f1, 4))

print("\nTuned Confusion Matrix:")
print(confusion_matrix(y_test, tuned_pred))

print("\nClassification Report:")
print(classification_report(
    y_test,
    tuned_pred,
    target_names=data.target_names
))

# Step 11: Compare baseline and tuned performance
print("\n===== MODEL COMPARISON =====")
print(f"Baseline Accuracy: {baseline_accuracy:.4f}")
print(f"Tuned Accuracy:    {tuned_accuracy:.4f}")

if tuned_accuracy > baseline_accuracy:
    print("Observation: Tuning improved test accuracy.")
elif tuned_accuracy < baseline_accuracy:
    print("Observation: Baseline model performed better.")
else:
    print("Observation: Both models have the same test accuracy.")

# Step 12: Save the tuned model confusion matrix
ConfusionMatrixDisplay.from_predictions(
    y_test,
    tuned_pred,
    display_labels=data.target_names,
    cmap="Blues"
)

plt.title("Tuned Model - Confusion Matrix")
plt.tight_layout()
plt.savefig("confusion_matrix.png", dpi=300)
plt.close()

print("\nConfusion matrix image saved as confusion_matrix.png")
print("\nPipeline completed successfully!")
