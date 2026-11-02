
import tensorflow as tf

print("TensorFlow Version:", tf.__version__)

# Step 1: Load the pre-trained MobileNetV2 model

base_model = tf.keras.applications.MobileNetV2(
    weights="imagenet",
    include_top=False,
    input_shape=(224, 224, 3)
)

print("\nMobileNetV2 model loaded successfully!")

# Step 2: Explore the model architecture

print("\nMobileNetV2 Architecture:")
base_model.summary()

# Step 3: Freeze the base model layers

base_model.trainable = False

print("\nBase Model Layers Frozen Successfully!")

# Step 4: Add our own classification head

model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(1, activation="sigmoid")
])

# Step 5: Compile the model

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# Step 6: Display the complete model architecture

print("\nComplete Transfer Learning Model:")
model.summary()

# Step 7: Display trainable and non-trainable parameters

print("\nTrainable Parameters:", sum(
    tf.size(weight).numpy()
    for weight in model.trainable_weights
))

print("Non-Trainable Parameters:", sum(
    tf.size(weight).numpy()
    for weight in model.non_trainable_weights
))

print("\nPractice 1 Completed Successfully!")
