
import cv2
import os
from pathlib import Path

# Get project folders
BASE_DIR = Path(__file__).resolve().parents[1]

INPUT_FOLDER = BASE_DIR / "dataset" / "sample_images"
OUTPUT_FOLDER = BASE_DIR / "dataset" / "processed_images"

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

# Find all images
image_files = [
    file for file in INPUT_FOLDER.iterdir()
    if file.suffix.lower() in [".jpg", ".jpeg", ".png"]
]

print("Starting Image Preprocessing...")
print("Total images:", len(image_files))

processed = 0

for image_path in image_files:

    print("\nProcessing:", image_path.name)

    image = cv2.imread(str(image_path))

    if image is None:
        print("Unable to read image!")
        continue

    # 1. Convert to grayscale
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 2. Improve contrast using CLAHE
    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    enhanced = clahe.apply(grayscale)

    # 3. Remove noise
    blurred = cv2.GaussianBlur(enhanced, (3, 3), 0)

    # 4. Apply adaptive thresholding
    threshold = cv2.adaptiveThreshold(
        blurred,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    # Save grayscale image
    gray_name = image_path.stem + "_grayscale.jpg"
    cv2.imwrite(str(OUTPUT_FOLDER / gray_name), grayscale)

    # Save enhanced image
    enhanced_name = image_path.stem + "_enhanced.jpg"
    cv2.imwrite(str(OUTPUT_FOLDER / enhanced_name), threshold)

    print("Grayscale saved:", gray_name)
    print("Enhanced saved:", enhanced_name)

    processed += 1

print("\n" + "=" * 45)
print("IMAGE PREPROCESSING COMPLETED")
print("=" * 45)

print("Total images:", len(image_files))
print("Successfully processed:", processed)
print("Output folder:", OUTPUT_FOLDER)
