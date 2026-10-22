# Day 16: Deep Learning Basics

## 1. What is Deep Learning?
Deep Learning is a branch of Machine Learning that uses neural networks with multiple layers to learn patterns from data. It is commonly used in image recognition, speech recognition, and natural language processing.

## 2. Difference Between Machine Learning and Deep Learning

- **Machine Learning:** Often requires manual feature selection and can work well with smaller datasets and simpler models.
- **Deep Learning:** Uses neural networks with multiple layers to learn features automatically. It often needs more data and computing power.

## 3. What is a Perceptron?
A perceptron is one of the simplest artificial neural network units. It receives input values, assigns weights, adds a bias, and applies an activation function to produce an output. It is a basic building block of neural networks.

## 4. Activation Functions Explored

- **ReLU (Rectified Linear Unit):** Converts negative values to zero and keeps positive values. Commonly used in hidden layers of neural networks.
- **Sigmoid:** Converts values into a range between 0 and 1. Commonly used in the output layer for binary classification.
- **Tanh:** Converts values into a range between -1 and 1. Commonly used in some neural network hidden layers and recurrent neural networks.
- **Softmax:** Converts output scores into class probabilities. Used in the output layer for multi-class classification, including this Fashion MNIST project.

## 5. Fashion MNIST ANN Model

The model classifies clothing images into 10 categories using the Fashion MNIST dataset.

**Model Architecture:**
- Input: 28 × 28 grayscale images
- Flatten layer: Converts each image into 784 values
- Hidden layer: 128 neurons with ReLU activation
- Output layer: 10 neurons with Softmax activation
- Optimizer: Adam
- Loss function: Sparse Categorical Crossentropy
- Training epochs: 5

## 6. Final Model Accuracy

- **Training Accuracy:** 89.12%
- **Validation Accuracy:** 87.55%
- **Testing Accuracy:** 86.50%

The model achieved 86.50% testing accuracy on unseen test images.

## 7. Output Files

- `sample_images.png`: Displays sample clothing images.
- `accuracy_graph.png`: Shows training and validation accuracy.
- `sample_predictions.png`: Compares predicted labels with actual labels.
- `fashion_mnist_model.keras`: Saved trained ANN model.

## 8. Conclusion

Completed Deep Learning practice using TensorFlow and Keras. Built and trained an ANN model for Fashion MNIST classification, explored activation functions, evaluated model accuracy, visualized predictions, and saved the trained model.
