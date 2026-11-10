
import cv2
import os

# Get project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Input image path
image_path = os.path.join(BASE_DIR, "dataset", "input_images", "document1.jpg")

# Output directory
output_dir = os.path.join(BASE_DIR, "output", "edge_detection")
os.makedirs(output_dir, exist_ok=True)

# Load image
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")

else:
    # Apply Gaussian Blur
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

    # Save output
    output_path = os.path.join(output_dir, "gaussian_blur.jpg")
    cv2.imwrite(output_path, blurred_image)

    print("Gaussian Blur applied successfully!")
    print("Output saved at:", output_path)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Gaussian Blur", blurred_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
