
import cv2
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
VIDEO_DIR = BASE_DIR / "sample_videos"
OUTPUT_DIR = BASE_DIR / "output_images"

OUTPUT_DIR.mkdir(exist_ok=True)

extensions = [".mp4", ".avi", ".mov", ".mkv", ".webm"]

videos = sorted([
    file for file in VIDEO_DIR.iterdir()
    if file.is_file() and file.suffix.lower() in extensions
])

print("Creating video previews...\n")

for index, video in enumerate(videos, start=1):
    cap = cv2.VideoCapture(str(video))

    if not cap.isOpened():
        print(f"Could not open: {video.name}")
        continue

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Capture a frame from the middle of the video
    cap.set(cv2.CAP_PROP_POS_FRAMES, total_frames // 2)

    success, frame = cap.read()

    if success:
        height, width = frame.shape[:2]
        new_width = 900
        new_height = int(height * new_width / width)

        preview = cv2.resize(frame, (new_width, new_height))

        output_path = OUTPUT_DIR / f"video_{index}_preview.jpg"
        cv2.imwrite(str(output_path), preview)

        print(f"Saved: {output_path.name}")

    cap.release()

print("\nAll previews created successfully!")