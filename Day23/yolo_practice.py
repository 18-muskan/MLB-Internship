from ultralytics import YOLO

# Load pretrained YOLOv8 Nano model
model = YOLO("yolov8n.pt")

# Display model information
print("YOLOv8 Nano model loaded successfully!")

# Display available object classes
print("\nAvailable Object Classes:")
print(model.names)