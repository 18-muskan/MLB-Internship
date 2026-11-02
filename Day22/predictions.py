
import os
import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt

# Day22 folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Existing trained model
MODEL_PATH = os.path.join(
    BASE_DIR, "results", "cats_dogs_mobilenetv2.keras"
)

# Prediction output folder
OUTPUT_DIR = os.path.join(
    BASE_DIR, "predictions", "sample_predictions"
)

os.makedirs(OUTPUT_DIR, exist_ok=True)

IMG_SIZE = 160

print("Loading existing trained model...")

model = tf.keras.models.load_model(MODEL_PATH)

print("Model loaded successfully!")
print("No training will be performed.")

# Load test images
print("\nLoading test images...")

test_data = tfds.load(
    "cats_vs_dogs",
    split="train[90%:]",
    as_supervised=True
)

class_names = ["Cat", "Dog"]

# Generate predictions for 10 images
count = 0

for image, label in test_data.take(10):

    # Prepare image
    resized_image = tf.image.resize(
        image, (IMG_SIZE, IMG_SIZE)
    )

    processed_image = tf.keras.applications.mobilenet_v2.preprocess_input(
        resized_image
    )

    input_image = tf.expand_dims(processed_image, axis=0)

    # Predict
    prediction = model.predict(input_image, verbose=0)

    predicted_class = 1 if prediction[0][0] >= 0.5 else 0
    actual_class = int(label.numpy())

    predicted_name = class_names[predicted_class]
    actual_name = class_names[actual_class]

    print("\nImage:", count + 1)
    print("Actual:", actual_name)
    print("Predicted:", predicted_name)

    # Save prediction image
    plt.figure(figsize=(5, 5))
    plt.imshow(image.numpy().astype("uint8"))
    plt.title(
        f"Actual: {actual_name} | Predicted: {predicted_name}"
    )
    plt.axis("off")

    image_path = os.path.join(
        OUTPUT_DIR, f"prediction_{count + 1}.png"
    )

    plt.savefig(image_path, bbox_inches="tight")
    plt.close()

    count += 1

print("\nAll predictions completed!")
print("Prediction images saved in:", OUTPUT_DIR)
