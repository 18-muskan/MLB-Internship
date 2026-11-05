
import cv2
import os

# Load input image in grayscale
image_path = "Input_Images/sample.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Image not found!")
else:
    # Apply Histogram Equalization
    equalized_image = cv2.equalizeHist(image)

    # Create output directory
    output_dir = "Image_Enhancement/histogram_outputs"
    os.makedirs(output_dir, exist_ok=True)

    # Save equalized image
    output_path = os.path.join(output_dir, "histogram_equalized.jpg")
    cv2.imwrite(output_path, equalized_image)

    print("Histogram Equalization completed successfully!")
