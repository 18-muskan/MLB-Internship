
import cv2
import os

input_folder = "input_videos"
output_folder = "input_videos/working"

os.makedirs(output_folder, exist_ok=True)

videos = ["video1.mp4", "video2.mp4", "video3.mp4"]

for video in videos:

    input_path = os.path.join(input_folder, video)
    output_path = os.path.join(output_folder, video)

    cap = cv2.VideoCapture(input_path)

    if not cap.isOpened():
        print("Cannot open:", video)
        continue

    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Process maximum 30 seconds
    max_frames = int(fps * 30)
    frames_to_process = min(total_frames, max_frames)

    width = 1280
    height = 720

    # Keep original aspect ratio
    original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    scale = min(width / original_width, height / original_height)

    new_width = int(original_width * scale)
    new_height = int(original_height * scale)

    new_width -= new_width % 2
    new_height -= new_height % 2

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    writer = cv2.VideoWriter(
        output_path,
        fourcc,
        fps,
        (new_width, new_height)
    )

    count = 0

    while count < frames_to_process:

        ret, frame = cap.read()

        if not ret:
            break

        resized_frame = cv2.resize(
            frame,
            (new_width, new_height)
        )

        writer.write(resized_frame)
        count += 1

    cap.release()
    writer.release()

    print("\nProcessed:", video)
    print("Frames saved:", count)
    print("Duration:", round(count / fps, 2), "seconds")
    print("Resolution:", new_width, "x", new_height)

print("\nAll videos optimized successfully!")
