from ultralytics import YOLO

def main():
    model = YOLO("weights/best.pt")

    metrics = model.val(
        data="data.yaml",
        split="test",
        imgsz=640,
        batch=8
    )

    print("Precision:", metrics.box.mp)
    print("Recall:", metrics.box.mr)
    print("mAP50:", metrics.box.map50)
    print("mAP50-95:", metrics.box.map)

if __name__ == "__main__":
    main()
