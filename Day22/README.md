# Day 22 – Transfer Learning and Cats vs Dogs Classification

## 1. Introduction

This project focuses on Transfer Learning using pre-trained Convolutional Neural Network (CNN) models. A Cats vs Dogs image classification model was developed using MobileNetV2.

## 2. Transfer Learning Models

Four popular pre-trained models were studied:

| Model | Description |
|---|---|
| VGG16 | Uses a simple architecture with 16 weight layers. It is computationally heavy. |
| ResNet50 | Uses residual connections to improve deep network training. |
| MobileNetV2 | A lightweight model designed for faster and efficient image classification. |
| EfficientNetB0 | Uses compound scaling to balance model size and accuracy. |

### Model Selection

MobileNetV2 was selected because it is lightweight and suitable for systems with limited computing resources.

## 3. Dataset

Dataset: Cats vs Dogs

Source: TensorFlow Datasets (TFDS)

Dataset preprocessing:
- Images resized to 160 × 160 pixels.
- MobileNetV2 preprocessing applied.
- Dataset divided into:
  - 80% Training
  - 10% Validation
  - 10% Testing

Some corrupted images were automatically skipped by the dataset loader.

## 4. Model Architecture

The project uses pre-trained MobileNetV2 with ImageNet weights.

The base model was frozen to preserve its pre-trained features.

Custom classification layers:
1. Global Average Pooling
2. Dropout (0.2)
3. Dense layer (128 neurons, ReLU)
4. Output layer (1 neuron, Sigmoid)

## 5. Training Configuration

- Optimizer: Adam
- Learning Rate: 0.001
- Loss Function: Binary Crossentropy
- Batch Size: 32
- Maximum Epochs: 5
- Early Stopping: Enabled

Training stopped after 4 epochs because of early stopping.

## 6. Results

| Metric | Result |
|---|---:|
| Training Accuracy (Epoch 4) | 99.05% |
| Validation Accuracy (Epoch 2) | 98.58% |
| Test Accuracy | 98.07% |
| Test Loss | 0.0468 |

The model achieved 98.07% test accuracy.

## 7. Graphs

The following graphs were generated