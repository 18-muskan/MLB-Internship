
---
title: Computer Vision Image Processing Studio
emoji: 📸
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 6.32.0
app_file: app.py
pinned: false
---

# Computer Vision Image Processing Studio

## Overview

Computer Vision Image Processing Studio is an interactive web application built using Python, OpenCV, NumPy and Gradio.

It allows users to upload images, apply different image processing techniques, preview the results and download processed images.

## Features

- Upload images.
- Grayscale conversion.
- Gaussian blur.
- Edge detection using Canny.
- Image rotation.
- Image enhancement using CLAHE.
- Contour detection.
- Shape detection.
- Brightness and contrast adjustment.
- Image sharpening.
- Image flipping.
- Thresholding.
- Multiple filters in sequence.
- Original and processed image preview.
- Download processed images.

## Technologies Used

- Python 3.13
- OpenCV
- NumPy
- Gradio
- Pillow

## Project Structure

```text
Day28/
│
├── app.py
├── requirements.txt
├── README.md
│
├── programs/
│   └── image_processor.py
│
├── sample_images/
├── sample_outputs/
└── screenshots/
```

## How to Run Locally

1. Clone the repository.
2. Open the project folder.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

5. Open the local Gradio URL in your browser.

## How to Use

1. Upload an image.
2. Select an image processing operation.
3. Adjust advanced settings if required.
4. Click Process Image.
5. View the processed result.
6. Download the output image.

## Custom Features

The project also includes additional image processing features such as brightness and contrast adjustment, image sharpening, image flipping and multiple filters in sequence.

## Deployment

The application is designed for deployment on Hugging Face Spaces using Gradio.

## Internship Project

MLB Internship - Day 28

Computer Vision Image Processing Studio
