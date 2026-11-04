# Day24 – OpenCV Fundamentals and Basic Image Processing

## Project Overview

This project focuses on learning OpenCV fundamentals and performing basic image processing operations using Python.

The project processes five different images: landscape, person, vehicle, document, and object. It includes individual Python programs for image processing and a menu-driven Image Toolkit mini project.

## Technologies Used

- Python 3.13
- OpenCV
- NumPy
- VS Code

## Project Structure

```text
Day24/
│
├── input_images/
│   ├── landscape.jpg
│   ├── person.jpg
│   ├── vehicle.jpg
│   ├── document.jpg
│   └── object.jpg
│
├── output/
│   ├── landscape/
│   ├── person/
│   ├── vehicle/
│   ├── document/
│   ├── object/
│   └── toolkit/
│
├── programs/
│   ├── image_information.py
│   ├── grayscale.py
│   ├── resize.py
│   ├── crop.py
│   ├── rotate.py
│   ├── flip.py
│   └── drawing.py
│
├── image_toolkit.py
└── README.md
```

## Implemented Image Processing Operations

### 1. Image Information
- Read image files using OpenCV.
- Display image height and width.
- Identify the number of color channels.
- Calculate image file size in bytes and KB.

### 2. Grayscale Conversion
- Convert color images into grayscale.
- Use `cv2.cvtColor()` and `cv2.COLOR_BGR2GRAY`.
- Save grayscale images in the output folders.

### 3. Image Resizing
- Resize images into small, medium, and large dimensions.
- Use `cv2.resize()`.

### 4. Image Cropping
- Crop top-left, center, and bottom-right regions.
- Use NumPy array slicing.

### 5. Image Rotation
- Rotate images by 90, 180, and 270 degrees.
- Use `cv2.rotate()`.

### 6. Image Flipping
- Perform horizontal flipping.
- Perform vertical flipping.
- Perform horizontal and vertical flipping together.
- Use `cv2.flip()`.

### 7. Drawing Shapes and Text
- Draw rectangles using `cv2.rectangle()`.
- Draw circles using `cv2.circle()`.
- Draw lines using `cv2.line()`.
- Draw polygons using `cv2.polylines()`.
- Add text using `cv2.putText()`.

### 8. Bonus Image Processing Operations

- Increase image brightness using `cv2.convertScaleAbs()`.
- Decrease image brightness.
- Enhance image contrast.
- Convert BGR images to RGB using `cv2.cvtColor()`.
- Display original and processed images for comparison.

Bonus outputs are stored in `output/bonus/`.

## Mini Project – Image Toolkit

A menu-driven application was developed to perform image processing operations through a single Python program.

Features include:

1. Load Image
2. Convert to Grayscale
3. Resize Image
4. Rotate Image
5. Flip Image
6. Crop Image
7. Draw Shapes
8. Add Text
9. Save Image
10. Display Image
11. Exit

Processed images are saved in the `output/toolkit/` directory.

## BGR vs RGB

OpenCV reads images in BGR format by default, which means Blue, Green, and Red.

Other image libraries commonly use RGB format, which means Red, Green, and Blue.

The channel order is important when displaying or processing images using different libraries.

## Why Grayscale Conversion?

Grayscale conversion changes a color image into shades of gray.

It reduces image information from three color channels to one intensity channel and is useful for image processing tasks such as edge detection and thresholding.

## How to Run the Project

### Step 1: Install Required Libraries

```bash
pip install opencv-python numpy
```

### Step 2: Open the Project Directory

```powershell
cd "C:\Users\owner\Documents\MLB-Internship\MLB-Internship\Day24"
```

### Step 3: Run Individual Programs

```bash
python programs/image_information.py
python programs/grayscale.py
python programs/resize.py
python programs/crop.py
python programs/rotate.py
python programs/flip.py
python programs/drawing.py
```

### Step 4: Run the Mini Project

```bash
python image_toolkit.py
```

Follow the menu instructions to select and perform image processing operations.

## Challenges and Solutions

- Image path errors were resolved by running programs from the correct project directory.
- Image dimensions were checked using the `shape` attribute.
- Different rotation and flipping operations were implemented using OpenCV functions.
- Output directories were created automatically using `os.makedirs()`.
- The Image Toolkit save path was improved using the absolute project directory