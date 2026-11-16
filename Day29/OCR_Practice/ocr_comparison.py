
import easyocr
import cv2
import csv
from pathlib import Path

# Project folders
BASE_DIR = Path(__file__).resolve().parents[1]

IMAGE_FOLDER = BASE_DIR / "dataset" / "sample_images"
PROCESSED_FOLDER = BASE_DIR / "dataset" / "processed_images"
OUTPUT_FOLDER = BASE_DIR / "extracted_text"

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

# Load EasyOCR
print("Loading EasyOCR model...")
reader = easyocr.Reader(['en'], gpu=False)

print("EasyOCR loaded successfully!")

# CSV report
csv_path = OUTPUT_FOLDER / "ocr_comparison.csv"

image_files = sorted([
    file for file in IMAGE_FOLDER.iterdir()
    if file.suffix.lower() in [".jpg", ".jpeg", ".png"]
])

comparison_data = []

for image_path in image_files:

    enhanced_path = PROCESSED_FOLDER / (
        image_path.stem + "_enhanced.jpg"
    )

    print("\n" + "=" * 50)
    print("Image:", image_path.name)

    original_image = cv2.imread(str(image_path))
    enhanced_image = cv2.imread(str(enhanced_path))

    if original_image is None or enhanced_image is None:
        print("Unable to read image. Skipping.")
        continue

    # OCR on original image
    original_results = reader.readtext(original_image)

    # OCR on enhanced image
    enhanced_results = reader.readtext(enhanced_image)

    original_text = " ".join(
        [result[1] for result in original_results]
    )

    enhanced_text = " ".join(
        [result[1] for result in enhanced_results]
    )

    # Calculate average confidence
    original_confidence = (
        sum(result[2] for result in original_results)
        / len(original_results)
        if original_results else 0
    )

    enhanced_confidence = (
        sum(result[2] for result in enhanced_results)
        / len(enhanced_results)
        if enhanced_results else 0
    )

    print("\nOriginal OCR:")
    print(original_text)

    print("\nEnhanced OCR:")
    print(enhanced_text)

    print("\nOriginal average confidence:",
          round(original_confidence, 3))

    print("Enhanced average confidence:",
          round(enhanced_confidence, 3))

    comparison_data.append([
        image_path.name,
        original_text,
        enhanced_text,
        round(original_confidence, 3),
        round(enhanced_confidence, 3)
    ])

# Save comparison report
with open(csv_path, "w", newline="", encoding="utf-8-sig") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Image Name",
        "Original OCR Text",
        "Enhanced OCR Text",
        "Original Average Confidence",
        "Enhanced Average Confidence"
    ])

    writer.writerows(comparison_data)

print("\n" + "=" * 50)
print("OCR COMPARISON COMPLETED")
print("=" * 50)

print("Images compared:", len(comparison_data))
print("Comparison report:", csv_path)
