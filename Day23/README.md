# Day 23 - Object Detection Using YOLOv8

## 1. Introduction

Object Detection is a computer vision technique used to identify objects in an image and locate them using bounding boxes. It provides information about what objects are present and where they are located.

## 2. Image Classification vs Object Detection

- Image Classification identifies the main category of an entire image.
- Object Detection identifies multiple objects in an image and shows their locations using bounding boxes.

## 3. What is YOLO?

YOLO stands for You Only Look Once. It is a real-time object detection algorithm that detects objects in images and videos.

YOLO is popular because it is fast, efficient, and capable of detecting multiple objects in a single image.

## 4. YOLO Concepts

- Bounding Box: A rectangle drawn around a detected object.
- Class Label: The name of the detected object.
- Confidence Score: A value indicating how confident the model is about its prediction.
- Inference: Using a trained model to make predictions on new images.
- Training: Teaching a model using a dataset.

## 5. Dataset Used

For this mini project, I used a public Vehicle Detection dataset downloaded from Roboflow Universe.

Dataset Name: Vehicle Detection v2 - Dataset with Truck and Bus

Dataset Format: YOLOv8

Dataset Classes:
- Bus
- Car
- Motorbike
- Truck

Dataset Distribution:
- Training Images: 475
- Validation Images: 61
- Testing Images: 55
- Total Images: 591

## 6. Tools and Technologies

- Python 3.13
- Ultralytics YOLOv8
- OpenCV
- Roboflow Universe
- Visual Studio Code
- PowerShell

## 7. Implementation

A pre-trained YOLOv8 Nano model was loaded using the Ultralytics package.

