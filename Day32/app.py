
import os
import cv2
import uuid
import tempfile
import streamlit as st
import pandas as pd
from datetime import datetime
from ultralytics import YOLO

# ---------------------------------------
# PROJECT CONFIGURATION
# ---------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR, "weights", "yolo11n.pt"
)

OUTPUT_DIR = os.path.join(
    BASE_DIR, "output_videos", "app_runs"
)

os.makedirs(OUTPUT_DIR, exist_ok=True)

st.set_page_config(
    page_title="VisionTrack AI",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------
# PROFESSIONAL UI STYLING
# ---------------------------------------

st.markdown("""
<style>

.stApp {
    background: #0b1120;
    color: #e5e7eb;
}

[data-testid="stSidebar"] {
    background: #111827;
    border-right: 1px solid #263449;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}

h1, h2, h3 {
    color: #f8fafc !important;
}

p, label {
    color: #cbd5e1;
}

.hero {
    background: linear-gradient(
        120deg, #132b40, #123b43, #142b45
    );
    border: 1px solid #285264;
    border-radius: 18px;
    padding: 28px;
    margin-bottom: 25px;
}

.hero-title {
    font-size: 32px;
    font-weight: 750;
    color: #f8fafc;
    margin-bottom: 8px;
}

.hero-subtitle {
    color: #b4c8d8;
    font-size: 14px;
}

.status-pill {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 20px;
    background: #123d35;
    color: #6ee7b7;
    font-size: 12px;
    font-weight: 700;
}

.section-label {
    color: #5eead4;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1.5px;
    margin-bottom: 8px;
}

div[data-testid="stMetric"] {
    background: #151f30;
    border: 1px solid #28364b;
    padding: 18px;
    border-radius: 14px;
}

div[data-testid="stMetricValue"] {
    color: #5eead4;
}

div[data-testid="stMetricLabel"] {
    color: #aebed0;
}

.stButton > button {
    background: linear-gradient(90deg, #0d9488, #0f766e);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: 700;
    width: 100%;
}

.stButton > button:hover {
    background: #14b8a6;
    color: white;
}

.stDownloadButton > button {
    background: #1d3553;
    color: white;
    border: 1px solid #3b607f;
    border-radius: 10px;
    width: 100%;
}

div[data-testid="stFileUploader"] {
    background: #131f30;
    border: 1px dashed #456078;
    border-radius: 14px;
    padding: 15px;
}

hr {
    border-color: #263449;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------
# MODEL LOADING
# ---------------------------------------

@st.cache_resource
def load_model():

    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Model weights not found: {MODEL_PATH}"
        )

    return YOLO(MODEL_PATH)


# ---------------------------------------
# SIDEBAR
# ---------------------------------------

with st.sidebar:

    st.markdown("## 🎯 VisionTrack AI")
    st.caption("Computer Vision Analytics Platform")

    st.divider()

    st.markdown("### Tracking Configuration")

    tracker_name = st.selectbox(
        "Tracking Algorithm",
        ["ByteTrack", "BoT-SORT"]
    )

    confidence = st.slider(
        "Detection Confidence",
        min_value=0.10,
        max_value=0.90,
        value=0.25,
        step=0.05
    )

    image_size = st.select_slider(
        "Inference Image Size",
        options=[320, 480, 640, 960],
        value=640
    )

    st.divider()

    st.markdown("### Model Information")

    st.markdown("""
    **Architecture:** YOLO11n

    **Task:** Object Detection

    **Classes:** 80 COCO classes

    **Device:** CPU

    **Framework:** Ultralytics
    """)

    st.divider()

    st.caption("VISIONTRACK AI | DAY 32 PROJECT")


# ---------------------------------------
# HEADER
# ---------------------------------------

st.markdown("""
<div class="hero">

    <div style="display:flex; justify-content:space-between;
                align-items:center; flex-wrap:wrap; gap:10px;">

        <div>
            <div class="hero-title">
                Intelligent Object Tracking
            </div>

            <div class="hero-subtitle">
                Detect, identify and track multiple objects
                across video frames using advanced AI.
            </div>
        </div>

        <div class="status-pill">
            ● SYSTEM READY
        </div>

    </div>

</div>
""", unsafe_allow_html=True)

# ---------------------------------------
# MODEL STATUS
# ---------------------------------------

col1, col2, col3 = st.columns(3)

col1.metric("Detection Model", "YOLO11n")
col2.metric("Tracking Algorithms", "02")
col3.metric("Available Classes", "80")

st.divider()

# ---------------------------------------
# VIDEO UPLOAD
# ---------------------------------------

st.markdown(
    '<div class="section-label">01 / INPUT SOURCE</div>',
    unsafe_allow_html=True
)

st.subheader("Upload Video")

uploaded_file = st.file_uploader(
    "Choose a video file",
    type=["mp4", "avi", "mov"],
    help="Upload a video for object detection and tracking."
)

if uploaded_file:

    st.success(
        f"Video uploaded: {uploaded_file.name}"
    )

    with st.expander("Preview Input Video", expanded=True):
        st.video(uploaded_file)

# ---------------------------------------
# TRACKING EXECUTION
# ---------------------------------------

if uploaded_file:

    st.divider()

    st.markdown(
        '<div class="section-label">02 / AI PROCESSING</div>',
        unsafe_allow_html=True
    )

    st.subheader("Start Tracking Analysis")

    st.write(
        f"Selected algorithm: **{tracker_name}**"
    )

    if st.button(
        "🚀  Start Object Tracking",
        use_container_width=True
    ):

        tracker_config = (
            "bytetrack.yaml"
            if tracker_name == "ByteTrack"
            else "botsort.yaml"
        )

        input_path = None
        writer = None
        cap = None

        output_path = os.path.join(
            OUTPUT_DIR,
            f"tracked_{uuid.uuid4().hex[:8]}.mp4"
        )

        try:

            # Save uploaded video temporarily
            suffix = os.path.splitext(
                uploaded_file.name
            )[1].lower()

            if suffix not in [".mp4", ".avi", ".mov"]:
                suffix = ".mp4"

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=suffix
            ) as temp_file:

                temp_file.write(
                    uploaded_file.getbuffer()
                )

                input_path = temp_file.name

            # Load YOLO model
            with st.spinner("Loading YOLO11n model..."):
                model = load_model()

            cap = cv2.VideoCapture(input_path)

            fps = cap.get(cv2.CAP_PROP_FPS)

            width = int(
                cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            )

            height = int(
                cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            )

            total_frames = int(
                cap.get(cv2.CAP_PROP_FRAME_COUNT)
            )

            if (
                not cap.isOpened()
                or fps <= 0
                or width <= 0
                or height <= 0
            ):
                raise ValueError(
                    "Unable to read the uploaded video."
                )

            writer = cv2.VideoWriter(
                output_path,
                cv2.VideoWriter_fourcc(*"mp4v"),
                fps,
                (width, height)
            )

            if not writer.isOpened():
                raise RuntimeError(
                    "Unable to create output video."
                )

            unique_ids = set()
            confidence_scores = []
            class_counts = {}

            frame_count = 0
            total_detections = 0

            progress = st.progress(0)
            status = st.empty()

            # Process each frame
            while cap.isOpened():

                ret, frame = cap.read()

                if not ret:
                    break

                results = model.track(
                    frame,
                    persist=True,
                    tracker=tracker_config,
                    conf=confidence,
                    imgsz=image_size,
                    device="cpu",
                    verbose=False
                )

                result = results[0]

                if result.boxes is not None:

                    boxes = result.boxes

                    if boxes.id is not None:

                        ids = (
                            boxes.id.cpu()
                            .numpy()
                            .astype(int)
                        )

                        unique_ids.update(ids.tolist())

                    if boxes.conf is not None:

                        scores = (
                            boxes.conf.cpu()
                            .numpy()
                            .tolist()
                        )

                        confidence_scores.extend(scores)

                    if boxes.cls is not None:

                        classes = (
                            boxes.cls.cpu()
                            .numpy()
                            .astype(int)
                        )

                        total_detections += len(classes)

                        for class_id in classes:

                            class_name = model.names[
                                int(class_id)
                            ]

                            class_counts[class_name] = (
                                class_counts.get(
                                    class_name, 0
                                ) + 1
                            )

                annotated_frame = result.plot()

                writer.write(annotated_frame)

                frame_count += 1

                if total_frames > 0:

                    progress.progress(
                        min(
                            frame_count / total_frames,
                            1.0
                        )
                    )

                status.write(
                    f"Processing frame {frame_count} "
                    f"of {total_frames}..."
                )

            cap.release()
            cap = None

            writer.release()
            writer = None

            progress.progress(1.0)

            status.success(
                "Object tracking completed successfully!"
            )

            # ---------------------------------------
            # RESULTS
            # ---------------------------------------

            average_confidence = (
                sum(confidence_scores)
                / len(confidence_scores)
                if confidence_scores else 0
            )

            st.session_state["tracking_result"] = {
                "output_path": output_path,
                "tracker": tracker_name,
                "unique_ids": sorted(unique_ids),
                "frames": frame_count,
                "detections": total_detections,
                "average_confidence": average_confidence,
                "class_counts": class_counts
            }

        except Exception as error:

            if cap is not None:
                cap.release()

            if writer is not None:
                writer.release()

            if os.path.exists(output_path):
                os.remove(output_path)

            st.error(
                f"Tracking failed: {error}"
            )

        finally:

            if input_path and os.path.exists(input_path):
                os.remove(input_path)


# ---------------------------------------
# ANALYTICS AND OUTPUT
# ---------------------------------------

if "tracking_result" in st.session_state:

    data = st.session_state["tracking_result"]

    if os.path.exists(data["output_path"]):

        st.divider()

        st.markdown(
            '<div class="section-label">03 / ANALYTICS</div>',
            unsafe_allow_html=True
        )

        st.subheader("Tracking Performance")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Unique Track IDs",
            len(data["unique_ids"])
        )

        c2.metric(
            "Processed Frames",
            data["frames"]
        )

        c3.metric(
            "Total Detections",
            data["detections"]
        )

        c4.metric(
            "Average Confidence",
            f"{data['average_confidence']:.1%}"
        )

        st.caption(
            "Average confidence is calculated across all "
            "detected bounding boxes."
        )

        # Class analytics
        if data["class_counts"]:

            st.subheader("Detected Object Classes")

            class_df = pd.DataFrame(
                list(data["class_counts"].items()),
                columns=["Object Class", "Detections"]
            ).sort_values(
                "Detections",
                ascending=False
            )

            st.dataframe(
                class_df,
                use_container_width=True,
                hide_index=True
            )

        # Tracking IDs
        with st.expander("View Tracking IDs"):

            st.write(data["unique_ids"])

        # ---------------------------------------
        # VIDEO OUTPUT
        # ---------------------------------------

        st.divider()

        st.markdown(
            '<div class="section-label">04 / OUTPUT</div>',
            unsafe_allow_html=True
        )

        st.subheader("Processed Tracking Video")

        st.video(data["output_path"])

        with open(data["output_path"], "rb") as file:

            video_bytes = file.read()

        st.download_button(
            label="⬇ Download Processed Video",
            data=video_bytes,
            file_name="visiontrack_output.mp4",
            mime="video/mp4",
            use_container_width=True
        )

        st.caption(
            f"Saved locally: {data['output_path']}"
        )

# ---------------------------------------
# FOOTER
# ---------------------------------------

st.divider()

st.markdown("""
<div style="text-align:center; padding:15px;">

    <div style="color:#5eead4; font-weight:700;">
        VISIONTRACK AI
    </div>

    <div style="color:#8292a8; font-size:12px;">
        Intelligent Computer Vision & Multi-Object Tracking
    </div>

    <div style="color:#64748b; font-size:11px; margin-top:8px;">
        Powered by YOLO11n · Ultralytics · OpenCV · Streamlit
    </div>

</div>
""", unsafe_allow_html=True)
