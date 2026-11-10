
import cv2
import os

# Get project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Input image
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

    # Apply Sobel X
    sobel_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)

    # Apply Sobel Y
    sobel_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)

    # Convert results to 8-bit images
    sobel_x = cv2.convertScaleAbs(sobel_x)
    sobel_y = cv2.convertScaleAbs(sobel_y)

    # Combine both directions
    sobel_combined = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

    # Save outputs
    cv2.imwrite(os.path.join(output_dir, "sobel_x.jpg"), sobel_x)
    cv2.imwrite(os.path.join(output_dir, "sobel_y.jpg"), sobel_y)
    cv2.imwrite(os.path.join(output_dir, "sobel_combined.jpg"), sobel_combined)

    print("Sobel Edge Detection completed successfully!")
    print("Sobel X, Sobel Y and Combined images saved.")

    # Display results
    cv2.imshow("Original Image", image)
    cv2.imshow("Sobel X", sobel_x)
    cv2.imshow("Sobel Y", sobel_y)
    cv2.imshow("Sobel Combined", sobel_combined)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
