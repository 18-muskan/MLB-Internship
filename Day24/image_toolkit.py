
import cv2
import os

# Automatically detect Day24 project location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Input and output folders
INPUT_FOLDER = os.path.join(BASE_DIR, "input_images")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "output", "toolkit")

# Create output folder automatically
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Current image
img = None
image_name = ""

print("\nImage Toolkit Started Successfully!")

while True:

    print("\n========== IMAGE TOOLKIT ==========")
    print("1. Load Image")
    print("2. Convert to Grayscale")
    print("3. Resize Image")
    print("4. Rotate Image")
    print("5. Flip Image")
    print("6. Crop Image")
    print("7. Draw Shapes")
    print("8. Add Text")
    print("9. Save Image")
    print("10. Display Image")
    print("11. Exit")

    choice = input("\nEnter your choice (1-11): ").strip()

    # 1. Load Image
    if choice == "1":

        print("\nAvailable Images:")
        print("landscape.jpg")
        print("person.jpg")
        print("vehicle.jpg")
        print("document.jpg")
        print("object.jpg")

        image_name = input("\nEnter image name: ").strip()

        image_path = os.path.join(INPUT_FOLDER, image_name)

        loaded_image = cv2.imread(image_path)

        if loaded_image is None:
            print("ERROR: Image not found!")
            print("Please check:", image_path)
        else:
            img = loaded_image
            print("\nImage loaded successfully!")
            print("Image:", image_name)
            print("Shape:", img.shape)

    # Other operations require loaded image
    elif choice in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:

        if img is None:
            print("\nPlease load an image first using option 1.")
            continue

        # 2. Grayscale
        if choice == "2":

            if len(img.shape) == 3:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                print("Image converted to grayscale!")
            else:
                print("Image is already grayscale.")

        # 3. Resize
        elif choice == "3":

            try:
                width = int(input("Enter new width: "))
                height = int(input("Enter new height: "))

                if width <= 0 or height <= 0:
                    print("Width and height must be greater than zero.")
                else:
                    img = cv2.resize(img, (width, height))
                    print("Image resized successfully!")
                    print("New shape:", img.shape)

            except ValueError:
                print("Please enter valid numbers.")

        # 4. Rotate
        elif choice == "4":

            print("1. 90 degrees clockwise")
            print("2. 180 degrees")
            print("3. 270 degrees clockwise")

            angle = input("Choose rotation: ").strip()

            if angle == "1":
                img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
            elif angle == "2":
                img = cv2.rotate(img, cv2.ROTATE_180)
            elif angle == "3":
                img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
            else:
                print("Invalid rotation choice.")
                continue

            print("Image rotated successfully!")

        # 5. Flip
        elif choice == "5":

            print("1. Horizontal Flip")
            print("2. Vertical Flip")
            print("3. Both Directions")

            flip_choice = input("Choose flip type: ").strip()

            if flip_choice == "1":
                img = cv2.flip(img, 1)
            elif flip_choice == "2":
                img = cv2.flip(img, 0)
            elif flip_choice == "3":
                img = cv2.flip(img, -1)
            else:
                print("Invalid flip choice.")
                continue

            print("Image flipped successfully!")

        # 6. Crop
        elif choice == "6":

            height, width = img.shape[:2]

            cropped = img[
                height // 4:3 * height // 4,
                width // 4:3 * width // 4
            ]

            if cropped.size > 0:
                img = cropped
                print("Center cropping completed!")
                print("New shape:", img.shape)
            else:
                print("Cropping failed.")

        # 7. Draw Shapes
        elif choice == "7":

            height, width = img.shape[:2]

            cv2.rectangle(
                img, (10, 10), (width - 10, height - 10),
                (0, 255, 0), 2
            )

            cv2.circle(
                img, (width // 2, height // 2),
                30, (255, 0, 0), 2
            )

            cv2.line(
                img, (0, 0), (width - 1, height - 1),
                (0, 0, 255), 2
            )

            print("Rectangle, circle and line added!")

        # 8. Add Text
        elif choice == "8":

            text = input("Enter text: ")

            cv2.putText(
                img,
                text,
                (10, img.shape[0] - 15),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (255, 255, 255),
                1
            )

            print("Text added successfully!")

        # 9. Save Image
        elif choice == "9":

            save_name = input(
                "Enter filename (example: document_gray.jpg): "
            ).strip()

            # Add JPG extension if missing
            if not save_name.lower().endswith((".jpg", ".jpeg", ".png")):
                save_name += ".jpg"

            # Keep filename inside toolkit output folder
            save_name = os.path.basename(save_name)

            output_path = os.path.join(OUTPUT_FOLDER, save_name)

            try:
                success = cv2.imwrite(output_path, img)

                if success and os.path.exists(output_path):
                    print("\nIMAGE SAVED SUCCESSFULLY!")
                    print("File:", save_name)
                    print("Full Location:", output_path)
                    print("File Size:", os.path.getsize(output_path), "bytes")
                else:
                    print("ERROR: Image could not be saved.")

            except Exception as error:
                print("Saving Error:", error)

        # 10. Display Image
        elif choice == "10":

            cv2.imshow("Image Toolkit", img)
            print("Press any key in the image window to close.")
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    # 11. Exit
    elif choice == "11":

        print("\nThank you for using Image Toolkit!")
        break

    else:
        print("Invalid choice! Enter a number from 1 to 11.")
