# Computer Vision Image Processing Studio

## Overview

Computer Vision Image Processing Studio is an interactive web application built using Python, OpenCV, NumPy and Streamlit.

It allows users to upload images, apply different computer vision techniques, preview processed results and download the output images.

## Live Application

Streamlit App: https://computer-vision-image-studio.streamlit.app/

GitHub Repository: https://github.com/18-muskan/MLB-Internship/tree/main/Day28

## Features

- Upload JPG, JPEG and PNG images.
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
- Streamlit
- Pillow

## Project Structure

```text
Day28/
│
├── app.py
├── streamlit_app.py
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
2. Open the Day28 folder.
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit application:

```bash
streamlit run streamlit_app.py
```

5. Open the local URL displayed in the terminal.

## How to Use

1. Open the application.
2. Upload a JPG, JPEG or PNG image.
3. Select an image processing operation.
4. Adjust brightness, contrast or rotation settings if needed.
5. Preview the original and processed images.
6. Download the processed image.

## Deployment

The application is deployed using Streamlit Community Cloud and connected to the GitHub repository.

The public application can be accessed through the live link provided above.

## Internship Project

MLB Internship - Day 28

Project: Computer Vision Image Processing Studio