
import cv2
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "output_images"

thumbnails = []

for i in range(1, 6):
    path = IMAGE_DIR / f"video_{i}_preview.jpg"
    image = cv2.imread(str(path))

    if image is None:
        print(f"Missing image: {path.name}")
        continue

    image = cv2.resize(image, (480, 270))
    cv2.putText(
        image, f"VIDEO {i}", (15, 35),
        cv2.FONT_HERSHEY_SIMPLEX, 1,
        (0, 255, 0), 2
    )
    thumbnails.append(image)

if thumbnails:
    blank = np.zeros((270, 480, 3), dtype=np.uint8)
    while len(thumbnails) < 6:
        thumbnails.append(blank.copy())

    rows = [
        np.hstack(thumbnails[0:2]),
        np.hstack(thumbnails[2:4]),
        np.hstack(thumbnails[4:6])
    ]

    sheet = np.vstack(rows)
    output = IMAGE_DIR / "all_videos_preview.jpg"

    cv2.imwrite(str(output), sheet)
    print(f"Contact sheet saved: {output}")
else:
    print("No preview images found!")
