
# Day 32 - Object Tracking Using YOLO11

## Project Overview

This project implements real-time object detection and multi-object tracking using the YOLO11n pretrained model.

Two tracking algorithms are implemented and tested:
- ByteTrack
- BoT-SORT

The system processes five sample videos and assigns tracking IDs to detected objects.

## Technologies Used

- Python
- YOLO11n
- Ultralytics
- OpenCV
- ByteTrack
- BoT-SORT
- Streamlit
- Pandas

## Project Structure

```text
Day32/
├── weights/
│   └── yolo11n.pt
├── sample_videos/
├── output_videos/
│   ├── video1_tracking/
│   ├── video2_tracking/
│   ├── video3_tracking/
│   ├── video4_tracking/
│   ├── video5_tracking/
│   └── botsort/
├── screenshots/
├── tracking.py
├── botsort_tracking.py
├── tracker_comparison.csv
├── requirements.txt
├── README.md
└── app.py
```

## Object Tracking

Object tracking identifies objects across consecutive video frames and assigns tracking IDs to them.

Unlike object detection, which detects objects independently in each frame, object tracking attempts to maintain the identity of objects across frames.

## Tracking Algorithms

### ByteTrack

ByteTrack uses both high-confidence and low-confidence detections to associate objects across frames.

### BoT-SORT

BoT-SORT combines object association with motion and camera-motion information to improve tracking in challenging scenes.

## Experimental Results

| Video | ByteTrack IDs | BoT-SORT IDs |
|---|---:|---:|
| Video 1 | 39 | 54 |
| Video 2 | 22 | 23 |
| Video 3 | 67 | 66 |
| Video 4 | 20 | 19 |
| Video 5 | 14 | 15 |

These values represent unique tracking IDs observed during each video. They do not necessarily represent the exact number of distinct physical objects.

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run ByteTrack

```bash
python tracking.py
```

## Run BoT-SORT

```bash
python botsort_tracking.py
```

## Mini Application

The Streamlit application allows users to upload a video, perform object tracking, view tracking IDs and confidence scores, and save the processed video.

Run the application:

```bash
streamlit run app.py
```

## Challenges

- Processing high-resolution 4K videos on CPU.
- Handling objects that become temporarily hidden.
- Maintaining tracking IDs across consecutive frames.
- Differences in tracking IDs between algorithms.

## Conclusion

The project successfully tested YOLO11n with ByteTrack and BoT-SORT on five sample videos. Both algorithms generated tracking IDs and saved processed video outputs for comparison.
