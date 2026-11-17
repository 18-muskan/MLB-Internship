
import cv2
import os
import numpy as np

# Main project folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASET_DIR = os.path.join(BASE_DIR, "dataset", "objects")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs", "watershed")

os.makedirs(OUTPUT_DIR, exist_ok=True)


def apply_watershed(image_path):

    image = cv2.imread(image_path)

    if image is None:
        print("Image could not be loaded:", image_path)
        return

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Otsu thresholding
    _, binary = cv2.threshold(
        gray, 0, 255,
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )

    # Remove noise using morphological opening
    kernel = np.ones((3, 3), np.uint8)

    opening = cv2.morphologyEx(
        binary,
        cv2.MORPH_OPEN,
        kernel,
        iterations=2
    )

    # Find sure background area
    sure_background = cv2.dilate(
        opening,
        kernel,
        iterations=3
    )

    # Find sure foreground area using distance transform
    distance = cv2.distanceTransform(
        opening,
        cv2.DIST_L2,
        5
    )

    _, sure_foreground = cv2.threshold(
        distance,
        0.4 * distance.max(),
        255,
        0
    )

    sure_foreground = np.uint8(sure_foreground)

    # Find unknown region
    unknown = cv2.subtract(
        sure_background,
        sure_foreground
    )

    # Label foreground regions
    _, markers = cv2.connectedComponents(sure_foreground)

    # Add one to all labels
    markers = markers + 1

    # Mark unknown region as zero
    markers[unknown == 255] = 0

    # Apply Watershed Algorithm
    markers = cv2.watershed(image, markers)

    # Highlight boundaries in red
    result = image.copy()
    result[markers == -1] = [0, 0, 255]

    filename = os.path.splitext(os.path.basename(image_path))[0]

    output_path = os.path.join(
        OUTPUT_DIR,
        filename + "_watershed.jpg"
    )

    cv2.imwrite(output_path, result)

    print("Watershed applied:", filename)


def main():

    print("WATERSHED SEGMENTATION")
    print("----------------------")

    total_images = 0

    for filename in os.listdir(DATASET_DIR):

        if filename.lower().endswith((".jpg", ".jpeg", ".png")):

            image_path = os.path.join(DATASET_DIR, filename)

            apply_watershed(image_path)
            total_images += 1

    print("\nProcessing completed!")
    print("Total images processed:", total_images)
    print("Results saved in outputs/watershed")


if __name__ == "__main__":
    main()
