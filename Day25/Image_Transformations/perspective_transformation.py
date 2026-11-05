
import cv2
import numpy as np
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

image_path = os.path.join(
    current_dir, "..", "Input_Images", "document.jpg"
)

img = cv2.imread(image_path)

if img is None:
    print("Error: Document image not found!")
    exit()

original = img.copy()
points = []

def select_points(event, x, y, flags, param):

    global points

    if event == cv2.EVENT_LBUTTONDOWN:

        if len(points) < 4:
            points.append([x, y])

            cv2.circle(
                img, (x, y), 5, (0, 255, 0), -1
            )

            cv2.imshow("Select Document Corners", img)

            print("Selected point:", len(points), x, y)


cv2.namedWindow("Select Document Corners")
cv2.setMouseCallback(
    "Select Document Corners", select_points
)

print("Select four document corners in this order:")
print("1. Top-left")
print("2. Top-right")
print("3. Bottom-right")
print("4. Bottom-left")
print("Press R to reset points.")
print("Press Q to quit.")

while True:

    cv2.imshow("Select Document Corners", img)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('r'):
        points = []
        img = original.copy()
        print("Points reset. Select again.")

    elif key == ord('q'):
        break

    elif len(points) == 4:
        break

cv2.destroyAllWindows()

if len(points) != 4:
    print("Error: Four points were not selected.")
    exit()

# Convert points into NumPy array
source_points = np.float32(points)

# Calculate output width and height
top_width = np.linalg.norm(source_points[1] - source_points[0])
bottom_width = np.linalg.norm(source_points[2] - source_points[3])

left_height = np.linalg.norm(source_points[3] - source_points[0])
right_height = np.linalg.norm(source_points[2] - source_points[1])

output_width = int(max(top_width, bottom_width))
output_height = int(max(left_height, right_height))

# Define rectangular destination points
destination_points = np.float32([
    [0, 0],
    [output_width - 1, 0],
    [output_width - 1, output_height - 1],
    [0, output_height - 1]
])

# Calculate perspective transformation matrix
matrix = cv2.getPerspectiveTransform(
    source_points, destination_points
)

# Apply perspective transformation
result = cv2.warpPerspective(
    original,
    matrix,
    (output_width, output_height)
)

# Create output folder
output_dir = os.path.join(
    current_dir, "perspective_outputs"
)

os.makedirs(output_dir, exist_ok=True)

# Save corrected image
output_path = os.path.join(
    output_dir, "perspective_corrected.jpg"
)

cv2.imwrite(output_path, result)

print("Perspective Transformation completed successfully!")
print("Corrected Image Size:", output_width, "x", output_height)
print("Output saved successfully!")

cv2.imshow("Original Document", original)
cv2.imshow("Perspective Corrected", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
