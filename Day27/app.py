
import streamlit as st
import cv2
import tempfile
import os

st.set_page_config(
    page_title="Day27 Video Processing App",
    page_icon="🎥",
    layout="wide"
)

st.title("🎥 Video Processing App")
st.write("Upload a video and apply OpenCV processing techniques.")

uploaded_file = st.file_uploader(
    "Upload your video",
    type=["mp4", "avi", "mov"]
)

effect = st.selectbox(
    "Select Processing Technique",
    ["Grayscale", "Gaussian Blur", "Canny Edge Detection"]
)

if uploaded_file is not None:

    st.subheader("Original Video")
    st.video(uploaded_file)

    if st.button("Process Video"):

        input_path = None
        output_path = None
        cap = None
        writer = None

        try:
            with tempfile.NamedTemporaryFile(
                delete=False, suffix=".mp4"
            ) as temp_input:
                temp_input.write(uploaded_file.getvalue())
                input_path = temp_input.name

            output_file = tempfile.NamedTemporaryFile(
                delete=False, suffix=".mp4"
            )
            output_path = output_file.name
            output_file.close()

            cap = cv2.VideoCapture(input_path)

            if not cap.isOpened():
                st.error("Unable to read uploaded video.")
                st.stop()

            fps = cap.get(cv2.CAP_PROP_FPS)
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

            if fps <= 0:
                fps = 25

            writer = cv2.VideoWriter(
                output_path,
                cv2.VideoWriter_fourcc(*"mp4v"),
                fps,
                (width, height)
            )

            if not writer.isOpened():
                st.error("Video writer could not start.")
                st.stop()

            progress = st.progress(0)
            status = st.empty()
            frame_count = 0

            while True:
                ret, frame = cap.read()

                if not ret:
                    break

                if effect == "Grayscale":
                    gray = cv2.cvtColor(
                        frame, cv2.COLOR_BGR2GRAY
                    )
                    processed = cv2.cvtColor(
                        gray, cv2.COLOR_GRAY2BGR
                    )

                elif effect == "Gaussian Blur":
                    processed = cv2.GaussianBlur(
                        frame, (5, 5), 0
                    )

                else:
                    gray = cv2.cvtColor(
                        frame, cv2.COLOR_BGR2GRAY
                    )
                    blurred = cv2.GaussianBlur(
                        gray, (5, 5), 0
                    )
                    edges = cv2.Canny(blurred, 50, 150)
                    processed = cv2.cvtColor(
                        edges, cv2.COLOR_GRAY2BGR
                    )

                writer.write(processed)
                frame_count += 1

                if total_frames > 0:
                    progress.progress(
                        min(frame_count / total_frames, 1.0)
                    )

            cap.release()
            cap = None

            writer.release()
            writer = None

            if frame_count == 0 or not os.path.exists(output_path):
                st.error("No frames were processed.")
            elif os.path.getsize(output_path) == 0:
                st.error("Output video is empty.")
            else:
                with open(output_path, "rb") as file:
                    video_bytes = file.read()

                st.success("Video processed successfully!")

                st.subheader("Processed Video")
                st.video(video_bytes)

                st.download_button(
                    "Download Processed Video",
                    data=video_bytes,
                    file_name="processed_video.mp4",
                    mime="video/mp4"
                )

                st.write("Processing Technique:", effect)
                st.write("Frames Processed:", frame_count)
                st.write("FPS:", round(fps, 2))
                st.write("Resolution:", f"{width} x {height}")

        except Exception as error:
            st.error(f"Processing error: {error}")

        finally:
            if cap is not None:
                cap.release()

            if writer is not None:
                writer.release()

            if input_path and os.path.exists(input_path):
                os.remove(input_path)

            if output_path and os.path.exists(output_path):
                os.remove(output_path)

else:
    st.info("Please upload a video to get started.")