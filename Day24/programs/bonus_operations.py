
import cv2
import os

# Project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

input_folder = os.path.join(BASE_DIR, "input_images")
output_folder = os.path.join(BASE_DIR, "output", "bonus")

os.makedirs(output_folder, exist_ok=True)

image_name = "landscape.jpg"
image_path = os.path.join(input_folder, image_name)

# Load original image
img = cv2.imread(image_path)

if img is None:
    print("Image not found!")
    exit()

print("\n========== BONUS IMAGE OPERATIONS ==========")

# 1. Increase Brightness
bright_image = cv2.convertScaleAbs(img, alpha=1, beta=50)

bright_path = os.path.join(output_folder, "bright_image.jpg")
cv2.imwrite(bright_path, bright_image)

print("Brightness increased successfully!")
print("Saved:", bright_path)

# 2. Decrease Brightness
dark_image = cv2.convertScaleAbs(img, alpha=1, beta=-50)

dark_path = os.path.join(output_folder, "dark_image.jpg")
cv2.imwrite(dark_path, dark_image)

print("Brightness decreased successfully!")
print("Saved:", dark_path)

# 3. Increase Contrast
contrast_image = cv2.convertScaleAbs(img, alpha=1.5, beta=0)

contrast_path = os.path.join(output_folder, "contrast_image.jpg")
cv2.imwrite(contrast_path, contrast_image)

print("Contrast increased successfully!")
print("Saved:", contrast_path)

# 4. BGR to RGB Conversion
rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

rgb_path = os.path.join(output_folder, "rgb_image.png")
cv2.imwrite(rgb_path, rgb_image)

print("BGR to RGB conversion completed!")
print("Saved:", rgb_path)

# 5. Display original and processed images
cv2.imshow("Original Image", img)
cv2.imshow("Bright Image", bright_image)
cv2.imshow("Dark Image", dark_image)
cv2.imshow("Contrast Image", contrast_image)
cv2.imshow("RGB Image", rgb_image)

print("\nPress any key on the image windows to close.")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("\n========== BONUS OPERATIONS COMPLETED ==========")
