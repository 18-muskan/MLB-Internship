
import os
from ultralytics import YOLO

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "weights", "yolo11n.pt")
INPUT_DIR = os.path.join(BASE_DIR, "sample_videos")
OUTPUT_DIR = os.path.join(BASE_DIR, "output_videos")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def track_videos():

    model = YOLO(MODEL_PATH)

    videos = sorted([
        f for f in os.listdir(INPUT_DIR)
        if f.lower().endswith((".mp4", ".avi", ".mov"))
    ])

    for video in videos:

        video_path = os.path.join(INPUT_DIR, video)
        video_name = os.path.splitext(video)[0]

        print(f"\nProcessing with ByteTrack: {video}")

        results = model.track(
            source=video_path,
            tracker="bytetrack.yaml",
            persist=False,
            conf=0.25,
            iou=0.5,
            imgsz=640,
            device="cpu",
            save=True,
            project=OUTPUT_DIR,
            name=f"{video_name}_tracking",
            exist_ok=True,
            stream=True,
            verbose=False
        )

        unique_ids = set()

        for result in results:
            if result.boxes is not None and result.boxes.id is not None:
                ids = result.boxes.id.cpu().numpy().astype(int)
                unique_ids.update(ids.tolist())

        print("Unique tracking IDs:", len(unique_ids))

    print("\nAll videos processed using ByteTrack!")

if __name__ == "__main__":
    track_videos()
