# Day 26 - Edge Detection and Morphological Operations

## Objective
The objective of this task was to learn edge detection techniques, morphological operations, and document boundary detection using OpenCV and Python.

## 1. Edge Detection
Implemented the following techniques:

- Grayscale: Converts a color image into grayscale.
- Gaussian Blur: Reduces noise and smooths the image.
- Sobel Operator: Detects horizontal and vertical edges.
- Laplacian Operator: Detects edges in all directions.
- Canny Edge Detection: Detects clear and strong edges.

## 2. Morphological Operations
Implemented:

- Erosion: Removes small white areas and reduces object size.
- Dilation: Expands white areas.
- Opening: Removes small noise.
- Closing: Fills small holes and gaps.
- Morphological Gradient: Highlights object boundaries.
- Top Hat: Highlights small bright details.
- Black Hat: Highlights small dark details.

## 3. Comparison
Compared different edge detection and morphological techniques using output images.

Canny provides clear edges, while Sobel detects directional edges and Laplacian detects edges in multiple directions.

Opening is useful for removing noise, while closing helps connect broken edges.

## 4. Mini Project: Document Boundary Detection
Developed a document boundary detection tool using OpenCV.

Processing steps:
1. Load document images.
2. Convert images into grayscale.
3. Apply Gaussian Blur.
4. Detect edges using Canny.
5. Apply morphological closing.
6. Find contours.
7. Select the largest contour.
8. Draw the detected document boundary.
9. Save the processed images.

## 5. Dataset and Results
Used 10 document images for testing.

For every image, four outputs were saved:
- Original image
- Edge detection image
- Morphological result
- Final boundary image

All 10 images were processed successfully.

## 6. Challenges
- Handling noise and uneven lighting.
- Detecting document boundaries in tilted images.
- Connecting broken edges.
- Selecting the largest contour correctly.

## 7. Best Combination
Grayscale + Gaussian Blur + Canny Edge Detection + Morphological Closing + Contour Detection.

This combination worked well for detecting document boundaries.

## Conclusion
Successfully implemented edge detection, morphological operations, comparison programs, and a document boundary detection tool using Python and OpenCV.