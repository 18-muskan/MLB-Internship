
from pathlib import Path

VIDEO_DIR = Path(__file__).resolve().parent / "sample_videos"

rename_map = {
    "14696002_1920_1080_50fps.mp4": "outdoor_gathering.mp4",
    "15636097_2160_3840_30fps.mp4": "shopping_mall.mp4",
    "3894943-hd_1920_1080_24fps.mp4": "city_street.mp4",
    "5699532-uhd_3840_2160_24fps.mp4": "pedestrian_traffic.mp4",
    "8869612-uhd_2160_4096_25fps.mp4": "indoor_dining.mp4"
}

for old_name, new_name in rename_map.items():
    old_path = VIDEO_DIR / old_name
    new_path = VIDEO_DIR / new_name

    if old_path.exists():
        if new_path.exists():
            print(f"Already exists: {new_name}")
        else:
            old_path.rename(new_path)
            print(f"Renamed: {old_name} -> {new_name}")
    else:
        print(f"File not found: {old_name}")

print("\nVideo organization completed!")
