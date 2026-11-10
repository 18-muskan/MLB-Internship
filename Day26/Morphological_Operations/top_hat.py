
import cv2
import os

# Get project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Input image
image_path = os.path.join(BASE_DIR, "dataset", "input_images", "document1.jpg")

# Output directory
output_dir = os.path.join(BASE_DIR, "output", "morphological_operations")
os.makedirs(output_dir, exist_ok=True)

# Load image
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")

else:
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))

    # Apply Top Hat
    top_hat = cv2.morphologyEx(
        gray, cv2.MORPH_TOPHAT, kernel
    )

    # Save output
    output_path = os.path.join(output_dir, "top_hat.jpg")
    cv2.imwrite(output_path, top_hat)

    print("Top Hat operation applied successfully!")
    print("Output saved at:", output_path)

    # Display images
    cv2.imshow("Original Grayscale Image", gray)
    cv2.imshow("Top Hat Operation", top_hat)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
