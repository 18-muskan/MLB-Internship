from ultralytics import YOLO

def main():
    model = YOLO("yolov8n.pt")

    model.train(
        data="data.yaml",
        epochs=10,
        imgsz=640,
        batch=8,
        device=0,
        workers=2,
        patience=3,
        project="results",
        name="equipment_yolov8"
    )

if __name__ == "__main__":
    main()
