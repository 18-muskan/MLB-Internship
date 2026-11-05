
import cv2
import os

# Load input image
image_path = "Input_Images/sample.jpg"
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")
else:
    # Apply Median Blur
    blurred_image = cv2.medianBlur(image, 5)

    # Create output directory
    output_dir = "Image_Enhancement/blur_outputs"
    os.makedirs(output_dir, exist_ok=True)

    # Save output image
    output_path = os.path.join(output_dir, "median_blur.jpg")
    cv2.imwrite(output_path, blurred_image)

    print("Median Blur applied successfully!")
