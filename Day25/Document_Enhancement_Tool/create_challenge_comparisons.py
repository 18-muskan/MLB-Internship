
import cv2
import numpy as np
import os

# Folder paths
dataset_dir = "Dataset"
corrected_dir = "Enhanced_Outputs/Perspective_Corrected"
enhanced_dir = "Enhanced_Outputs/Final_Enhanced"
output_dir = "Challenge_Results"

os.makedirs(output_dir, exist_ok=True)


def prepare_panel(image, label):

    # Convert grayscale image to color
    if len(image.shape) == 2:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    # Resize while maintaining aspect ratio
    target_width = 350
    target_height = 420

    h, w = image.shape[:2]

    scale = min(target_width / w, target_height / h)

    new_width = int(w * scale)
    new_height = int(h * scale)

    resized = cv2.resize(
        image,
        (new_width, new_height)
    )

    # Create white background
    canvas = np.full(
        (target_height + 50, target_width, 3),
        255,
        dtype=np.uint8
    )

    x = (target_width - new_width) // 2
    y = 50 + (target_height - new_height) // 2

    canvas[y:y + new_height, x:x + new_width] = resized

    # Add label
    cv2.putText(
        canvas,
        label,
        (10, 32),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (0, 0, 0),
        2
    )

    return canvas


# Process five tilted documents
for number in range(1, 6):

    original_path = os.path.join(
        dataset_dir,
        f"img{number}.jpg"
    )

    corrected_path = os.path.join(
        corrected_dir,
        f"img{number}_corrected.jpg"
    )

    enhanced_path = os.path.join(
        enhanced_dir,
        f"img{number}_enhanced.jpg"
    )

    original = cv2.imread(original_path)
    corrected = cv2.imread(corrected_path)
    enhanced = cv2.imread(enhanced_path)

    if original is None or corrected is None or enhanced is None:
        print("Missing image for document:", number)
        continue

    # Prepare three panels
    panel1 = prepare_panel(original, "Original")
    panel2 = prepare_panel(corrected, "Perspective Corrected")
    panel3 = prepare_panel(enhanced, "Final Enhanced")

    # Combine panels horizontally
    comparison = np.hstack((
        panel1,
        panel2,
        panel3
    ))

    # Save challenge comparison
    output_path = os.path.join(
        output_dir,
        f"img{number}_challenge_comparison.jpg"
    )

    cv2.imwrite(output_path, comparison)

    print("Challenge comparison saved:", output_path)


print("\nFive tilted document comparisons created successfully!")
