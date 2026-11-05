
import cv2
import numpy as np
import os

# Get the current script directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load input image
image_path = os.path.join(
    current_dir, "..", "Input_Images", "sample.jpg"
)

img = cv2.imread(image_path)

if img is None:
    print("Error: Image not found. Check the image path.")
    exit()

height, width = img.shape[:2]

# 1. Move image to the right
right_matrix = np.float32([
    [1, 0, 100],
    [0, 1, 0]
])

right = cv2.warpAffine(img, right_matrix, (width, height))

# 2. Move image to the left
left_matrix = np.float32([
    [1, 0, -100],
    [0, 1, 0]
])

left = cv2.warpAffine(img, left_matrix, (width, height))

# 3. Move image downward
down_matrix = np.float32([
    [1, 0, 0],
    [0, 1, 100]
])

down = cv2.warpAffine(img, down_matrix, (width, height))

# 4. Move image upward
up_matrix = np.float32([
    [1, 0, 0],
    [0, 1, -100]
])

up = cv2.warpAffine(img, up_matrix, (width, height))

# Create output folder
output_dir = os.path.join(current_dir, "outputs")
os.makedirs(output_dir, exist_ok=True)

# Save all results
cv2.imwrite(os.path.join(output_dir, "translated_right.jpg"), right)
cv2.imwrite(os.path.join(output_dir, "translated_left.jpg"), left)
cv2.imwrite(os.path.join(output_dir, "translated_down.jpg"), down)
cv2.imwrite(os.path.join(output_dir, "translated_up.jpg"), up)

print("Translation completed successfully!")
print("Original image size:", width, "x", height)
print("All translated images saved in outputs folder.")

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Moved Right", right)
cv2.imshow("Moved Left", left)
cv2.imshow("Moved Down", down)
cv2.imshow("Moved Up", up)

cv2.waitKey(0)
cv2.destroyAllWindows()
