
import cv2
import os

input_folder = "input_videos/working"
output_folder = "output_videos"

os.makedirs(output_folder, exist_ok=True)

videos = ["video1.mp4", "video2.mp4", "video3.mp4"]

for video in videos:

    input_path = os.path.join(input_folder, video)

    cap = cv2.VideoCapture(input_path)

    if not cap.isOpened():
        print("Error opening video:", video)
        continue

    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    print("\nProcessing:", video)
    print("FPS:", round(fps, 2))
    print("Width:", width)
    print("Height:", height)
    print("Total Frames:", total_frames)

    output_path = os.path.join(
        output_folder,
        video.replace(".mp4", "_processed.mp4")
    )

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    writer = cv2.VideoWriter(
        output_path,
        fourcc,
        fps,
        (width, height)
    )

    while True:

        ret, frame = cap.read()

        if not ret:
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

        # Convert edges to BGR for video saving
        processed_frame = cv2.cvtColor(
            edges,
            cv2.COLOR_GRAY2BGR
        )

        # Save processed frame
        writer.write(processed_frame)

        # Display original and processed frames
        combined = cv2.hconcat([
            frame,
            processed_frame
        ])

        cv2.imshow("Original | Canny Processed", combined)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    writer.release()

    cv2.destroyAllWindows()

    print("Processed video saved:", output_path)

print("\nAll videos processed successfully!")

cv2.destroyAllWindows()
