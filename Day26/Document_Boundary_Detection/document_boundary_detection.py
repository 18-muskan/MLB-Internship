
import cv2
import os
import glob

# Get project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Input images directory
input_dir = os.path.join(BASE_DIR, "dataset", "input_images")

# Output directories
output_base = os.path.join(BASE_DIR, "output", "document_boundaries")

original_dir = os.path.join(output_base, "original_images")
edge_dir = os.path.join(output_base, "edge_detection")
morph_dir = os.path.join(output_base, "morphological_results")
final_dir = os.path.join(output_base, "final_boundaries")

# Create output directories
for folder in [original_dir, edge_dir, morph_dir, final_dir]:
    os.makedirs(folder, exist_ok=True)

# Get all document images
image_files = []

for extension in ["*.jpg", "*.jpeg", "*.png"]:
    image_files.extend(glob.glob(os.path.join(input_dir, extension)))

image_files.sort()

print("Total images found:", len(image_files))

if len(image_files) == 0:
    print("Error: No document images found!")

else:
    # Create morphological kernel
    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT, (5, 5)
    )

    # Process each document image
    for image_path in image_files:

        filename = os.path.splitext(os.path.basename(image_path))[0]

        print("\nProcessing:", filename)

        # Load original image
        image = cv2.imread(image_path)

        if image is None:
            print("Unable to load:", filename)
            continue

        # 1. Save original image
        original_output = os.path.join(
            original_dir, filename + "_original.jpg"
        )
        cv2.imwrite(original_output, image)

        # 2. Convert image to grayscale
        gray = cv2.cvtColor(
            image, cv2.COLOR_BGR2GRAY
        )

        # Apply Gaussian Blur
        blurred = cv2.GaussianBlur(
            gray, (5, 5), 0
        )

        # 3. Apply Canny Edge Detection
        edges = cv2.Canny(
            blurred, 50, 150
        )

        edge_output = os.path.join(
            edge_dir, filename + "_edges.jpg"
        )
        cv2.imwrite(edge_output, edges)

        # 4. Apply Morphological Closing
        morph = cv2.morphologyEx(
            edges,
            cv2.MORPH_CLOSE,
            kernel,
            iterations=2
        )

        morph_output = os.path.join(
            morph_dir, filename + "_morphology.jpg"
        )
        cv2.imwrite(morph_output, morph)

        # 5. Find external contours
        contours, hierarchy = cv2.findContours(
            morph,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        # Copy original image for drawing
        final_image = image.copy()

        if contours:

            # Find largest contour
            largest_contour = max(
                contours, key=cv2.contourArea
            )

            area = cv2.contourArea(largest_contour)

            # Approximate contour shape
            perimeter = cv2.arcLength(
                largest_contour, True
            )

            approx = cv2.approxPolyDP(
                largest_contour,
                0.02 * perimeter,
                True
            )

            # Draw detected document boundary
            if area > 1000:

                cv2.drawContours(
                    final_image,
                    [approx],
                    -1,
                    (0, 255, 0),
                    3
                )

                print("Document boundary detected!")
                print("Largest contour area:", area)

            else:
                print("No significant document boundary found.")

        else:
            print("No contours detected.")

        # 6. Save final boundary image
        final_output = os.path.join(
            final_dir, filename + "_boundary.jpg"
        )

        cv2.imwrite(final_output, final_image)

        print("All four outputs saved for:", filename)

    print("\n================================")
    print("DOCUMENT PROCESSING COMPLETED!")
    print("Total images processed:", len(image_files))
    print("Original, edge, morphology and final images saved.")
    print("================================")
