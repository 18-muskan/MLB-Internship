
import cv2
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

# Get original dimensions
height, width = img.shape[:2]

print("Original Image Size:", width, "x", height)

# 1. Upscaling - Double the size
larger = cv2.resize(
    img,
    None,
    fx=2,
    fy=2,
    interpolation=cv2.INTER_LINEAR
)

# 2. Downscaling - Half the size
smaller = cv2.resize(
    img,
    None,
    fx=0.5,
    fy=0.5,
    interpolation=cv2.INTER_AREA
)

# 3. Custom resizing
custom = cv2.resize(
    img,
    (500, 500),
    interpolation=cv2.INTER_LINEAR
)

# Create output folder
output_dir = os.path.join(current_dir, "scaling_outputs")
os.makedirs(output_dir, exist_ok=True)

# Save images
cv2.imwrite(os.path.join(output_dir, "upscaled.jpg"), larger)
cv2.imwrite(os.path.join(output_dir, "downscaled.jpg"), smaller)
cv2.imwrite(os.path.join(output_dir, "custom_resized.jpg"), custom)

print("Upscaled Size:", larger.shape[1], "x", larger.shape[0])
print("Downscaled Size:", smaller.shape[1], "x", smaller.shape[0])
print("Custom Size:", custom.shape[1], "x", custom.shape[0])

print("All scaling operations completed successfully!")

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Upscaled Image", larger)
cv2.imshow("Downscaled Image", smaller)
cv2.imshow("Custom Resized Image", custom)

cv2.waitKey(0)
cv2.destroyAllWindows()
