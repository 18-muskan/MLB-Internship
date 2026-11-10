
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
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Convert image into binary format
    _, binary = cv2.threshold(
        gray, 127, 255, cv2.THRESH_BINARY
    )

    # Create kernel
    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT, (3, 3)
    )

    # Apply morphological operations
    erosion = cv2.erode(binary, kernel, iterations=1)

    dilation = cv2.dilate(binary, kernel, iterations=1)

    opening = cv2.morphologyEx(
        binary, cv2.MORPH_OPEN, kernel
    )

    closing = cv2.morphologyEx(
        binary, cv2.MORPH_CLOSE, kernel
    )

    gradient = cv2.morphologyEx(
        binary, cv2.MORPH_GRADIENT, kernel
    )

    # Top Hat and Black Hat on grayscale image
    large_kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT, (9, 9)
    )

    top_hat = cv2.morphologyEx(
        gray, cv2.MORPH_TOPHAT, large_kernel
    )

    black_hat = cv2.morphologyEx(
        gray, cv2.MORPH_BLACKHAT, large_kernel
    )

    # Prepare images for comparison
    images = [
        ("Original", gray),
        ("Erosion", erosion),
        ("Dilation", dilation),
        ("Opening", opening),
        ("Closing", closing),
        ("Gradient", gradient),
        ("Top Hat", top_hat),
        ("Black Hat", black_hat)
    ]

    # Resize and add titles
    comparison_images = []

    for title, img in images:

        resized = cv2.resize(img, (400, 300))

        colored = cv2.cvtColor(
            resized, cv2.COLOR_GRAY2BGR
        )

        cv2.putText(
            colored,
            title,
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2
        )

        comparison_images.append(colored)

    # Create comparison grid
    row1 = np.hstack(comparison_images[:4])
    row2 = np.hstack(comparison_images[4:])

    comparison = np.vstack((row1, row2))

    # Save comparison image
    output_path = os.path.join(
        output_dir, "morphology_comparison.jpg"
    )

    cv2.imwrite(output_path, comparison)

    print("Morphological comparison completed successfully!")
    print("All seven operations compared successfully!")
    print("Output saved at:", output_path)

    # Display comparison
    cv2.imshow("Morphological Operations Comparison", comparison)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
