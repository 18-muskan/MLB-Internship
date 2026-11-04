
import cv2
import os

# Folder containing input images
input_folder = "input_images"

# List of image files
image_files = [
    "landscape.jpg",
    "person.jpg",
    "vehicle.jpg",
    "document.jpg",
    "object.jpg"
]

print("\n========== IMAGE INFORMATION REPORT ==========\n")

# Process each image
for image_name in image_files:

    image_path = os.path.join(input_folder, image_name)

    img = cv2.imread(image_path)

    if img is None:
        print("Image not found:", image_name)
        continue

    # Get image dimensions
    height, width = img.shape[:2]

    # Get number of channels
    if len(img.shape) == 2:
        channels = 1
    else:
        channels = img.shape[2]

    # Get file size
    file_size = os.path.getsize(image_path)

    print("----------------------------------------")
    print("Image Name:", image_name)
    print("Height:", height, "pixels")
    print("Width:", width, "pixels")
    print("Channels:", channels)
    print("File Size:", file_size, "bytes")
    print("File Size:", round(file_size / 1024, 2), "KB")

print("\n========== REPORT COMPLETED ==========")
