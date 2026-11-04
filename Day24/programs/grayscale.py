
import cv2
import os

# Input folder
input_folder = "input_images"

# Output folder
output_folder = "output"

# List of images
image_files = [
    "landscape.jpg",
    "person.jpg",
    "vehicle.jpg",
    "document.jpg",
    "object.jpg"
]

print("\n========== GRAYSCALE CONVERSION ==========\n")

for image_name in image_files:

    # Read image
    image_path = os.path.join(input_folder, image_name)
    img = cv2.imread(image_path)

    if img is None:
        print("Image not found:", image_name)
        continue

    # Convert BGR image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Create separate output folder for each image
    category = os.path.splitext(image_name)[0]
    save_folder = os.path.join(output_folder, category)

    os.makedirs(save_folder, exist_ok=True)

    # Save grayscale image
    output_path = os.path.join(save_folder, "grayscale.jpg")
    cv2.imwrite(output_path, gray)

    print("Image:", image_name)
    print("Original Shape:", img.shape)
    print("Grayscale Shape:", gray.shape)
    print("Saved:", output_path)
    print("----------------------------------------")

print("\n========== GRAYSCALE CONVERSION COMPLETED ==========")
