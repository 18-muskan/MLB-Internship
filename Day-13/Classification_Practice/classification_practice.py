
# Day 13 - Classification Practice
# Iris dataset and model evaluation

from pathlib import Path

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

# 1. Load the Iris dataset
iris = load_iris()

X = iris.data
y = iris.target

print("===== Iris Dataset Information =====")
print("Features:", iris.feature_names)
print("Target Classes:", iris.target_names)
print("Total Samples:", len(X))
print("Dataset Shape:", X.shape)

# 2. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\n===== Training and Testing Data =====")
print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# 3. Train the Logistic Regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

print("\nLogistic Regression model trained successfully!")

# 4. Make predictions
y_pred = model.predict(X_test)

# 5. Evaluate model performance
print("\n===== Model Evaluation =====")

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(
    y_test, y_pred, average="weighted", zero_division=0
)
recall = recall_score(
    y_test, y_pred, average="weighted", zero_division=0
)
f1 = f1_score(
    y_test, y_pred, average="weighted", zero_division=0
)

print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-Score:  {f1:.4f}")

# 6. Display the classification report
print("\n===== Classification Report =====")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=iris.target_names,
        zero_division=0
    )
)

# 7. Generate the confusion matrix
cm = confusion_matrix(y_test, y_pred)

print("===== Confusion Matrix =====")
print(cm)

# 8. Save the confusion matrix inside this script's folder
output_path = Path(__file__).resolve().parent / "confusion_matrix.png"

matrix_display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=iris.target_names
)

matrix_display.plot(cmap="Blues")
plt.title("Iris Classification - Confusion Matrix")
plt.tight_layout()
plt.savefig(output_path, dpi=300, bbox_inches="tight")

print("\nConfusion matrix saved successfully!")
print("Image location:", output_path)

# 9. Show the confusion matrix
plt.show()
