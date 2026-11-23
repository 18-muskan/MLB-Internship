
import cv2
from pathlib import Path
from ultralytics import YOLO

BASE_DIR = Path(__file__).resolve().parent

VIDEO_DIR = BASE_DIR / "sample_videos"
OUTPUT_DIR = BASE_DIR / "output_videos"

MODEL_NAME = "yolov8n.pt"
CONFIDENCE = 0.35
MAX_FRAME_SIZE = 960

OUTPUT_DIR.mkdir(exist_ok=True)


def process_video(video_path):

    print("\n" + "=" * 50)
    print(f"PROCESSING: {video_path.name}")
    print("=" * 50)

    # Load a fresh model for each video to reset tracking IDs
    model = YOLO(MODEL_NAME)

    cap = cv2.VideoCapture(str(video_path))

    if not cap.isOpened():
        print("Error: Could not open video!")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps <= 0:
        fps = 25

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    output_path = OUTPUT_DIR / f"{video_path.stem}_counted.mp4"

    writer = None

    frame_number = 0
    peak_occupancy = 0

    previous_positions = {}
    counted_entries = set()
    counted_exits = set()

    entry_count = 0
    exit_count = 0

    while True:

        success, frame = cap.read()

        if not success:
            break

        frame_number += 1

        # Resize large frames to reduce processing time
        height, width = frame.shape[:2]

        scale = min(
            MAX_FRAME_SIZE / width,
            MAX_FRAME_SIZE / height,
            1.0
        )

        if scale < 1:
            frame = cv2.resize(
                frame,
                (int(width * scale), int(height * scale))
            )

        height, width = frame.shape[:2]

        # Detect and track only people (class 0)
        results = model.track(
            frame,
            persist=True,
            classes=[0],
            conf=CONFIDENCE,
            tracker="bytetrack.yaml",
            verbose=False
        )

        result = results[0]

        current_count = len(result.boxes)
        peak_occupancy = max(peak_occupancy, current_count)

        # Initialize output video writer
        if writer is None:

            fourcc = cv2.VideoWriter_fourcc(*"mp4v")

            writer = cv2.VideoWriter(
                str(output_path),
                fourcc,
                fps,
                (width, height)
            )

        # Horizontal counting line
        line_y = int(height * 0.60)

        cv2.line(
            frame,
            (0, line_y),
            (width, line_y),
            (0, 255, 255),
            2
        )

        if result.boxes is not None and len(result.boxes) > 0:

            boxes = result.boxes.xyxy.cpu().numpy()
            confidences = result.boxes.conf.cpu().numpy()

            if result.boxes.id is not None:
                track_ids = result.boxes.id.int().cpu().tolist()
            else:
                track_ids = [None] * len(boxes)

            for box, confidence, track_id in zip(
                boxes, confidences, track_ids
            ):

                x1, y1, x2, y2 = map(int, box)

                center_y = int((y1 + y2) / 2)

                label = (
                    f"Person {track_id}"
                    if track_id is not None
                    else "Person"
                )

                label += f" {confidence:.2f}"

                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    label,
                    (x1, max(y1 - 10, 20)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    2
                )

                # Detect line crossing using tracking IDs
                if track_id is not None:

                    if track_id in previous_positions:

                        previous_y = previous_positions[track_id]

                        # Person crosses downward: entry
                        if (
                            previous_y < line_y
                            and center_y >= line_y
                            and track_id not in counted_entries
                        ):
                            entry_count += 1
                            counted_entries.add(track_id)

                        # Person crosses upward: exit
                        elif (
                            previous_y >= line_y
                            and center_y < line_y
                            and track_id not in counted_exits
                        ):
                            exit_count += 1
                            counted_exits.add(track_id)

                    previous_positions[track_id] = center_y

        # Display people counting information
        cv2.putText(
            frame,
            f"People Count: {current_count}",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )

        cv2.putText(
            frame,
            f"Entries: {entry_count}  Exits: {exit_count}",
            (20, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 255),
            2
        )

        cv2.putText(
            frame,
            f"Peak Occupancy: {peak_occupancy}",
            (20, 105),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        if writer is not None:
            writer.write(frame)

        if frame_number % 50 == 0:
            print(
                f"Progress: {frame_number}/{total_frames} frames | "
                f"People: {current_count} | "
                f"Peak: {peak_occupancy}"
            )

    cap.release()

    if writer is not None:
        writer.release()

    print("\nVIDEO PROCESSING COMPLETED")
    print(f"Output: {output_path}")
    print(f"Peak Occupancy: {peak_occupancy}")
    print(f"Total Entries: {entry_count}")
    print(f"Total Exits: {exit_count}")


def main():

    videos = sorted([
        file for file in VIDEO_DIR.iterdir()
        if file.is_file() and file.suffix.lower() in [
            ".mp4", ".avi", ".mov", ".mkv"
        ]
    ])

    if not videos:
        print("No videos found in sample_videos folder!")
        return

    print("\nDAY 33 - YOLO PEOPLE COUNTING SYSTEM")
    print(f"Total Videos: {len(videos)}")

    for video in videos:
        process_video(video)

    print("\nALL VIDEOS PROCESSED SUCCESSFULLY!")


if __name__ == "__main__":
    main()
