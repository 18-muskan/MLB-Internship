
import cv2
import os

# Load input image
image_path = "Input_Images/sample.jpg"
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")
else:
    # Apply Bilateral Filtering
    filtered_image = cv2.bilateralFilter(image, 9, 75, 75)

    # Create output directory
    output_dir = "Image_Enhancement/blur_outputs"
    os.makedirs(output_dir, exist_ok=True)

    # Save filtered image
    output_path = os.path.join(output_dir, "bilateral_filter.jpg")
    cv2.imwrite(output_path, filtered_image)

    print("Bilateral Filtering applied successfully!")
