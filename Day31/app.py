
import streamlit as st
from ultralytics import YOLO
from PIL import Image
import tempfile
import cv2
import os

st.set_page_config(
    page_title="Construction Equipment Detection",
    page_icon="🚜",
    layout="wide"
)

st.title("🚜 Construction Equipment Detection System")
st.write("Upload an image or video to detect construction equipment using YOLOv8.")

MODEL_PATH = os.path.join(os.path.dirname(__file__), "weights", "best.pt")

@st.cache_resource
def load_model():
    return YOLO(MODEL_PATH)

try:
    model = load_model()
    st.success("YOLO model loaded successfully!")
except Exception as e:
    st.error(f"Model loading error: {e}")
    st.stop()

option = st.sidebar.radio(
    "Select Detection Type",
    ["Image Detection", "Video Detection"]
)

if option == "Image Detection":
    st.header("Image Detection")

    uploaded_file = st.file_uploader(
        "Upload an image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original Image")
            st.image(image, use_container_width=True)

        if st.button("Detect Equipment"):
            with st.spinner("Detecting equipment..."):
                results = model.predict(image, conf=0.25)
                result_image = results[0].plot()
                result_image = cv2.cvtColor(
                    result_image, cv2.COLOR_BGR2RGB
                )

            with col2:
                st.subheader("Detection Result")
                st.image(result_image, use_container_width=True)

            output_image = Image.fromarray(result_image)

            with tempfile.NamedTemporaryFile(
                suffix=".jpg", delete=False
            ) as temp:
                output_path = temp.name
                output_image.save(output_path)

            with open(output_path, "rb") as file:
                st.download_button(
                    "Download Detection Image",
                    data=file,
                    file_name="equipment_detection.jpg",
                    mime="image/jpeg"
                )

            os.remove(output_path)

            detected = results[0].boxes
            st.subheader("Detection Summary")
            st.write(f"Total objects detected: {len(detected)}")

            for box in detected:
                class_id = int(box.cls[0])
                confidence = float(box.conf[0])
                class_name = model.names[class_id]
                st.write(
                    f"- {class_name}: {confidence * 100:.2f}% confidence"
                )

elif option == "Video Detection":
    st.header("Video Detection")

    uploaded_video = st.file_uploader(
        "Upload a video",
        type=["mp4", "avi", "mov"]
    )

    if uploaded_video:
        if st.button("Detect Objects in Video"):
            with tempfile.NamedTemporaryFile(
                suffix=".mp4", delete=False
            ) as input_temp:
                input_temp.write(uploaded_video.read())
                input_path = input_temp.name

            cap = cv2.VideoCapture(input_path)

            fps = cap.get(cv2.CAP_PROP_FPS)
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

            if fps <= 0:
                fps = 25

            with tempfile.NamedTemporaryFile(
                suffix=".mp4", delete=False
            ) as output_temp:
                output_path = output_temp.name

            writer = cv2.VideoWriter(
                output_path,
                cv2.VideoWriter_fourcc(*"mp4v"),
                fps,
                (width, height)
            )

            progress = st.progress(0)
            status = st.empty()

            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            frame_number = 0

            while cap.isOpened():
                ret, frame = cap.read()

                if not ret:
                    break

                result = model.predict(frame, conf=0.25, verbose=False)
                annotated_frame = result[0].plot()
                writer.write(annotated_frame)

                frame_number += 1

                if total_frames > 0:
                    progress.progress(
                        min(frame_number / total_frames, 1.0)
                    )

                status.write(f"Processing frame {frame_number}...")

            cap.release()
            writer.release()

            st.success("Video detection completed!")

            st.video(output_path)

            with open(output_path, "rb") as file:
                st.download_button(
                    "Download Detected Video",
                    data=file,
                    file_name="equipment_detection.mp4",
                    mime="video/mp4"
                )

            os.remove(input_path)
