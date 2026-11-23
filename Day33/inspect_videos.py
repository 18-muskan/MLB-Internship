
import cv2
import os
from pathlib import Path

# Project directory
BASE_DIR = Path(__file__).resolve().parent
VIDEO_DIR = BASE_DIR / "sample_videos"

# Supported video formats
extensions = [
    ".mp4", ".avi", ".mov",
    ".mkv", ".webm", ".mpeg"
]

print("\n====================================")
print("       DAY 33 VIDEO INSPECTOR")
print("====================================")

if not VIDEO_DIR.exists():
    print("Sample videos folder not found!")

else:

    videos = [
        file for file in VIDEO_DIR.rglob("*")
        if file.is_file()
        and file.suffix.lower() in extensions
    ]

    if not videos:
        print("No video files found!")
    
    else:
        print(f"\nTotal Videos Found: {len(videos)}")

        for index, video in enumerate(videos, start=1):

            cap = cv2.VideoCapture(str(video))

            if not cap.isOpened():
                print(f"\n{index}. Cannot open: {video.name}")
                continue

            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

            fps = cap.get(cv2.CAP_PROP_FPS)

            frames = int(
                cap.get(cv2.CAP_PROP_FRAME_COUNT)
            )

            duration = frames / fps if fps > 0 else 0

            size_mb = video.stat().st_size / (1024 * 1024)

            print("\n------------------------------------")
            print(f"Video Number : {index}")
            print(f"Original Name: {video.name}")
            print(f"Folder       : {video.parent}")
            print(f"Format       : {video.suffix}")
            print(f"Resolution   : {width} x {height}")
            print(f"FPS          : {fps:.2f}")
            print(f"Total Frames : {frames}")
            print(f"Duration     : {duration:.2f} seconds")
            print(f"File Size    : {size_mb:.2f} MB")

            cap.release()

        print("\n====================================")
        print("       INSPECTION COMPLETED")
        print("====================================")
