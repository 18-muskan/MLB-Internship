import streamlit as st
from ultralytics import YOLO
from PIL import Image
from collections import Counter
from pathlib import Path
import numpy as np
import pandas as pd
import tempfile
import cv2
import os
import time

# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------
st.set_page_config(
    page_title="ConstructAI | Equipment Intelligence",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

MODEL_PATH = Path(__file__).parent / "weights" / "best.pt"

# -------------------------------------------------
# PROFESSIONAL STYLING
# -------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}
.stApp {
    background: linear-gradient(135deg, #0b1220 0%, #111c2e 55%, #101827 100%);
    color: #edf2f7;
}
[data-testid="stSidebar"] {
    background: #101a2a;
    border-right: 1px solid #26364d;
}
.hero {
    padding: 28px 30px;
    border-radius: 18px;
    background: linear-gradient(110deg, #172a42, #203d56);
    border: 1px solid #34516b;
    margin-bottom: 22px;
}
.hero h1 {
    font-size: 32px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 7px;
}
.hero p {
    color: #bdcddd;
    font-size: 14px;
    margin-bottom: 0;
}
.metric-card {
    background: #172438;
    border: 1px solid #2b4059;
    border-radius: 14px;
    padding: 18px;
    min-height: 112px;
}
.metric-label {
    color: #9fb2c8;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 1px;
}
.metric-value {
    color: #ffffff;
    font-size: 27px;
    font-weight: 800;
    margin-top: 8px;
}
.section-title {
    font-size: 20px;
    font-weight: 700;
    color: #f1f5f9;
    margin: 16px 0 12px 0;
}
.info-panel {
    background: #172438;
    border: 1px solid #2b4059;
    border-radius: 13px;
    padding: 17px;
}
div.stButton > button {
    border-radius: 9px;
    font-weight: 600;
}
.stDownloadButton > button {
    border-radius: 9px;
    font-weight: 600;
}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# MODEL
# -------------------------------------------------
@st.cache_resource
def load_model():
    return YOLO(str(MODEL_PATH))

if not MODEL_PATH.exists():
    st.error("Model weights not found. Expected: weights/best.pt")
    st.stop()

try:
    model = load_model()
except Exception as error:
    st.error(f"Unable to load YOLO model: {error}")
    st.stop()

class_names = model.names
if isinstance(class_names, dict):
    class_options = [class_names[i] for i in sorted(class_names)]
else:
    class_options = list(class_names)

# -------------------------------------------------
# HELPERS
# -------------------------------------------------
def metric_card(label, value):
    st.markdown(
        f"""<div class="metric-card">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
        </div>""",
        unsafe_allow_html=True
    )

def run_prediction(source, confidence, iou, selected_classes):
    class_ids = [
        class_id for class_id, name in class_names.items()
        if name in selected_classes
    ] if selected_classes else None

    return model.predict(
        source=source,
        conf=confidence,
        iou=iou,
        classes=class_ids,
        imgsz=640,
        verbose=False
    )

def extract_detection_data(result):
    rows = []
    if result.boxes is None:
        return rows

    for box in result.boxes:
        class_id = int(box.cls[0].item())
        confidence = float(box.conf[0].item())
        rows.append({
            "Equipment": class_names[class_id],
            "Confidence": round(confidence * 100, 2)
        })
    return rows

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
with st.sidebar:
    st.markdown("## 🏗️ ConstructAI")
    st.caption("Equipment Intelligence Platform")
    st.divider()

    page = st.radio(
        "NAVIGATION",
        ["Dashboard", "Image Detection", "Video Detection", "Model Insights"],
        label_visibility="visible"
    )

    st.divider()
    st.markdown("### ⚙️ Detection Settings")

    confidence = st.slider(
        "Confidence Threshold",
        min_value=0.10,
        max_value=0.95,
        value=0.35,
        step=0.05,
        help="Higher confidence means stricter predictions."
    )

    iou = st.slider(
        "IoU Threshold",
        min_value=0.10,
        max_value=0.90,
        value=0.45,
        step=0.05,
        help="Controls overlap filtering between bounding boxes."
    )

    selected_classes = st.multiselect(
        "Equipment Classes",
        options=class_options,
        default=class_options,
        help="Choose which equipment categories to detect."
    )

    st.divider()
    st.markdown("**Model Status**")
    st.success("YOLO model loaded")
    st.caption("YOLOv8 Nano · Custom trained")

# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>🏗️ ConstructAI Intelligence</h1>
    <p>AI-powered construction equipment detection, visual analytics
    and real-time inference using a custom-trained YOLOv8 model.</p>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# DASHBOARD
# -------------------------------------------------
if page == "Dashboard":
    st.markdown("## Platform Overview")
    st.write("Analyze construction equipment in images and videos using computer vision.")

    a, b, c, d = st.columns(4)
    with a:
        metric_card("Equipment Classes", "10")
    with b:
        metric_card("Test mAP@50", "88.12%")
    with c:
        metric_card("Test Precision", "87.07%")
    with d:
        metric_card("Test Recall", "84.41%")

    st.markdown('<div class="section-title">Available Capabilities</div>',
                unsafe_allow_html=True)

    x, y = st.columns(2)
    with x:
        st.markdown("""
        <div class="info-panel">
        <h3>📷 Image Intelligence</h3>
        <p>Upload construction site images, detect equipment,
        inspect confidence scores and download annotated results.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="info-panel">
        <h3>📊 Detection Analytics</h3>
        <p>Review detected equipment categories, total objects,
        confidence levels and class-wise statistics.</p>
        </div>
        """, unsafe_allow_html=True)

    with y:
        st.markdown("""
        <div class="info-panel">
        <h3>🎬 Video Intelligence</h3>
        <p>Process video frames, visualize bounding boxes
        and export the annotated video.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="info-panel">
        <h3>🎛️ Custom Controls</h3>
        <p>Adjust confidence, IoU and equipment class filters
        to customize model predictions.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Supported Equipment</div>',
                unsafe_allow_html=True)
    st.write(" · ".join(class_options))

    st.info("Choose Image Detection or Video Detection from the sidebar to begin.")

# -------------------------------------------------
# IMAGE DETECTION
# -------------------------------------------------
elif page == "Image Detection":
    st.markdown("## 📷 Image Detection")
    st.write("Upload an image to identify construction equipment.")

    uploaded = st.file_uploader(
        "Upload construction site image",
        type=["jpg", "jpeg", "png", "webp"],
        key="image_upload"
    )

    if uploaded:
        image = Image.open(uploaded).convert("RGB")

        left, right = st.columns(2)
        with left:
            st.markdown("**Original Image**")
            st.image(image, use_container_width=True)

        with right:
            st.markdown("**Detection Output**")
            if st.button("🚀 Analyze Image", type="primary", use_container_width=True):
                if not selected_classes:
                    st.warning("Please select at least one equipment class.")
                else:
                    with st.spinner("Analyzing image with YOLO..."):
                        start = time.time()
                        predictions = run_prediction(
                            image, confidence, iou, selected_classes
                        )
                        elapsed = time.time() - start
                        result = predictions[0]
                        annotated = cv2.cvtColor(
                            result.plot(), cv2.COLOR_BGR2RGB
                        )
                        rows = extract_detection_data(result)

                    st.session_state["image_result"] = annotated
                    st.session_state["image_rows"] = rows
                    st.session_state["image_time"] = elapsed

                    st.image(annotated, use_container_width=True)

        if "image_result" in st.session_state:
            annotated = st.session_state["image_result"]
            rows = st.session_state["image_rows"]

            st.divider()
            st.markdown("### Detection Analytics")

            total = len(rows)
            average_conf = (
                np.mean([r["Confidence"] for r in rows]) if rows else 0
            )

            m1, m2, m3 = st.columns(3)
            with m1:
                metric_card("Objects Detected", str(total))
            with m2:
                metric_card("Average Confidence", f"{average_conf:.1f}%")
            with m3:
                metric_card("Inference Time", f"{st.session_state['image_time']:.2f}s")

            if rows:
                df = pd.DataFrame(rows)
                st.dataframe(df, use_container_width=True, hide_index=True)

                counts = Counter(r["Equipment"] for r in rows)
                chart_df = pd.DataFrame(
                    list(counts.items()), columns=["Equipment", "Count"]
                ).set_index("Equipment")
                st.markdown("**Equipment Distribution**")
                st.bar_chart(chart_df)

            else:
                st.warning("No equipment detected. Try lowering the confidence threshold.")

            output_image = Image.fromarray(annotated)
            from io import BytesIO
            buffer = BytesIO()
            output_image.save(buffer, format="PNG")

            st.download_button(
                "⬇️ Download Annotated Image",
                data=buffer.getvalue(),
                file_name="constructai_prediction.png",
                mime="image/png",
                use_container_width=True
            )

# -------------------------------------------------
# VIDEO DETECTION
# -------------------------------------------------
elif page == "Video Detection":
    st.markdown("## 🎬 Video Detection")
    st.write("Upload a video to process frames and identify construction equipment.")

    uploaded_video = st.file_uploader(
        "Upload video",
        type=["mp4", "avi", "mov", "mkv"],
        key="video_upload"
    )

    if uploaded_video:
        st.video(uploaded_video)

        if st.button("▶️ Start Video Analysis", type="primary"):
            if not selected_classes:
                st.warning("Please select at least one equipment class.")
            else:
                input_path = None
                output_path = None
                cap = None

                try:
                    with tempfile.NamedTemporaryFile(
                        delete=False, suffix=".mp4"
                    ) as input_file:
                        input_file.write(uploaded_video.getbuffer())
                        input_path = input_file.name

                    cap = cv2.VideoCapture(input_path)

                    if not cap.isOpened():
                        st.error("Could not open this video. Try an MP4 video.")
                    else:
                        fps = cap.get(cv2.CAP_PROP_FPS)
                        fps = fps if fps and fps > 0 else 25
                        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

                        if frame_count <= 0 or width <= 0 or height <= 0:
                            st.error("Invalid or unsupported video.")
                        else:
                            with tempfile.NamedTemporaryFile(
                                delete=False, suffix=".mp4"
                            ) as output_file:
                                output_path = output_file.name

                            writer = cv2.VideoWriter(
                                output_path,
                                cv2.VideoWriter_fourcc(*"mp4v"),
                                fps,
                                (width, height)
                            )

                            progress = st.progress(0)
                            status = st.empty()
                            all_rows = []
                            processed = 0

                            while True:
                                ret, frame = cap.read()
                                if not ret:
                                    break

                                result = run_prediction(
                                    frame, confidence, iou, selected_classes
                                )[0]

                                annotated_frame = result.plot()
                                writer.write(annotated_frame)
                                all_rows.extend(extract_detection_data(result))

                                processed += 1
                                progress.progress(
                                    min(processed / frame_count, 1.0)
                                )
                                status.write(
                                    f"Processing frame {processed} of {frame_count}"
                                )

                            cap.release()
                            writer.release()

                            st.success(f"Video processing completed: {processed} frames")

                            if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
                                with open(output_path, "rb") as video_file:
                                    video_bytes = video_file.read()

                                st.markdown("### Annotated Video")
                                st.video(video_bytes)

                                st.download_button(
                                    "⬇️ Download Processed Video",
                                    data=video_bytes,
                                    file_name="constructai_annotated_video.mp4",
                                    mime="video/mp4",
                                    use_container_width=True
                                )

                            st.markdown("### Video Analytics")
                            total = len(all_rows)
                            avg = (
                                np.mean([r["Confidence"] for r in all_rows])
                                if all_rows else 0
                            )

                            m1, m2, m3 = st.columns(3)
                            with m1:
                                metric_card("Frames Processed", str(processed))
                            with m2:
                                metric_card("Total Detections", str(total))
                            with m3:
                                metric_card("Average Confidence", f"{avg:.1f}%")

                            if all_rows:
                                df = pd.DataFrame(all_rows)
                                counts = df["Equipment"].value_counts()
                                st.bar_chart(counts)
                                st.dataframe(
                                    df, use_container_width=True, hide_index=True
                                )
                            else:
                                st.warning("No equipment detected in the video.")

                except Exception as error:
                    st.error(f"Video processing error: {error}")

                finally:
                    if cap is not None:
                        cap.release()
                    for path in [input_path, output_path]:
                        if path and os.path.exists(path):
                            try:
                                os.remove(path)
                            except OSError:
                                pass

# -------------------------------------------------
# MODEL INSIGHTS
# -------------------------------------------------
elif page == "Model Insights":
    st.markdown("## 🧠 Model Insights")
    st.write("Technical information and evaluation performance of the custom-trained model.")

    st.markdown("### Model Configuration")
    config1, config2 = st.columns(2)

    with config1:
        st.markdown("""
        <div class="info-panel">
        <b>Architecture</b><br>YOLOv8 Nano<br><br>
        <b>Task</b><br>Object Detection<br><br>
        <b>Input Resolution</b><br>640 × 640<br><br>
        <b>Training Epochs</b><br>10
        </div>
        """, unsafe_allow_html=True)

    with config2:
        st.markdown("""
        <div class="info-panel">
        <b>Dataset</b><br>SODA1 Construction Equipment<br><br>
        <b>Training Images</b><br>7,790<br><br>
        <b>Validation Images</b><br>1,702<br><br>
        <b>Test Images</b><br>494
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### Test Set Performance")
    performance = pd.DataFrame({
        "Metric": ["Precision", "Recall", "mAP@50", "mAP@50-95"],
        "Score": [87.07, 84.41, 88.12, 72.68]
    })

    st.dataframe(performance, use_container_width=True, hide_index=True)
    st.bar_chart(performance.set_index("Metric"))

    st.markdown("### Supported Equipment Categories")
    st.write(", ".join(class_options))

    st.caption(
        "Evaluation values are from the separately evaluated test split. "
        "Actual prediction quality may vary with image quality and scene conditions."
    )

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.divider()
st.caption(
    "ConstructAI | Custom YOLOv8 Construction Equipment Detection | "
    "Computer Vision Project"
)
