
import cv2
import numpy as np
import os

# Get current script directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load image
image_path = os.path.join(
    current_dir, "..", "Input_Images", "sample.jpg"
)

img = cv2.imread(image_path)

if img is None:
    print("Error: Image not found!")
    exit()

height, width = img.shape[:2]

# Three points from original image
original_points = np.float32([
    [50, 50],
    [250, 50],
    [50, 180]
])

# Three corresponding points in output image
new_points = np.float32([
    [80, 80],
    [270, 50],
    [100, 200]
])

# Calculate affine transformation matrix
matrix = cv2.getAffineTransform(
    original_points,
    new_points
)

# Apply affine transformation
result = cv2.warpAffine(
    img,
    matrix,
    (width, height)
)

# Create output folder
output_dir = os.path.join(current_dir, "affine_outputs")
os.makedirs(output_dir, exist_ok=True)

# Save result
output_path = os.path.join(
    output_dir, "affine_transformed.jpg"
)

cv2.imwrite(output_path, result)

print("Affine Transformation completed successfully!")
print("Original Image Size:", width, "x", height)
print("Transformed image saved successfully!")

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Affine Transformation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
