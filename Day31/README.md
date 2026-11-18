
# Custom YOLO Construction Equipment Detection System

## Project Overview

This project uses a custom-trained YOLOv8 model to detect construction equipment in images and videos. A Streamlit web application allows users to upload files and view detection results.

## Dataset

Dataset: SODA1 Construction Equipment  
Source: https://universe.roboflow.com/soda1/equipment-wmk6r

License: CC BY 4.0

Total Images: 9,986

- Training: 7,790 images
- Validation: 1,702 images
- Testing: 494 images

## Detection Classes

The model detects 10 construction equipment classes:

1. Backhoe Loader
2. Compactor
3. Concrete Mixer Truck
4. Dozer
5. Dump Truck
6. Excavator
7. Grader
8. Mobile Crane
9. Tower Crane
10. Wheel Loader

## Model Training

- Model: YOLOv8 Nano
- Image Size: 640
- Epochs: 10
- Batch Size: 8
- Hardware: NVIDIA Tesla T4 GPU

## Test Evaluation Results

| Metric | Score |
|---|---:|
| Precision | 87.07% |
| Recall | 84.41% |
| mAP@50 | 88.12% |
| mAP@50-95 | 72.68% |

Test images: 494

## Project Features

- Custom YOLO object detection
- Image upload and detection
- Video upload and frame-by-frame detection
- Bounding boxes and class labels
- Confidence scores
- Downloadable detection results
- Streamlit web interface

## Project Structure

```text
Day31/
├── app.py
├── requirements.txt
├── README.md
├── weights/
│   └── best.pt
├── sample_images/
├── predictions/
├── results/
├── programs/
└── dataset/
