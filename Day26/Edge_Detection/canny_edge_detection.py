
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
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Canny Edge Detection
    canny = cv2.Canny(blurred, 50, 150)

    # Save output
    output_path = os.path.join(output_dir, "canny_edges.jpg")
    cv2.imwrite(output_path, canny)

    print("Canny Edge Detection completed successfully!")
    print("Output saved at:", output_path)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Canny Edge Detection", canny)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
