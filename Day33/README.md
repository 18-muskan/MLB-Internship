# Day 33 – AI-Based People Counting & Crowd Analytics

## Project Overview

This project focuses on developing an AI-based People Counting and Crowd Analytics System using YOLOv8, ByteTrack, OpenCV, and Streamlit.

The system detects people in images and videos, tracks their movement using unique tracking IDs, and calculates the number of people in video frames. It also provides peak occupancy statistics and basic entry and exit estimates.

An interactive Streamlit dashboard allows users to upload images and videos, perform detection and tracking, view analytics, and download processed results.

## Objectives

- Detect people in images and videos using YOLOv8.
- Track multiple people across video frames.
- Assign unique tracking IDs using ByteTrack.
- Count detected people in each frame.
- Calculate peak occupancy in videos.
- Estimate entries and exits using line-crossing logic.
- Build an interactive dashboard for visualizing results.

## Key Features

- **YOLOv8 People Detection:** Detects people using a pretrained YOLOv8 model.
- **ByteTrack Object Tracking:** Tracks detected people across consecutive video frames.
- **Unique Tracking IDs:** Assigns IDs to tracked individuals.
- **Image Detection:** Upload images and detect people with bounding boxes.
- **Video Detection:** Process videos and visualize detected people.
- **People Counting:** Counts the number of detected people in each frame.
- **Peak Occupancy:** Records the maximum number of people detected in a single frame.
- **Entry and Exit Estimation:** Uses a virtual horizontal line to estimate people crossing.
- **Interactive Dashboard:** Provides a Streamlit-based interface.
- **Analytics:** Displays detection statistics and project information.
- **Download Results:** Allows users to download processed images and videos.

## Technologies Used

- Python
- YOLOv8
- Ultralytics
- ByteTrack
- OpenCV
- Streamlit
- NumPy
- Pillow

## How People Counting Works

The project uses YOLOv8 to detect people in images and video frames. The model identifies people and draws bounding boxes around them.

For video processing, ByteTrack tracks detected people across consecutive frames and assigns unique tracking IDs. These IDs help the system identify the same person as they move through the video.

The system counts the people detected in each frame and calculates peak occupancy, which represents the maximum number of people detected at one time.

A basic line-crossing mechanism is also implemented to estimate entries and exits when tracked people cross a predefined horizontal line.

## Difference Between People Detection and People Counting

**People Detection:**

People detection identifies individuals in an image or video frame and marks their positions using bounding boxes. It tells us where people are located.

**People Counting:**

People counting calculates how many people are detected. In video-based counting, object tracking helps follow individuals across frames using unique IDs and reduces repeated counting.

In simple words, detection finds people, while counting calculates their number.

## Dataset and Testing

The project was tested using five sample videos representing different environments:

1. Outdoor Gathering
2. Shopping Mall
3. City Street
4. Pedestrian Traffic
5. Indoor Dining

Different video resolutions, lighting conditions, and crowd densities were used to observe the performance of the detection and tracking system.

## Challenges Faced

During the development and testing of this project, several challenges were encountered:

- **Crowded Scenes:** People standing close together sometimes caused overlapping bounding boxes.
- **Occlusion:** Partially visible people were more difficult to detect.
- **Lighting Conditions:** Different lighting environments affected detection performance.
- **Tracking Stability:** Fast movement and overlapping people sometimes caused tracking IDs to change.
- **Video Resolution:** High-resolution videos required additional processing time and resources.
- **Small and Distant People:** The model sometimes missed people who appeared very small or far away.

## Future Improvements

The project can be improved further by implementing:

- Training a custom YOLO model using a larger and more diverse crowd dataset.
- Improving detection accuracy in highly crowded environments.
- Using advanced tracking algorithms for more stable tracking IDs.
- Implementing more accurate entry and exit counting using virtual counting lines.
- Adding real-time CCTV camera support.
- Developing crowd density estimation.
- Adding overcrowding alerts and notifications.
- Optimizing video processing for faster performance.
- Creating detailed reports and historical crowd analytics.

## Project Structure

```text
Day33/
│
├── app.py
├── people_counting.py
├── inspect_videos.py
├── create_previews.py
├── create_contact_sheet.py
├── rename_videos.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── sample_videos/
│
├── output_videos/
│
├── output_images/
│
└── weights/
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Folder

```bash
cd MLB-Internship/Day33
```

### 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal to access the application.

**Note:** The YOLOv8 model weights are required for detection. The application should download the pretrained model automatically if configured to load `yolov8n.pt` and internet access is available.

## How to Use the Application

1. Run the Streamlit application.
2. Open the Dashboard to explore the project overview.
3. Navigate to Detection Studio.
4. Upload an image or video.
5. Run the detection or tracking process.
6. View bounding boxes, tracking IDs, and people counts.
7. Explore the Analytics page.
8. Download the processed results.

## Applications

This project can be useful in several real-world scenarios:

- Shopping mall crowd monitoring.
- Pedestrian traffic analysis.
- Public space monitoring.
- Event crowd management.
- Smart surveillance systems.
- People flow analysis.

## Learning Outcomes

Through this project, I gained practical experience in:

- Object detection using YOLOv8.
- Multi-object tracking using ByteTrack.
- Video processing with OpenCV.
- People counting and peak occupancy analysis.
- Working with pretrained computer vision models.
- Building interactive AI applications using Streamlit.
- Handling different video formats and resolutions.
- Understanding real-world challenges in crowded environments.

## Author

**Muskan Ejaz**

Machine Learning & Computer Vision  
MLB Internship – Day 33

**Project:** AI-Based People Counting & Crowd Analytics System