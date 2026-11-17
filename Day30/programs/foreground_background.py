
import cv2
import os
import numpy as np

# Get main project folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASET_DIR = os.path.join(BASE_DIR, "dataset")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs", "foreground")

os.makedirs(OUTPUT_DIR, exist_ok=True)


def remove_background(image_path):

    image = cv2.imread(image_path)

    if image is None:
        print("Image could not be loaded:", image_path)
        return

    height, width = image.shape[:2]

    # Create a mask for GrabCut
    mask = np.zeros((height, width), np.uint8)

    # Define rectangle around the main object
    margin_x = max(1, int(width * 0.05))
    margin_y = max(1, int(height * 0.05))

    rect = (
        margin_x,
        margin_y,
        max(1, width - 2 * margin_x),
        max(1, height - 2 * margin_y)
    )

    # Create background and foreground models
    background_model = np.zeros((1, 65), np.float64)
    foreground_model = np.zeros((1, 65), np.float64)

    # Apply GrabCut algorithm
    cv2.grabCut(
        image,
        mask,
        rect,
        background_model,
        foreground_model,
        5,
        cv2.GC_INIT_WITH_RECT
    )

    # Convert mask into binary foreground mask
    foreground_mask = np.where(
        (mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD),
        255,
        0
    ).astype("uint8")

    # Create white background
    result = np.full_like(image, 255)

    # Keep only foreground pixels
    result[foreground_mask == 255] = image[foreground_mask == 255]

    filename = os.path.splitext(os.path.basename(image_path))[0]

    output_path = os.path.join(
        OUTPUT_DIR,
        filename + "_foreground.jpg"
    )

    cv2.imwrite(output_path, result)

    print("Background removed:", filename)


def main():

    print("FOREGROUND AND BACKGROUND SEGMENTATION")
    print("--------------------------------------")

    total_images = 0

    for category in os.listdir(DATASET_DIR):

        category_path = os.path.join(DATASET_DIR, category)

        if not os.path.isdir(category_path):
            continue

        for filename in os.listdir(category_path):

            if filename.lower().endswith((".jpg", ".jpeg", ".png")):

                image_path = os.path.join(category_path, filename)

                remove_background(image_path)
                total_images += 1

    print("\nProcessing completed!")
    print("Total images processed:", total_images)
    print("Results saved in outputs/foreground")


if __name__ == "__main__":
    main()
