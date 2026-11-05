
# Document Image Enhancement Tool

## Project Overview

The Document Image Enhancement Tool is a Python-based application developed using OpenCV and NumPy. It improves the readability and quality of document images by applying perspective correction, noise reduction, contrast enhancement, brightness adjustment, and sharpening techniques.

## Project Objectives

- Correct tilted document images.
- Convert document images into grayscale.
- Reduce unwanted image noise.
- Improve image brightness and contrast.
- Sharpen text and document details.
- Generate before-and-after comparisons.
- Save enhanced document images.

## Technologies Used

- Python
- OpenCV
- NumPy

## Dataset

The project uses 10 document images stored in the Dataset folder.

- 5 tilted document images.
- 5 straight document images.

## Image Transformation Techniques

1. Translation
2. Rotation
3. Scaling
4. Affine Transformation
5. Perspective Transformation

## Image Enhancement Techniques

1. Brightness Adjustment
2. Contrast Adjustment
3. Gaussian Blur
4. Median Blur
5. Bilateral Filter
6. Image Sharpening
7. Histogram Equalization
8. CLAHE
9. Gamma Correction

## Document Enhancement Pipeline

1. Load document images.
2. Correct perspective distortion.
3. Convert images into grayscale.
4. Apply bilateral filtering for noise reduction.
5. Improve contrast using CLAHE.
6. Adjust brightness.
7. Apply image sharpening.
8. Save final enhanced images.
9. Generate before-and-after comparisons.

## Mandatory Challenge

Five tilted document images were manually corrected using perspective transformation.

The four document corners were selected for each image, and OpenCV perspective transformation was applied to obtain corrected document images.

The corrected images were then processed through the enhancement pipeline.

## Project Results

- 10 document images processed successfully.
- 10 perspective-corrected image files generated.
- 10 final enhanced images generated.
- 10 before-and-after comparison images generated.
- Manual perspective correction completed for 5 tilted images.

## Project Structure

Day25/
│
├── Dataset/
│   ├── img1.jpg
│   ├── img2.jpg
│   └── ... img10.jpg
│
├── Image_Transformations/
│
├── Image_Enhancement/
│
├── Document_Enhancement_Tool/
│   ├── batch_manual_perspective.py
│   ├── final_enhancement.py
│   └── create_challenge_comparisons.py
│
├── Enhanced_Outputs/
│   ├── Perspective_Corrected/
│   └── Final_Enhanced/
│
├── Comparisons/
│
├── Challenge_Results/
│
├── README.md
└── requirements.txt


## How to Run

Install the required libraries:

pip install -r requirements.txt

Run the final enhancement script:

python Document_Enhancement_Tool/final_enhancement.py

For manual perspective correction of tilted images:
python Document_Enhancement_Tool/batch_manual_perspective.py


## Conclusion

This project demonstrates practical image processing techniques using Python and OpenCV. It provides a workflow for correcting tilted documents, reducing noise, improving readability, and generating enhanced document images with visual comparisons.
