from ultralytics import YOLO
from pathlib import Path

# Get the Day23 folder path
BASE_DIR = Path(__file__).resolve().parent

# Load pretrained YOLOv8 Nano model
model_path = BASE_DIR / "yolov8n.pt"
model = YOLO(str(model_path))

# Input and output folders
input_folder = BASE_DIR / "sample_images"
output_folder = BASE_DIR / "output_images"

# Run object detection on all images
results = model.predict(
    source=str(input_folder),
    save=True,
    project=str(output_folder),
    name="detected_images",
    exist_ok=True,
    conf=0.25,
    device="cpu"
)

# Display detection details
print("\nOBJECT DETECTION RESULTS")

for result in results:
    print("\nImage:", Path(result.path).name)

    if result.boxes is not None and len(result.boxes) > 0:
        for box in result.boxes:
            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            confidence = float(box.conf[0])
            coordinates = box.xyxy[0].tolist()

            print("Object:", class_name)
            print("Confidence:", round(confidence, 2))
            print("Bounding Box:", coordinates)
    else:
        print("No objects detected.")

print("\nDetection completed successfully!")
print("Results saved in:", output_folder / "detected_images")