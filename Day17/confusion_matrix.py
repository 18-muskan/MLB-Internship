
# Day 17 - Confusion Matrix
# Use the already trained model. No retraining required.

import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path
from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import fashion_mnist
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Set folder paths
BASE_DIR = Path(__file__).parent
MODEL_PATH = BASE_DIR / "fashion_mnist_cnn.keras"
OUTPUT_DIR = BASE_DIR / "outputs" / "confusion_matrix"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Clothing class names
class_names = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]

# Load the saved model (no training)
print("Loading saved CNN model...")
model = load_model(MODEL_PATH)

# Load test data
print("Loading Fashion MNIST test data...")
(_, _), (x_test, y_test) = fashion_mnist.load_data()

# Normalize and reshape test images
x_test = x_test.astype("float32") / 255.0
x_test = x_test.reshape(-1, 28, 28, 1)

# Predict test images
print("Predicting test images...")
probabilities = model.predict(x_test, batch_size=64, verbose=1)
y_pred = np.argmax(probabilities, axis=1)

# Generate confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Plot and save confusion matrix
display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=class_names
)

fig, ax = plt.subplots(figsize=(11, 9))
display.plot(ax=ax, cmap="Blues", xticks_rotation=45, colorbar=False)
plt.title("Fashion MNIST CNN - Confusion Matrix")
plt.tight_layout()

image_path = OUTPUT_DIR / "confusion_matrix.png"
plt.savefig(image_path, dpi=150, bbox_inches="tight")
plt.close()

# Show accuracy and save location
accuracy = np.mean(y_pred == y_test) * 100

print(f"\nTest Accuracy: {accuracy:.2f}%")
print("Confusion matrix saved at:", image_path)
print("\nConfusion Matrix:")
print(cm)
print("\nCompleted! Model was not retrained.")
