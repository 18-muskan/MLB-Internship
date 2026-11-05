
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

height, width = img.shape[:2]

# Find image center
center = (width // 2, height // 2)

# Create output folder
output_dir = os.path.join(current_dir, "rotation_outputs")
os.makedirs(output_dir, exist_ok=True)

# Rotation angles
angles = [45, 90, 180, 270]

for angle in angles:

    # Create rotation matrix
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    # Apply rotation
    rotated = cv2.warpAffine(
        img,
        matrix,
        (width, height)
    )

    # Save rotated image
    output_path = os.path.join(
        output_dir, f"rotated_{angle}.jpg"
    )

    cv2.imwrite(output_path, rotated)

    print(f"Image rotated by {angle} degrees successfully!")

    # Display image
    cv2.imshow(f"Rotation {angle} Degrees", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("All rotated images saved successfully!")
