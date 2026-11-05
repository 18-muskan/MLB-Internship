
import cv2
import numpy as np
import os

# Load input image
image_path = "Input_Images/sample.jpg"
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")
else:
    # Set gamma value
    gamma = 1.5

    # Create lookup table
    lookup_table = np.array([
        ((i / 255.0) ** (1.0 / gamma)) * 255
        for i in range(256)
    ]).astype("uint8")

    # Apply Gamma Correction
    corrected_image = cv2.LUT(image, lookup_table)

    # Create output directory
    output_dir = "Image_Enhancement/gamma_outputs"
    os.makedirs(output_dir, exist_ok=True)

    # Save corrected image
    output_path = os.path.join(output_dir, "gamma_corrected.jpg")
    cv2.imwrite(output_path, corrected_image)

    print("Gamma Correction completed successfully!")
