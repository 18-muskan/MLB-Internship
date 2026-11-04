
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

print("\n========== IMAGE FLIPPING ==========\n")

for image_name in image_files:

    image_path = os.path.join(input_folder, image_name)
    img = cv2.imread(image_path)

    if img is None:
        print("Image not found:", image_name)
        continue

    category = os.path.splitext(image_name)[0]
    save_folder = os.path.join(output_folder, category)

    os.makedirs(save_folder, exist_ok=True)

    # Horizontal flip
    horizontal_flip = cv2.flip(img, 1)

    # Vertical flip
    vertical_flip = cv2.flip(img, 0)

    # Both horizontal and vertical flip
    both_flip = cv2.flip(img, -1)

    flips = {
        "horizontal": horizontal_flip,
        "vertical": vertical_flip,
        "both": both_flip
    }

    for flip_name, flipped_image in flips.items():

        output_path = os.path.join(
            save_folder,
            f"flipped_{flip_name}.jpg"
        )

        cv2.imwrite(output_path, flipped_image)

        print("Image:", image_name)
        print("Flip Type:", flip_name)
        print("Flipped Shape:", flipped_image.shape)
        print("Saved:", output_path)
        print("--------------------------------")

print("\n========== FLIPPING COMPLETED ==========")
