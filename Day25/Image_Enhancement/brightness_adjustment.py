
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

# 1. Increase brightness
bright = cv2.convertScaleAbs(
    img,
    alpha=1.0,
    beta=50
)

# 2. Decrease brightness
dark = cv2.convertScaleAbs(
    img,
    alpha=1.0,
    beta=-50
)

# Create output folder
output_dir = os.path.join(
    current_dir, "brightness_outputs"
)

os.makedirs(output_dir, exist_ok=True)

# Save results
cv2.imwrite(
    os.path.join(output_dir, "increased_brightness.jpg"),
    bright
)

cv2.imwrite(
    os.path.join(output_dir, "decreased_brightness.jpg"),
    dark
)

print("Brightness adjustment completed successfully!")

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Increased Brightness", bright)
cv2.imshow("Decreased Brightness", dark)

cv2.waitKey(0)
cv2.destroyAllWindows()
