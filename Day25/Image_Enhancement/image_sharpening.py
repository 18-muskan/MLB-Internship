
import cv2
import numpy as np
import os

# Load input image
image_path = "Input_Images/sample.jpg"
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")
else:
    # Create sharpening kernel
    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])

    # Apply sharpening
    sharpened_image = cv2.filter2D(image, -1, kernel)

    # Create output directory
    output_dir = "Image_Enhancement/sharpen_outputs"
    os.makedirs(output_dir, exist_ok=True)

    # Save sharpened image
    output_path = os.path.join(output_dir, "sharpened_image.jpg")
    cv2.imwrite(output_path, sharpened_image)

    print("Image sharpening completed successfully!")
