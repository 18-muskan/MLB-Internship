
import cv2
import numpy as np
import os

# Folder paths
dataset_dir = "Dataset"
output_dir = "Enhanced_Outputs/Perspective_Corrected"

os.makedirs(output_dir, exist_ok=True)

# Five tilted document images
image_names = [f"img{i}.jpg" for i in range(1, 6)]


def order_points(points):

    points = np.array(points, dtype="float32")

    # Find the center of four corners
    center = np.mean(points, axis=0)

    # Arrange points clockwise
    angles = np.arctan2(
        points[:, 1] - center[1],
        points[:, 0] - center[0]
    )

    ordered = points[np.argsort(angles)]

    # Start from the topmost corner
    start_index = np.argmin(ordered[:, 1])

    ordered = np.roll(ordered, -start_index, axis=0)

    return ordered.astype("float32")


def correct_perspective(image, points):

    source_points = order_points(points)

    top_left, top_right, bottom_right, bottom_left = source_points

    width = int(max(
        np.linalg.norm(bottom_right - bottom_left),
        np.linalg.norm(top_right - top_left)
    ))

    height = int(max(
        np.linalg.norm(top_right - bottom_right),
        np.linalg.norm(top_left - bottom_left)
    ))

    if width < 2 or height < 2:
        return None

    destination_points = np.array([
        [0, 0],
        [width - 1, 0],
        [width - 1, height - 1],
        [0, height - 1]
    ], dtype="float32")

    matrix = cv2.getPerspectiveTransform(
        source_points,
        destination_points
    )

    corrected = cv2.warpPerspective(
        image,
        matrix,
        (width, height)
    )

    return corrected


# Process all five tilted images
for image_name in image_names:

    image_path = os.path.join(dataset_dir, image_name)
    original = cv2.imread(image_path)

    if original is None:
        print("Image not found:", image_name)
        continue

    display_image = original.copy()
    points = []

    print("\nProcessing:", image_name)
    print("Click the four document corners in ANY order.")
    print("Press ESC to cancel.")

    def select_corners(event, x, y, flags, param):

        if event == cv2.EVENT_LBUTTONDOWN and len(points) < 4:

            points.append([x, y])

            cv2.circle(
                display_image,
                (x, y),
                5,
                (0, 255, 0),
                -1
            )

            cv2.putText(
                display_image,
                str(len(points)),
                (x + 7, y - 7),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2
            )

            cv2.imshow("Select Document Corners", display_image)

            print("Corner selected:", x, y)

    cv2.namedWindow("Select Document Corners")
    cv2.setMouseCallback("Select Document Corners", select_corners)

    cv2.imshow("Select Document Corners", display_image)

    key = cv2.waitKey(0)
    cv2.destroyAllWindows()

    if key == 27 or len(points) != 4:
        print("Image skipped:", image_name)
        continue

    corrected = correct_perspective(original, points)

    if corrected is None:
        print("Invalid corner selection:", image_name)
        continue

    output_name = os.path.splitext(image_name)[0] + "_corrected.jpg"

    output_path = os.path.join(output_dir, output_name)

    cv2.imwrite(output_path, corrected)

    print("Perspective correction completed:", output_name)

    cv2.imshow("Corrected Document", corrected)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


print("\nManual perspective correction process completed!")
