
import os
import matplotlib.pyplot as plt
import tensorflow as tf

# Day22 folder path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Existing trained model
MODEL_PATH = os.path.join(
    BASE_DIR, "results", "cats_dogs_mobilenetv2.keras"
)

# Graphs folder
GRAPHS_DIR = os.path.join(BASE_DIR, "graphs")
os.makedirs(GRAPHS_DIR, exist_ok=True)

# Load existing model
print("Loading existing trained model...")

model = tf.keras.models.load_model(MODEL_PATH)

print("Model loaded successfully!")
print("No training will be performed.")

# Actual training results from previous run
epochs = [1, 2, 3, 4]

training_accuracy = [97.66, 98.44, 98.80, 99.05]
validation_accuracy = [98.32, 98.58, 98.41, 98.24]

training_loss = [0.0652, 0.0431, 0.0334, 0.0251]
validation_loss = [0.0511, 0.0401, 0.0484, 0.0514]

# Accuracy Graph
plt.figure(figsize=(8, 5))

plt.plot(epochs, training_accuracy, marker="o",
         label="Training Accuracy")

plt.plot(epochs, validation_accuracy, marker="o",
         label="Validation Accuracy")

plt.title("Cats vs Dogs - Model Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy (%)")
plt.xticks(epochs)
plt.legend()
plt.grid(True)

plt.savefig(os.path.join(GRAPHS_DIR, "accuracy.png"))
plt.close()

# Loss Graph
plt.figure(figsize=(8, 5))

plt.plot(epochs, training_loss, marker="o",
         label="Training Loss")

plt.plot(epochs, validation_loss, marker="o",
         label="Validation Loss")

plt.title("Cats vs Dogs - Model Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.xticks(epochs)
plt.legend()
plt.grid(True)

plt.savefig(os.path.join(GRAPHS_DIR, "loss.png"))
plt.close()

print("\nAccuracy graph saved successfully!")
print("Loss graph saved successfully!")
print("\nBoth graphs are saved inside Day22/graphs.")
print("Practice completed successfully!")
