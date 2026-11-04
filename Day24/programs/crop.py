
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

print("\n========== IMAGE CROPPING ==========\n")

for image_name in image_files:

    image_path = os.path.join(input_folder, image_name)
    img = cv2.imread(image_path)

    if img is None:
        print("Image not found:", image_name)
        continue

    height, width = img.shape[:2]

    # Define crop regions
    crop_regions = {
        "top_left": (0, 0, width // 2, height // 2),
        "center": (width // 4, height // 4,
                   3 * width // 4, 3 * height // 4),
        "bottom_right": (width // 2, height // 2,
                         width, height)
    }

    category = os.path.splitext(image_name)[0]
    save_folder = os.path.join(output_folder, category)

    os.makedirs(save_folder, exist_ok=True)

    for region_name, coordinates in crop_regions.items():

        x1, y1, x2, y2 = coordinates

        # Crop selected region
        cropped = img[y1:y2, x1:x2]

        # Save cropped image
        output_path = os.path.join(
            save_folder,
            f"cropped_{region_name}.jpg"
        )

        cv2.imwrite(output_path, cropped)

        print("Image:", image_name)
        print("Region:", region_name)
        print("Cropped Shape:", cropped.shape)
        print("Saved:", output_path)
        print("--------------------------------")

print("\n========== CROPPING COMPLETED ==========")
