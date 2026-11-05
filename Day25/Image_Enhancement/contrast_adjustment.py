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

# 1. Increase contrast
high_contrast = cv2.convertScaleAbs(
    img,
    alpha=1.8,
    beta=0
)

# 2. Decrease contrast
low_contrast = cv2.convertScaleAbs(
    img,
    alpha=0.5,
    beta=0
)

# Create output folder
output_dir = os.path.join(
    current_dir, "contrast_outputs"
)

os.makedirs(output_dir, exist_ok=True)

# Save images
cv2.imwrite(
    os.path.join(output_dir, "high_contrast.jpg"),
    high_contrast
)

cv2.imwrite(
    os.path.join(output_dir, "low_contrast.jpg"),
    low_contrast
)

print("Contrast adjustment completed successfully!")

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("High Contrast", high_contrast)
cv2.imshow("Low Contrast", low_contrast)

cv2.waitKey(0)
cv2.destroyAllWindows()