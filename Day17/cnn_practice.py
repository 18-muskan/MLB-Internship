
# Day 17 - CNN Practice
# Practice 1: Load and visualize Fashion MNIST dataset
from pathlib import Path
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import fashion_mnist

# Load the Fashion MNIST dataset
print("Loading Fashion MNIST dataset...")

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

# Names of the 10 clothing classes
class_names = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot"
]

# Display dataset information
print("\nDataset loaded successfully!")
print("Training images:", x_train.shape)
print("Training labels:", y_train.shape)
print("Testing images:", x_test.shape)
print("Testing labels:", y_test.shape)

# Display the first 10 sample images
plt.figure(figsize=(12, 6))

for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(x_train[i], cmap="gray")
    plt.title(class_names[y_train[i]])
    plt.axis("off")

plt.suptitle("Fashion MNIST - 10 Sample Images")
plt.tight_layout()

# Save the sample image visualization
# Save the image inside Day17/outputs/graphs
output_folder = Path(__file__).parent / "outputs" / "graphs"
output_folder.mkdir(parents=True, exist_ok=True)

image_path = output_folder / "fashion_mnist_samples.png"
plt.savefig(image_path, dpi=150)

print("Image saved at:", image_path)

# Display the images
plt.show()


# Practice 2: Normalize images and prepare them for CNN

print("\nPreparing images for CNN...")

# Convert pixel values from 0-255 to 0-1
x_train_normalized = x_train.astype("float32") / 255.0
x_test_normalized = x_test.astype("float32") / 255.0

# Add a channel dimension for grayscale images
x_train_cnn = x_train_normalized.reshape(60000, 28, 28, 1)
x_test_cnn = x_test_normalized.reshape(10000, 28, 28, 1)

# Display the new shapes and pixel range
print("\nNormalization completed!")
print("Training data shape:", x_train_cnn.shape)
print("Testing data shape:", x_test_cnn.shape)
print("Minimum pixel value:", x_train_cnn.min())
print("Maximum pixel value:", x_train_cnn.max())
print("First image label:", y_train[0])
print("First image class:", class_names[y_train[0]])

