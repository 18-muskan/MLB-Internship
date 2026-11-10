
import cv2
import os
import numpy as np

# Get project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Input image
image_path = os.path.join(BASE_DIR, "dataset", "input_images", "document1.jpg")

# Output directory
output_dir = os.path.join(BASE_DIR, "output", "comparison")
os.makedirs(output_dir, exist_ok=True)

# Load image
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")

else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Sobel Edge Detection
    sobel_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)

    sobel = cv2.addWeighted(
        cv2.convertScaleAbs(sobel_x), 0.5,
        cv2.convertScaleAbs(sobel_y), 0.5, 0
    )

    # Laplacian Edge Detection
    laplacian = cv2.Laplacian(blurred, cv2.CV_64F, ksize=3)
    laplacian = cv2.convertScaleAbs(laplacian)

    # Canny Edge Detection
    canny = cv2.Canny(blurred, 50, 150)

    # Resize images to same dimensions
    height, width = 300, 400

    original = cv2.resize(gray, (width, height))
    sobel = cv2.resize(sobel, (width, height))
    laplacian = cv2.resize(laplacian, (width, height))
    canny = cv2.resize(canny, (width, height))

    # Add labels
    def add_title(img, title):
        result = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        cv2.putText(result, title, (10, 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (0, 0, 255), 2)
        return result

    # Create comparison
    top_row = np.hstack((
        add_title(original, "Original"),
        add_title(sobel, "Sobel")
    ))

    bottom_row = np.hstack((
        add_title(laplacian, "Laplacian"),
        add_title(canny, "Canny")
    ))

    comparison = np.vstack((top_row, bottom_row))

    # Save comparison image
    output_path = os.path.join(output_dir, "edge_comparison.jpg")
    cv2.imwrite(output_path, comparison)

    print("Edge detection comparison completed successfully!")
    print("Comparison image saved at:", output_path)

    # Display comparison
    cv2.imshow("Edge Detection Comparison", comparison)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
