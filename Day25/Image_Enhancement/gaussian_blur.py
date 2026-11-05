
import cv2
import os

# Load input image
image_path = "Input_Images/sample.jpg"
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")
else:
    # Apply Gaussian Blur
    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

    # Create output directory
    output_dir = "Image_Enhancement/blur_outputs"
    os.makedirs(output_dir, exist_ok=True)

    # Save blurred image
    output_path = os.path.join(output_dir, "gaussian_blur.jpg")
    cv2.imwrite(output_path, blurred_image)

    print("Gaussian Blur applied successfully!")
