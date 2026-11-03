
from ultralytics import YOLO
from pathlib import Path
from collections import Counter

# Get the Day23 directory
BASE_DIR = Path(__file__).resolve().parent

# Load pretrained YOLOv8 Nano model
model = YOLO(str(BASE_DIR / "yolov8n.pt"))

# New vehicle dataset path
DATASET_DIR = (
    BASE_DIR
    / "dataset"
    / "Vehicle Detection.v2-dataset-with-truck-and-bus.yolov8"
)

# Use test images for inference
dataset_images = DATASET_DIR / "test" / "images"

# Output folder inside Day23
output_folder = BASE_DIR / "output_images"

# Run pretrained model on test images
results = model.predict(
    source=str(dataset_images),
    save=True,
    project=str(output_folder),
    name="vehicle_detection_results",
    exist_ok=True,
    conf=0.25,
    device="cpu",
    classes=[2, 3, 5, 7]
)

# Analyze predictions
total_objects = Counter()

print("\nVEHICLE DETECTION MINI PROJECT")
print("--------------------------------")

for result in results:
    print("\nImage:", Path(result.path).name)

    if result.boxes is not None and len(result.boxes) > 0:
        for box in result.boxes:
            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            confidence = float(box.conf[0])

            total_objects[class_name] += 1

            print(
                "Detected:", class_name,
                "| Confidence:", round(confidence, 2)
            )
    else:
        print("No objects detected.")

# Display overall summary
print("\nOVERALL DETECTION SUMMARY")
print("--------------------------------")

for class_name, count in total_objects.items():
    print(class_name, ":", count)

print("\nTotal detected objects:", sum(total_objects.values()))
print("Total images processed:", len(results))

print(
    "\nResults saved in:",
    output_folder / "vehicle_detection_results"
)
