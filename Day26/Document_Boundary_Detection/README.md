# Document Boundary Detection Tool

## Objective
The objective of this mini project is to detect document boundaries from images using OpenCV and image processing techniques.

## Processing Steps
1. Load document images from the dataset.
2. Convert images into grayscale.
3. Apply Gaussian Blur to reduce noise.
4. Use Canny Edge Detection to detect edges.
5. Apply Morphological Closing to connect broken edges.
6. Find contours in the processed image.
7. Select the largest contour.
8. Draw the detected boundary on the original image.
9. Save all output images.

## Dataset
A dataset of 10 document images was used for testing.

## Output
For each input image, the tool saves:
- Original image
- Edge detection result
- Morphological result
- Final boundary detection result

Total images processed successfully: 10.

## Technologies Used
- Python
- OpenCV
- NumPy
- Image Processing

## Conclusion
The tool successfully processed 10 document images and detected their boundaries using Canny Edge Detection, Morphological Closing, and Contour Detection.