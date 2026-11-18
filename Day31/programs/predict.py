from ultralytics import YOLO

def main():
    model = YOLO("weights/best.pt")

    model.predict(
        source="sample_images",
        conf=0.25,
        imgsz=640,
        save=True,
        project="predictions",
        name="test_predictions"
    )

if __name__ == "__main__":
    main()
