
import cv2
import os

input_folder = "input_images"
output_folder = "output"

image_files = [
    "landscape.jpg",
    "person.jpg",
    "vehicle.jpg",
    "document.jpg",
    "object.jpg"
]

print("\n========== IMAGE ROTATION ==========\n")

for image_name in image_files:

    image_path = os.path.join(input_folder, image_name)
    img = cv2.imread(image_path)

    if img is None:
        print("Image not found:", image_name)
        continue

    category = os.path.splitext(image_name)[0]
    save_folder = os.path.join(output_folder, category)

    os.makedirs(save_folder, exist_ok=True)

    # Rotate image by 90 degrees clockwise
    rotated_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    # Rotate image by 180 degrees
    rotated_180 = cv2.rotate(img, cv2.ROTATE_180)

    # Rotate image by 270 degrees clockwise
    rotated_270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

    rotations = {
        "90": rotated_90,
        "180": rotated_180,
        "270": rotated_270
    }

    for angle, rotated_image in rotations.items():

        output_path = os.path.join(
            save_folder,
            f"rotated_{angle}.jpg"
        )

        cv2.imwrite(output_path, rotated_image)

        print("Image:", image_name)
        print("Rotation:", angle, "degrees")
        print("Rotated Shape:", rotated_image.shape)
        print("Saved:", output_path)
        print("--------------------------------")

print("\n========== ROTATION COMPLETED ==========")
