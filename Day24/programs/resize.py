
import cv2
import os

# Input folder
input_folder = "input_images"

# Output folder
output_folder = "output"

# Image names
image_files = [
    "landscape.jpg",
    "person.jpg",
    "vehicle.jpg",
    "document.jpg",
    "object.jpg"
]

# Different resolutions (width, height)
resolutions = {
    "small": (200, 150),
    "medium": (400, 300),
    "large": (600, 400)
}

print("\n========== IMAGE RESIZING ==========\n")

for image_name in image_files:

    image_path = os.path.join(input_folder, image_name)
    img = cv2.imread(image_path)

    if img is None:
        print("Image not found:", image_name)
        continue

    category = os.path.splitext(image_name)[0]

    for size_name, dimensions in resolutions.items():

        # Resize image
        resized = cv2.resize(img, dimensions)

        # Create output folder
        save_folder = os.path.join(output_folder, category)
        os.makedirs(save_folder, exist_ok=True)

        # Save resized image
        output_path = os.path.join(
            save_folder,
            f"resized_{size_name}.jpg"
        )

        cv2.imwrite(output_path, resized)

        print("Image:", image_name)
        print("Resolution:", size_name)
        print("New Shape:", resized.shape)
        print("Saved:", output_path)
        print("--------------------------------")

print("\n========== RESIZING COMPLETED ==========")
