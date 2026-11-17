# Day 30 – AI Image Segmentation Studio

A complete Image Segmentation project developed using Python, OpenCV, NumPy, Matplotlib and Streamlit. This project explores different image segmentation techniques and provides an interactive web application for processing images.

## 1. Project Overview

Image segmentation is a computer vision technique that divides an image into meaningful regions or separates objects from their background.

The main objective of this project is to understand and implement image segmentation methods, process different types of images, compare their results and develop an interactive segmentation tool.

## 2. Topics Covered

- Introduction to Image Segmentation
- Segmentation vs Object Detection
- Semantic Segmentation
- Instance Segmentation
- Real-world Applications of Image Segmentation
- Image Thresholding Techniques
- Foreground and Background Segmentation
- Watershed Algorithm
- Image Processing with OpenCV

## 3. Implemented Algorithms

### Binary Thresholding
Uses a fixed threshold value to convert a grayscale image into a binary image containing black and white pixels.

### Adaptive Thresholding
Calculates different threshold values for local image regions. It is useful for images with uneven lighting.

### Otsu Thresholding
Automatically determines an optimal threshold value based on the image histogram.

### GrabCut Algorithm
Separates foreground objects from the background using OpenCV's GrabCut algorithm. The processed foreground is displayed on a white background.

### Watershed Algorithm
Uses morphological operations, distance transformation and markers to identify boundaries between image regions. Detected boundaries are highlighted in red.

## 4. Dataset

A dataset of 15 images was prepared and organized into four categories.

| Category | Images |
|---|---:|
| Documents | 4 |
| Objects | 4 |
| Shadows | 3 |
| Uneven Lighting | 4 |
| Total | 15 |

The dataset includes documents, everyday objects, shadows and images with uneven lighting conditions.

## 5. Coding Practice

The following tasks were implemented using OpenCV:

- Reading images from dataset folders.
- Converting images into grayscale.
- Applying Binary Thresholding.
- Applying Adaptive Thresholding.
- Applying Otsu Thresholding.
- Comparing all three thresholding methods.
- Saving grayscale and processed images.
- Separating foreground and background.
- Processing object images using Watershed.

### Processing Results

- 15 images processed using Binary Thresholding.
- 15 images processed using Adaptive Thresholding.
- 15 images processed using Otsu Thresholding.
- 15 images processed using GrabCut.
- 4 object images processed using Watershed.
- Comparison charts and processed outputs saved successfully.

## 6. Mini Project – Document & Object Segmentation Tool

A mini project was developed to demonstrate image segmentation techniques in an interactive application.

### Application Features

- Upload images in JPG, JPEG and PNG formats.
- Select different segmentation methods.
- Apply Binary Thresholding.
- Apply Adaptive Thresholding.
- Apply Otsu Thresholding.
- Remove background using GrabCut.
- Apply Watershed Segmentation.
- View original and processed images.
- Download processed images in PNG format.

### User Interface

The application was developed using Streamlit with a modern dark-themed dashboard, custom styling, sidebar navigation, image upload section, method selection and processing results.

## 7. Technologies and Libraries

- Python
- OpenCV
- NumPy
- Matplotlib
- Pillow
- Streamlit

## 8. Project Structure

```text
Day30/
│
├── app.py
├── requirements.txt
├── README.md
│
├── dataset/
│   ├── documents/
│   ├── objects/
│   ├── shadows/
│   └── uneven_lighting/
│
├── programs/
│   ├── segmentation.py
│   ├── foreground_background.py
│   └── watershed.py
│
├── mini_project/
│   └── segmentation_tool.py
│
├── outputs/
│   ├── adaptive/
│   ├── binary/
│   ├── comparison/
│   ├── foreground/
│   ├── otsu/
│   └── watershed/
│
└── screenshots/
```

## 9. Installation

Clone the repository:

```bash
git clone https://github.com/18-muskan/MLB-Internship.git
```

Navigate to the project folder:

```bash
cd MLB-Internship/Day30
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## 10. Run the Project

Run the thresholding and comparison program:

```bash
python programs/segmentation.py
```

Run foreground and background segmentation:

```bash
python programs/foreground_background.py
```

Run the Watershed algorithm:

```bash
python programs/watershed.py
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## 11. Methods Comparison

- Binary Thresholding is suitable for images with consistent lighting.
- Adaptive Thresholding performs better when lighting conditions vary across an image.
- Otsu Thresholding automatically selects a threshold based on image intensity distribution.
- GrabCut is useful for separating foreground objects from backgrounds.
- Watershed helps identify boundaries between image regions and objects.

The best method depends on the image, lighting conditions and segmentation requirements.

## 12. Challenges Faced

- Working with images having different lighting conditions.
- Handling shadows and complex backgrounds.
- Selecting suitable threshold values.
- Separating foreground objects from backgrounds.
- Understanding and implementing the Watershed algorithm.
- Organizing datasets and saving processed results.
- Developing an interactive Streamlit application.

## 13. Learning Outcomes

- Understood fundamental image segmentation concepts.
- Implemented multiple thresholding techniques using OpenCV.
- Learned foreground and background segmentation.
- Practiced the Watershed algorithm.
- Processed and analyzed a dataset of 15 images.
- Developed an interactive image segmentation application.
- Learned to build a user-friendly computer vision interface using Streamlit.

## 14. Deployment

The Streamlit application is prepared for deployment using Streamlit Community Cloud.

Live Demo: To be added after deployment.

## 15. Project Information

**Developer:** Muskan Ejaz

**Project:** AI Image Segmentation Studio

**Internship:** Machine Learning Internship – Day 30

**GitHub Repository:** https://github.com/18-muskan/MLB-Internship

## Live Demo

Try the Image Segmentation Studio online:

https://ai-image-segmentation-studio.streamlit.app/