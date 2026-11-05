
import cv2
import os

# Load input image in grayscale
image_path = "Input_Images/sample.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Image not found!")
else:
    # Create CLAHE object
    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    # Apply CLAHE
    enhanced_image = clahe.apply(image)

    # Create output directory
    output_dir = "Image_Enhancement/clahe_outputs"
    os.makedirs(output_dir, exist_ok=True)

    # Save enhanced image
    output_path = os.path.join(output_dir, "clahe_enhanced.jpg")
    cv2.imwrite(output_path, enhanced_image)

    print("CLAHE enhancement completed successfully!")
