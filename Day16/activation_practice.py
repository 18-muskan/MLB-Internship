
# Day 16 - Activation Functions Practice

import tensorflow as tf
from tensorflow.keras import layers, Sequential

# Test three different activation functions
activations = ["relu", "sigmoid", "tanh"]

for activation in activations:
    print("\nActivation Function:", activation)
    print("-" * 35)

    # Create a neural network
    model = Sequential([
        tf.keras.Input(shape=(4,)),
        layers.Dense(8, activation=activation),
        layers.Dense(3, activation="softmax")
    ])

    # Display the model structure
    model.summary()

    # Test the activation function with sample values
    sample_values = tf.constant([-2.0, 0.0, 2.0])
    output = layers.Activation(activation)(sample_values)

    print("Input values:", sample_values.numpy())
    print("Output values:", output.numpy())
