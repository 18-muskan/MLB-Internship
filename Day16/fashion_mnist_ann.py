
# Day 16 - Fashion MNIST Classification using ANN

import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, Sequential
from tensorflow.keras.datasets import fashion_mnist

# Create output folder automatically
os.makedirs("outputs", exist_ok=True)

# Clothing class names
class_names = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]

print("=" * 50)
print("FASHION MNIST CLOTHING CLASSIFICATION")
print("=" * 50)

# Step 1: Load the dataset
print("\nLoading Fashion MNIST dataset...")
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

# Step 2: Explore the dataset
print("\nTraining images shape:", x_train.shape)
print("Training labels shape:", y_train.shape)
print("Testing images shape:", x_test.shape)
print("Testing labels shape:", y_test.shape)
print("First five labels:", y_train[:5])

# Step 3: Display sample images
plt.figure(figsize=(8, 4))

for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(x_train[i], cmap="gray")
    plt.title(class_names[y_train[i]], fontsize=8)
    plt.axis("off")

plt.tight_layout()
plt.savefig("outputs/sample_images.png")
plt.close()

# Step 4: Normalize pixel values
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

print("\nPixel values normalized from 0-255 to 0-1.")
print("Minimum pixel value:", x_train.min())
print("Maximum pixel value:", x_train.max())

# Step 5: Build the ANN model
model = Sequential([
    tf.keras.Input(shape=(28, 28)),
    layers.Flatten(name="Flatten_Layer"),
    layers.Dense(128, activation="relu", name="Hidden_Layer"),
    layers.Dense(10, activation="softmax", name="Output_Layer")
])

# Step 6: Compile the model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

print("\nANN Model Summary:")
model.summary()

# Step 7: Train the model
print("\nTraining model...")
history = model.fit(
    x_train,
    y_train,
    epochs=5,
    batch_size=32,
    validation_split=0.1,
    verbose=1
)

# Step 8: Evaluate on test data
print("\nEvaluating model...")
test_loss, test_accuracy = model.evaluate(
    x_test, y_test, verbose=0
)

print(f"\nFinal Training Accuracy: "
      f"{history.history['accuracy'][-1] * 100:.2f}%")
print(f"Final Validation Accuracy: "
      f"{history.history['val_accuracy'][-1] * 100:.2f}%")
print(f"Final Testing Accuracy: {test_accuracy * 100:.2f}%")

# Step 9: Plot training and validation accuracy
plt.figure(figsize=(8, 5))
plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.title("Fashion MNIST - Model Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/accuracy_graph.png")
plt.close()

# Step 10: Predict five test images
predictions = model.predict(x_test[:5], verbose=0)
predicted_labels = np.argmax(predictions, axis=1)

print("\nSample Predictions:")

plt.figure(figsize=(10, 4))

for i in range(5):
    predicted = class_names[predicted_labels[i]]
    actual = class_names[y_test[i]]

    print(f"Image {i + 1}: Predicted = {predicted}, "
          f"Actual = {actual}")

    plt.subplot(1, 5, i + 1)
    plt.imshow(x_test[i], cmap="gray")
    plt.title(f"Pred: {predicted}\nActual: {actual}", fontsize=8)
    plt.axis("off")

plt.tight_layout()
plt.savefig("outputs/sample_predictions.png")
plt.close()

# Step 11: Save the trained model
model.save("outputs/fashion_mnist_model.keras")

print("\nSaved files in the outputs folder:")
print("- sample_images.png")
print("- accuracy_graph.png")
print("- sample_predictions.png")
print("- fashion_mnist_model.keras")
print("\nMini project completed successfully!")
