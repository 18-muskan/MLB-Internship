
# Day 13 - Iris Flower Classification System
# Predicting flower species using Logistic Regression

from pathlib import Path

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

# 1. Load and explore the Iris dataset
iris = load_iris()

X = iris.data
y = iris.target

print("===== IRIS FLOWER CLASSIFICATION SYSTEM =====")
print("Features:", iris.feature_names)
print("Flower Species:", iris.target_names)
print("Total Samples:", len(X))
print("Dataset Shape:", X.shape)

# 2. Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# 3. Train Logistic Regression
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# 4. Predict flower species
y_pred = model.predict(X_test)

# 5. Evaluate Logistic Regression
print("\n===== LOGISTIC REGRESSION RESULTS =====")

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

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=iris.target_names,
        zero_division=0
    )
)

# 6. Display confusion matrix
cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix:")
print(cm)

# Save confusion matrix inside the project folder
output_path = Path(__file__).resolve().parent / "iris_confusion_matrix.png"

matrix_display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=iris.target_names
)

matrix_display.plot(cmap="Blues")
plt.title("Iris Flower Classification - Confusion Matrix")
plt.tight_layout()
plt.savefig(output_path, dpi=300, bbox_inches="tight")
print("\nConfusion matrix saved at:", output_path)

plt.show()

# 7. Show sample predictions with actual values
print("\n===== SAMPLE FLOWER PREDICTIONS =====")

for i in range(min(10, len(X_test))):
    predicted_species = iris.target_names[y_pred[i]]
    actual_species = iris.target_names[y_test[i]]

    print(
        f"Sample {i + 1}: "
        f"Predicted = {predicted_species}, "
        f"Actual = {actual_species}"
    )

# 8. Bonus: Train and compare Decision Tree
tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train, y_train)

tree_pred = tree_model.predict(X_test)

tree_accuracy = accuracy_score(y_test, tree_pred)
tree_precision = precision_score(
    y_test, tree_pred, average="weighted", zero_division=0
)
tree_recall = recall_score(
    y_test, tree_pred, average="weighted", zero_division=0
)
tree_f1 = f1_score(
    y_test, tree_pred, average="weighted", zero_division=0
)

print("\n===== MODEL COMPARISON =====")
print("Metric          Logistic Regression    Decision Tree")
print(f"Accuracy        {accuracy:.4f}                 {tree_accuracy:.4f}")
print(f"Precision       {precision:.4f}                 {tree_precision:.4f}")
print(f"Recall          {recall:.4f}                 {tree_recall:.4f}")
print(f"F1-Score        {f1:.4f}                 {tree_f1:.4f}")

print("\nProject completed successfully!")
