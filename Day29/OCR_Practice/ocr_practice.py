
import easyocr
import os
import cv2

# Folder paths
IMAGE_FOLDER = "../dataset/sample_images"
OUTPUT_FOLDER = "../extracted_text"

# Create output folder if it does not exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Initialize EasyOCR
print("Loading EasyOCR model...")
reader = easyocr.Reader(['en'], gpu=False)

print("\nEasyOCR model loaded successfully!")

# Supported image extensions
image_extensions = (".jpg", ".jpeg", ".png", ".bmp")

# Get all images
image_files = [
    file for file in os.listdir(IMAGE_FOLDER)
    if file.lower().endswith(image_extensions)
]

print(f"\nTotal images found: {len(image_files)}")

successful = 0
failed = 0

# Process each image
for image_name in sorted(image_files):

    image_path = os.path.join(IMAGE_FOLDER, image_name)

    print("\n" + "=" * 55)
    print("Processing:", image_name)
    print("=" * 55)

    try:
        # Check whether image can be opened
        image = cv2.imread(image_path)

        if image is None:
            print("Error: Unable to open image.")
            failed += 1
            continue

        # Extract text using EasyOCR
        results = reader.readtext(image_path)

        extracted_text = []

        for box, text, confidence in results:

            print(f"Text: {text}")
            print(f"Confidence: {confidence:.2f}")

            extracted_text.append(text)

        # Save extracted text
        output_name = os.path.splitext(image_name)[0] + ".txt"
        output_path = os.path.join(OUTPUT_FOLDER, output_name)

        with open(output_path, "w", encoding="utf-8") as file:
            file.write("\n".join(extracted_text))

        print("Saved:", output_path)

        successful += 1

    except Exception as error:
        print("Processing error:", error)
        failed += 1

# Final summary
print("\n" + "=" * 55)
print("OCR PROCESSING COMPLETED")
print("=" * 55)

print("Total images:", len(image_files))
print("Successfully processed:", successful)
print("Failed images:", failed)
print("Extracted text folder:", OUTPUT_FOLDER)
