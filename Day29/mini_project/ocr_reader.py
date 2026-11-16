
import easyocr
import cv2
from pathlib import Path
import matplotlib.pyplot as plt

# Project folders
BASE_DIR = Path(__file__).resolve().parents[1]

IMAGE_FOLDER = BASE_DIR / "dataset" / "sample_images"
OUTPUT_FOLDER = BASE_DIR / "extracted_text"

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

# Load EasyOCR model
print("Loading EasyOCR...")
reader = easyocr.Reader(['en'], gpu=False)

print("\nOCR Reader is ready!")

# Show available images
image_files = sorted([
    file for file in IMAGE_FOLDER.iterdir()
    if file.suffix.lower() in [".jpg", ".jpeg", ".png"]
])

print("\nAvailable Images:")

for index, image in enumerate(image_files, start=1):
    print(f"{index}. {image.name}")

# Select image
try:
    choice = int(input("\nEnter image number: "))

    if choice < 1 or choice > len(image_files):
        print("Invalid image number!")
        raise SystemExit

    selected_image = image_files[choice - 1]

except ValueError:
    print("Please enter a valid number!")
    raise SystemExit

# Read image
image = cv2.imread(str(selected_image))

if image is None:
    print("Unable to load image!")
    raise SystemExit

# Extract text
print("\nExtracting text...")
results = reader.readtext(image)

extracted_text = []

for box, text, confidence in results:
    extracted_text.append(text)
    print(f"Text: {text} | Confidence: {confidence:.2f}")

# Combine extracted text
final_text = "\n".join(extracted_text)

# Save text file
output_file = OUTPUT_FOLDER / (
    selected_image.stem + "_mini_project.txt"
)

with open(output_file, "w", encoding="utf-8") as file:
    file.write(final_text)

print("\nExtracted Text:")
print("-" * 40)
print(final_text if final_text else "No text detected.")

print("\nText saved successfully:")
print(output_file)

# Display original image
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10, 6))
plt.imshow(image_rgb)
plt.title("Original Image: " + selected_image.name)
plt.axis("off")
plt.tight_layout()
plt.show()
