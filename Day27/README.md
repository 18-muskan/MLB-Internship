# Day 27 - Video Processing with OpenCV

## Introduction

Today I learned how to process recorded videos and live webcam streams using OpenCV in Python. I worked with video frames and applied different image processing techniques.

## Topics Covered

- Reading videos using OpenCV.
- Capturing individual video frames.
- Understanding FPS (Frames Per Second).
- Extracting video properties (width, height, total frames).
- Converting video frames into grayscale.
- Applying Gaussian Blur.
- Applying Canny Edge Detection.
- Saving processed videos.
- Real-time webcam processing.

## Practical Tasks

1. Loaded three different input videos using OpenCV.
2. Extracted and displayed video frames.
3. Checked FPS, resolution, and total frame count.
4. Converted frames into grayscale.
5. Applied Gaussian Blur to reduce noise.
6. Used Canny Edge Detection to identify edges.
7. Saved processed videos in MP4 format.
8. Captured and processed live webcam video.
9. Compared original and processed video frames.

## Video Comparison Results

| Video | Original Duration | Processed Duration |
|---|---|---|
| Video 1 | 10.01 seconds | 10.01 seconds |
| Video 2 | 9.11 seconds | 9.11 seconds |
| Video 3 | 82.38 seconds | 30 seconds |

### Observations

- Video 1: Edge detection highlighted the boundaries of objects and moving subjects.
- Video 2: Canny detected object boundaries and details in the video frames.
- Video 3: The video was trimmed to 30 seconds and processed successfully. Edge detection highlighted natural shapes and textures.

## Webcam Processing

I also developed a real-time webcam processing program that captures live video, applies grayscale conversion, Gaussian Blur and Canny Edge Detection, and saves the processed recording.

Webcam Resolution: 640 × 480

Webcam FPS: 30

## What is FPS?

FPS means Frames Per Second. It tells us how many individual frames are displayed in one second of a video.

For example, 30 FPS means the video displays 30 frames every second.

## Challenges Faced

- Processing high-resolution videos was time-consuming.
- Reduced video resolution to improve processing speed.
- Trimmed the third video to 30 seconds.
- Faced video writing warnings during comparison, so I used side-by-side frame display and saved comparison screenshots instead.

## Tools and Technologies

- Python
- OpenCV
- NumPy
- VS Code

## Project Structure

- input_videos: Original and optimized input videos.
- output_videos: Processed videos and webcam recording.
- programs: Python scripts.
- screenshots: Video comparison screenshots.
- sample_images: Example images.

## Conclusion

Successfully completed video processing using OpenCV. Learned how to read videos, process individual frames, apply image processing techniques, capture webcam footage, and save processed video outputs.