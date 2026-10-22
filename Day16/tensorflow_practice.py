
# Day 16 - TensorFlow Installation and Verification

import tensorflow as tf
from tensorflow import keras

print("TensorFlow Installation Successful!")
print("TensorFlow Version:", tf.__version__)
print("Keras Imported Successfully!")

# Check whether TensorFlow is working
print("TensorFlow Test:", tf.reduce_sum([1, 2, 3]).numpy())
