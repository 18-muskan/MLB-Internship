
import cv2
import os
import numpy as np

# Input and output folders
input_dir = "Enhanced_Outputs/Perspective_Corrected"
dataset_dir = "Dataset"

final_dir = "Enhanced_Outputs/Final_Enhanced"
comparison_dir = "Comparisons"

os.makedirs(final_dir, exist_ok=True)
os.makedirs(comparison_dir, exist_ok=True)


def enhance_document(image):

    # 1. Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 2. Reduce noise
    denoised = cv2.bilateralFilter(gray, 9, 75, 75)

    # 3. Improve contrast using CLAHE
    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    contrast = clahe.apply(denoised)

    # 4. Adjust brightness
    bright = cv2.convertScaleAbs(
        contrast,
        alpha=1.2,
        beta=10
    )

    # 5. Sharpen image
    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])

    sharpened = cv2.filter2D(
        bright,
        -1,
        kernel
    )

    return sharpened


def create_comparison(original, enhanced, output_path):

    # Convert enhanced grayscale image to BGR
    enhanced_color = cv2.cvtColor(
        enhanced,
        cv2.COLOR_GRAY2BGR
    )

    # Resize both images to the same height
    height = 400

    original_width = int(
        original.shape[1] * height / original.shape[0]
    )

    enhanced_width = int(
        enhanced_color.shape[1] * height / enhanced_color.shape[0]
    )

    original_resized = cv2.resize(
        original,
        (original_width, height)
    )

    enhanced_resized = cv2.resize(
        enhanced_color,
        (enhanced_width, height)
    )

    # Add labels
    cv2.putText(
        original_resized,
        "Original",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255),
        2
    )

    cv2.putText(
        enhanced_resized,
        "Enhanced",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 150, 0),
        2
    )

    comparison = np.hstack((
        original_resized,
        enhanced_resized
    ))

    cv2.imwrite(output_path, comparison)


# Process all 10 corrected images
for number in range(1, 11):

    filename = f"img{number}_corrected.jpg"

    corrected_path = os.path.join(
        input_dir,
        filename
    )

    original_path = os.path.join(
        dataset_dir,
        f"img{number}.jpg"
    )

    corrected_image = cv2.imread(corrected_path)
    original_image = cv2.imread(original_path)

    if corrected_image is None:
        print("Corrected image not found:", filename)
        continue

    if original_image is None:
        print("Original image not found:", f"img{number}.jpg")
        continue

    # Apply enhancement
    enhanced_image = enhance_document(corrected_image)

    # Save final enhanced image
    output_name = f"img{number}_enhanced.jpg"

    output_path = os.path.join(
        final_dir,
        output_name
    )

    cv2.imwrite(output_path, enhanced_image)

    # Save original vs final comparison
    comparison_path = os.path.join(
        comparison_dir,
        f"img{number}_comparison.jpg"
    )

    create_comparison(
        original_image,
        enhanced_image,
        comparison_path
    )

    print("Enhanced successfully:", output_name)


print("\nAll document images processed successfully!")
print("Final images saved in:", final_dir)
print("Comparisons saved in:", comparison_dir)
