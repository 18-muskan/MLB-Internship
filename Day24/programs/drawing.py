
import cv2
import os
import numpy as np

input_folder = "input_images"
output_folder = "output"

image_files = [
    "landscape.jpg",
    "person.jpg",
    "vehicle.jpg",
    "document.jpg",
    "object.jpg"
]

print("\n========== DRAWING ON IMAGES ==========\n")

for image_name in image_files:

    image_path = os.path.join(input_folder, image_name)
    img = cv2.imread(image_path)

    if img is None:
        print("Image not found:", image_name)
        continue

    height, width = img.shape[:2]

    # Draw rectangle
    cv2.rectangle(
        img,
        (10, 10),
        (width - 10, height - 10),
        (0, 255, 0),
        2
    )

    # Draw circle
    cv2.circle(
        img,
        (width // 2, height // 2),
        30,
        (255, 0, 0),
        2
    )

    # Draw line
    cv2.line(
        img,
        (0, 0),
        (width, height),
        (0, 0, 255),
        2
    )

    # Draw polygon
    points = np.array([
        [width // 4, height // 4],
        [width // 2, height // 4],
        [width // 2, height // 2]
    ], np.int32)

    points = points.reshape((-1, 1, 2))

    cv2.polylines(
        img,
        [points],
        True,
        (0, 255, 255),
        2
    )

    # Add text
    cv2.putText(
        img,
        "OpenCV",
        (10, height - 15),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (255, 255, 255),
        1
    )

    category = os.path.splitext(image_name)[0]
    save_folder = os.path.join(output_folder, category)

    os.makedirs(save_folder, exist_ok=True)

    output_path = os.path.join(save_folder, "drawing.jpg")

    cv2.imwrite(output_path, img)

    print("Image:", image_name)
    print("Drawing: Rectangle, Circle, Line, Polygon and Text")
    print("Saved:", output_path)
    print("--------------------------------")

print("\n========== DRAWING COMPLETED ==========")
