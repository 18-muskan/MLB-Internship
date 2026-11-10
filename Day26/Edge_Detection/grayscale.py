
import cv2
import os

# Get project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Input image path
image_path = os.path.join(BASE_DIR, "dataset", "input_images", "document1.jpg")

# Output directory
output_dir = os.path.join(BASE_DIR, "output", "edge_detection")
os.makedirs(output_dir, exist_ok=True)

# Load original image
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")
else:
    # Convert image into grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Save grayscale image
    output_path = os.path.join(output_dir, "grayscale.jpg")
    cv2.imwrite(output_path, gray_image)

    print("Grayscale conversion completed successfully!")
    print("Output saved at:", output_path)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
