
import cv2
import os
import matplotlib.pyplot as plt

# Get the main Day30 project folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Dataset and output folders
DATASET_DIR = os.path.join(BASE_DIR, "dataset")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

# Create output folders if they do not exist
methods = ["binary", "adaptive", "otsu", "comparison"]

for method in methods:
    os.makedirs(os.path.join(OUTPUT_DIR, method), exist_ok=True)

def process_image(image_path, category):
    # Read original image
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Image could not be loaded:", image_path)
        return

    # Convert image into grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 1. Binary Thresholding
    _, binary = cv2.threshold(
        gray, 127, 255, cv2.THRESH_BINARY
    )

    # 2. Adaptive Thresholding
    adaptive = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    # 3. Otsu Thresholding
    otsu_value, otsu = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    # Get image filename
    filename = os.path.splitext(os.path.basename(image_path))[0]

    # Save grayscale image
    cv2.imwrite(
        os.path.join(OUTPUT_DIR, "comparison", filename + "_gray.jpg"),
        gray
    )

    # Save Binary output
    cv2.imwrite(
        os.path.join(OUTPUT_DIR, "binary", filename + "_binary.jpg"),
        binary
    )

    # Save Adaptive output
    cv2.imwrite(
        os.path.join(OUTPUT_DIR, "adaptive", filename + "_adaptive.jpg"),
        adaptive
    )

    # Save Otsu output
    cv2.imwrite(
        os.path.join(OUTPUT_DIR, "otsu", filename + "_otsu.jpg"),
        otsu
    )

    # Compare all methods in one figure
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(binary, cmap="gray")
    plt.title("Binary Thresholding")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(adaptive, cmap="gray")
    plt.title("Adaptive Thresholding")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(otsu, cmap="gray")
    plt.title("Otsu Thresholding")
    plt.axis("off")

    plt.tight_layout()

    comparison_path = os.path.join(
        OUTPUT_DIR, "comparison", filename + "_comparison.png"
    )

    plt.savefig(comparison_path)
    plt.close()

    print("Processed:", filename)
    print("Otsu threshold value:", otsu_value)

def main():
    print("IMAGE SEGMENTATION PROJECT")
    print("--------------------------")

    total_images = 0

    # Process images from all dataset categories
    for category in os.listdir(DATASET_DIR):

        category_path = os.path.join(DATASET_DIR, category)

        if not os.path.isdir(category_path):
            continue

        for filename in os.listdir(category_path):

            if filename.lower().endswith((".jpg", ".jpeg", ".png")):

                image_path = os.path.join(category_path, filename)

                process_image(image_path, category)
                total_images += 1

    print("\nProcessing completed!")
    print("Total images processed:", total_images)
    print("Results saved inside outputs folder.")

if __name__ == "__main__":
    main()