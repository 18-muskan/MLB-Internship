
import cv2
import os

# Create output folder
os.makedirs("output_videos", exist_ok=True)

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Webcam could not be opened.")
    exit()

# Get webcam properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fps = cap.get(cv2.CAP_PROP_FPS)

if fps <= 0:
    fps = 20.0

print("Webcam started successfully!")
print("Width:", width)
print("Height:", height)
print("FPS:", fps)

# Create video writer
output_path = "output_videos/webcam_processed.mp4"

fourcc = cv2.VideoWriter_fourcc(*"mp4v")

writer = cv2.VideoWriter(
    output_path,
    fourcc,
    fps,
    (width, height)
)

if not writer.isOpened():
    print("Error: Could not create output video.")
    cap.release()
    exit()

print("\nPress Q to stop webcam recording.")

while True:

    ret, frame = cap.read()

    if not ret:
        print("Unable to capture frame.")
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(
        gray,
        (5, 5),
        0
    )

    # Apply Canny Edge Detection
    edges = cv2.Canny(
        blurred,
        50,
        150
    )

    # Convert processed frame to BGR
    processed = cv2.cvtColor(
        edges,
        cv2.COLOR_GRAY2BGR
    )

    # Save processed frame
    writer.write(processed)

    # Display original and processed frames
    combined = cv2.hconcat([
        frame,
        processed
    ])

    cv2.imshow("Live Webcam | Edge Detection", combined)

    # Stop when Q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
writer.release()
cv2.destroyAllWindows()

print("\nWebcam recording saved successfully!")
print("Output:", output_path)
