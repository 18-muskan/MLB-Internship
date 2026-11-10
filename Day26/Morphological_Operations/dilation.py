
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

    # Convert image into binary format
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Create kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    # Apply dilation
    dilation = cv2.dilate(binary, kernel, iterations=1)

    # Save output
    output_path = os.path.join(output_dir, "dilation.jpg")
    cv2.imwrite(output_path, dilation)

    print("Dilation applied successfully!")
    print("Output saved at:", output_path)

    # Display images
    cv2.imshow("Original Binary Image", binary)
    cv2.imshow("Dilation", dilation)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
