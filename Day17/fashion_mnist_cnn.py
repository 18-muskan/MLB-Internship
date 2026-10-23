
# Day 17 - Fashion MNIST CNN Model

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

# Create output folders inside Day17
BASE_DIR = Path(__file__).parent
GRAPH_DIR = BASE_DIR / "outputs" / "graphs"
PREDICTION_DIR = BASE_DIR / "outputs" / "predictions"
CONFUSION_DIR = BASE_DIR / "outputs" / "confusion_matrix"

for folder in [GRAPH_DIR, PREDICTION_DIR, CONFUSION_DIR]:
    folder.mkdir(parents=True, exist_ok=True)

# Load Fashion MNIST
print("Loading Fashion MNIST...")
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

class_names = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]

# Normalize and reshape images
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

# Build CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),

    Conv2D(64, (3, 3), activation="relu"),
    MaxPooling2D((2, 2)),

    Flatten(),
    Dense(128, activation="relu"),
    Dropout(0.3),
    Dense(10, activation="softmax")
])

# Configure model training
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

print("\nCNN Model Summary:")
model.summary()

# Train the model
print("\nTraining CNN model...")
history = model.fit(
    x_train,
    y_train,
    epochs=5,
    batch_size=64,
    validation_split=0.1
)

# Evaluate on unseen test data
print("\nEvaluating on test data...")
test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=1)

print(f"\nFinal Test Loss: {test_loss:.4f}")
print(f"Final Test Accuracy: {test_accuracy * 100:.2f}%")

# Save the trained model inside Day17
model_path = BASE_DIR / "fashion_mnist_cnn.keras"
model.save(model_path)
print("Model saved at:", model_path)

# Plot training and validation accuracy
plt.figure(figsize=(8, 5))
plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.title("CNN Training and Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.tight_layout()
plt.savefig(GRAPH_DIR / "cnn_accuracy.png", dpi=150)
plt.close()

# Plot training and validation loss
plt.figure(figsize=(8, 5))
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.title("CNN Training and Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.tight_layout()
plt.savefig(GRAPH_DIR / "cnn_loss.png", dpi=150)
plt.close()

# Predict the first 10 test images
predictions = model.predict(x_test[:10], verbose=0)
predicted_labels = np.argmax(predictions, axis=1)

print("\nSample Predictions:")
for i in range(10):
    print(
        f"Image {i + 1}: Actual = {class_names[y_test[i]]}, "
        f"Predicted = {class_names[predicted_labels[i]]}"
    )

# Save sample predictions as a graph
plt.figure(figsize=(12, 6))

for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(x_test[i].squeeze(), cmap="gray")
    color = "green" if predicted_labels[i] == y_test[i] else "red"
    plt.title(
        f"Pred: {class_names[predicted_labels[i]]}\n"
        f"Actual: {class_names[y_test[i]]}",
        color=color,
        fontsize=8
    )
    plt.axis("off")

plt.suptitle("Fashion MNIST CNN Predictions")
plt.tight_layout()
plt.savefig(PREDICTION_DIR / "sample_predictions.png", dpi=150)
plt.close()

print("\nAll graphs and predictions saved inside Day17/outputs.")
print("CNN project completed successfully!")
