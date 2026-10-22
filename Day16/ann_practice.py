
# Day 16 - Artificial Neural Network Practice

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

print("ARTIFICIAL NEURAL NETWORK")
print("-------------------------")

# Create a simple neural network
model = keras.Sequential([
    # Input layer: accepts 4 input features
    keras.Input(shape=(4,), name="Input_Layer"),

    # Hidden layer: contains 8 neurons
    layers.Dense(8, activation="relu", name="Hidden_Layer"),

    # Output layer: produces 3 class scores as probabilities
    layers.Dense(3, activation="softmax", name="Output_Layer")
])

# Display the model architecture and parameters
model.summary()
