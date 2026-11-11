
import cv2
import os

input_folder = "input_videos/working"
output_folder = "output_videos"
screenshot_folder = "screenshots"

os.makedirs(screenshot_folder, exist_ok=True)

videos = ["video1.mp4", "video2.mp4", "video3.mp4"]

for video in videos:

    original_path = os.path.join(input_folder, video)

    processed_name = video.replace(
        ".mp4", "_processed.mp4"
    )

    processed_path = os.path.join(
        output_folder, processed_name
    )

    original = cv2.VideoCapture(original_path)
    processed = cv2.VideoCapture(processed_path)

    if not original.isOpened() or not processed.isOpened():
        print("Cannot open:", video)
        original.release()
        processed.release()
        continue

    print("\nComparing:", video)

    count = 0

    while True:

        ret1, frame1 = original.read()
        ret2, frame2 = processed.read()

        if not ret1 or not ret2:
            break

        # Resize both frames
        frame1 = cv2.resize(frame1, (640, 360))
        frame2 = cv2.resize(frame2, (640, 360))

        # Add labels
        cv2.putText(
            frame1, "Original",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            1, (0, 255, 0), 2
        )

        cv2.putText(
            frame2, "Processed",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            1, (0, 255, 0), 2
        )

        combined = cv2.hconcat([frame1, frame2])

        cv2.imshow("Original vs Processed", combined)

        # Save one comparison screenshot
        if count == 30:
            screenshot_path = os.path.join(
                screenshot_folder,
                video.replace(".mp4", "_comparison.jpg")
            )

            cv2.imwrite(screenshot_path, combined)

            print("Screenshot saved:", screenshot_path)

        count += 1

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    original.release()
    processed.release()
    cv2.destroyAllWindows()

    print("Frames compared:", count)

print("\nAll video comparisons completed!")
cv2.destroyAllWindows()
