
import streamlit as st
import cv2
import numpy as np
import tempfile
import os
from pathlib import Path
from PIL import Image
from ultralytics import YOLO


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="VisionCount AI | People Analytics",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================
# CUSTOM PREMIUM UI DESIGN
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(ellipse at 10% 5%, rgba(111, 66, 193, 0.22), transparent 35%),
        radial-gradient(ellipse at 90% 20%, rgba(0, 180, 216, 0.13), transparent 35%),
        linear-gradient(135deg, #080B18 0%, #101329 50%, #090D1D 100%);
    color: #F4F5FF;
}

/* Hide default Streamlit header */
header[data-testid="stHeader"] {
    background: transparent;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #11152B, #0B1020);
    border-right: 1px solid rgba(160, 140, 255, 0.18);
}

/* Main container */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}

/* Main title */
.hero-title {
    font-size: clamp(2.3rem, 5vw, 4rem);
    font-weight: 900;
    letter-spacing: -2px;
    line-height: 1.1;
    background: linear-gradient(90deg, #FFFFFF, #B9A5FF, #67E8F9);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: fadeIn 1.2s ease;
}

.hero-subtitle {
    color: #A5AAC6;
    font-size: 1rem;
    margin-top: 12px;
}

/* Gradient text */
.gradient-text {
    background: linear-gradient(90deg, #A78BFA, #67E8F9);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Glass cards */
.glass-card {
    background: linear-gradient(
        145deg,
        rgba(255,255,255,0.09),
        rgba(255,255,255,0.025)
    );
    border: 1px solid rgba(190, 180, 255, 0.18);
    border-radius: 20px;
    padding: 24px;
    box-shadow: 0 15px 45px rgba(0,0,0,0.25);
    backdrop-filter: blur(18px);
    transition: all 0.35s ease;
    transform-style: preserve-3d;
}

.glass-card:hover {
    transform: translateY(-7px) rotateX(2deg);
    border-color: rgba(167, 139, 250, 0.65);
    box-shadow: 0 20px 55px rgba(105, 75, 220, 0.20);
}

.metric-label {
    color: #A5AAC6;
    font-size: 0.85rem;
    font-weight: 600;
}

.metric-value {
    font-size: 2.2rem;
    font-weight: 800;
    color: #FFFFFF;
    margin-top: 8px;
}

.metric-icon {
    font-size: 1.7rem;
    margin-bottom: 12px;
}

/* Section heading */
.section-title {
    color: #FFFFFF;
    font-size: 1.45rem;
    font-weight: 800;
    margin: 22px 0 14px 0;
}

/* Buttons */
.stButton > button,
.stDownloadButton > button {
    background: linear-gradient(100deg, #7957E8, #377DEB);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.65rem 1.2rem;
    font-weight: 700;
    transition: all 0.3s ease;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(111, 91, 220, 0.4);
    border: none;
}

/* Upload area */
[data-testid="stFileUploader"] {
    background: rgba(120, 100, 200, 0.07);
    border: 1px dashed rgba(167, 139, 250, 0.55);
    border-radius: 16px;
    padding: 14px;
}

/* Inputs */
.stSlider, [data-testid="stSelectbox"] {
    color: #FFFFFF;
}

/* Sidebar brand */
.brand-box {
    padding: 16px 8px 25px 8px;
    border-bottom: 1px solid rgba(255,255,255,0.10);
    margin-bottom: 20px;
}

.brand-name {
    font-size: 1.45rem;
    font-weight: 900;
    background: linear-gradient(90deg, #B9A5FF, #67E8F9);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.brand-caption {
    color: #8992B5;
    font-size: 0.72rem;
    letter-spacing: 2px;
}

/* Status pill */
.status-pill {
    display: inline-block;
    color: #86EFAC;
    background: rgba(34, 197, 94, 0.12);
    border: 1px solid rgba(34, 197, 94, 0.25);
    padding: 6px 12px;
    border-radius: 30px;
    font-size: 0.75rem;
    font-weight: 700;
}

/* Feature cards */
.feature-card {
    background: rgba(255,255,255,0.045);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 16px;
    padding: 19px;
    min-height: 135px;
    transition: 0.3s ease;
}

.feature-card:hover {
    transform: translateY(-5px);
    background: rgba(140,120,255,0.10);
}

.feature-icon {
    font-size: 1.8rem;
    margin-bottom: 10px;
}

.feature-heading {
    font-weight: 800;
    color: white;
    margin-bottom: 5px;
}

.feature-description {
    font-size: 0.82rem;
    color: #A5AAC6;
}

/* Animations */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes glow {
    0%, 100% {
        box-shadow: 0 0 12px rgba(139,92,246,0.12);
    }
    50% {
        box-shadow: 0 0 28px rgba(139,92,246,0.30);
    }
}

.glow-effect {
    animation: glow 3s infinite;
}

/* Footer */
.footer {
    text-align: center;
    color: #727B9E;
    padding: 30px 0 10px 0;
    font-size: 0.8rem;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# LOAD YOLO MODEL
# ==========================================

@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")


# ==========================================
# HELPER FUNCTIONS
# ==========================================

def create_metric_card(icon, label, value):
    st.markdown(f"""
    <div class="glass-card">
        <div class="metric-icon">{icon}</div>
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
    </div>
    """, unsafe_allow_html=True)


def resize_frame(frame, max_width=960):
    height, width = frame.shape[:2]

    if width > max_width:
        ratio = max_width / width
        frame = cv2.resize(
            frame,
            (max_width, int(height * ratio))
        )

    return frame


def detect_image(image, model, confidence):
    image_array = np.array(image)
    frame = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)

    results = model.predict(
        frame,
        classes=[0],
        conf=confidence,
        verbose=False
    )

    result = results[0]
    people_count = len(result.boxes)

    annotated = result.plot()
    annotated = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)

    return annotated, people_count


def process_video(uploaded_file, model, confidence, progress_bar):

    temp_input = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp4"
    )

    temp_input.write(uploaded_file.getvalue())
    temp_input.close()

    cap = cv2.VideoCapture(temp_input.name)

    if not cap.isOpened():
        os.unlink(temp_input.name)
        raise ValueError("Unable to open the uploaded video.")

    fps = cap.get(cv2.CAP_PROP_FPS)
    if not fps or fps <= 0:
        fps = 25

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if total_frames <= 0:
        cap.release()
        os.unlink(temp_input.name)
        raise ValueError("The uploaded video has no readable frames.")

    output_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp4"
    )
    output_path = output_file.name
    output_file.close()

    writer = None
    frame_count = 0
    peak_occupancy = 0
    current_count = 0
    tracked_ids = set()

    try:
        while True:

            success, frame = cap.read()

            if not success:
                break

            frame = resize_frame(frame)

            results = model.track(
                frame,
                persist=True,
                classes=[0],
                conf=confidence,
                tracker="bytetrack.yaml",
                verbose=False
            )

            result = results[0]
            current_count = len(result.boxes)

            peak_occupancy = max(
                peak_occupancy,
                current_count
            )

            if result.boxes is not None and result.boxes.id is not None:
                ids = result.boxes.id.int().cpu().tolist()
                tracked_ids.update(ids)

            annotated = result.plot()

            height, width = annotated.shape[:2]

            if writer is None:
                fourcc = cv2.VideoWriter_fourcc(*"mp4v")
                writer = cv2.VideoWriter(
                    output_path,
                    fourcc,
                    fps,
                    (width, height)
                )

                if not writer.isOpened():
                    raise RuntimeError("Could not create the output video.")

            cv2.putText(
                annotated,
                f"PEOPLE: {current_count}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 255),
                2
            )

            cv2.putText(
                annotated,
                f"PEAK OCCUPANCY: {peak_occupancy}",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255),
                2
            )

            writer.write(annotated)

            frame_count += 1

            if frame_count % 5 == 0 or frame_count == total_frames:
                progress_bar.progress(
                    min(frame_count / total_frames, 1.0),
                    text=f"Analyzing video: {frame_count}/{total_frames} frames"
                )

    finally:
        cap.release()

        if writer is not None:
            writer.release()

        if os.path.exists(temp_input.name):
            os.unlink(temp_input.name)

    if frame_count == 0 or writer is None:
        if os.path.exists(output_path):
            os.unlink(output_path)
        raise ValueError("No frames could be processed.")

    return output_path, peak_occupancy, len(tracked_ids), frame_count


# ==========================================
# SIDEBAR NAVIGATION
# ==========================================

with st.sidebar:

    st.markdown("""
    <div class="brand-box">
        <div style="font-size:2rem;">👁️</div>
        <div class="brand-name">VisionCount AI</div>
        <div class="brand-caption">INTELLIGENCE PLATFORM</div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "NAVIGATION",
        [
            "🏠 Dashboard",
            "🔍 Detection Studio",
            "📊 Analytics",
            "ℹ️ About Project"
        ]
    )

    st.markdown("---")

    st.markdown(
        '<div class="status-pill">● YOLO ENGINE READY</div>',
        unsafe_allow_html=True
    )

    st.markdown("")
    st.caption("POWERED BY YOLOv8 + ByteTrack")
    st.caption("VisionCount AI · Day 33")


# ==========================================
# MODEL INITIALIZATION
# ==========================================

try:
    model = load_model()
except Exception as error:
    st.error(f"Unable to load YOLO model: {error}")
    st.stop()


# ==========================================
# DASHBOARD PAGE
# ==========================================

if page == "🏠 Dashboard":

    st.markdown(
        '<div class="status-pill">● SYSTEM ONLINE</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hero-title">See More. Count Smarter.</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="hero-subtitle">
        Intelligent people detection, object tracking and crowd analytics
        powered by computer vision.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        create_metric_card("🎯", "AI ENGINE", "YOLOv8n")

    with col2:
        create_metric_card("🧠", "TRACKING ENGINE", "ByteTrack")

    with col3:
        create_metric_card("⚡", "PROCESSING MODE", "Real-time*")

    st.markdown(
        '<div class="section-title">Explore Your AI Workspace</div>',
        unsafe_allow_html=True
    )

    f1, f2 = st.columns(2)

    with f1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🔍</div>
            <div class="feature-heading">Detection Studio</div>
            <div class="feature-description">
                Upload images or videos and detect people
                with AI-powered bounding boxes and tracking IDs.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with f2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <div class="feature-heading">Crowd Analytics</div>
            <div class="feature-description">
                Understand people counts, peak occupancy,
                unique tracked IDs and video analysis results.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.info(
        "*Video processing is performed frame-by-frame, "
        "not as a live camera stream."
    )

    st.markdown("""
    <div class="footer">
        VISIONCOUNT AI · INTELLIGENT PEOPLE ANALYTICS
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# DETECTION STUDIO PAGE
# ==========================================

elif page == "🔍 Detection Studio":

    st.markdown(
        '<div class="hero-title">Detection Studio</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="hero-subtitle">
        Upload your media and let artificial intelligence analyze the scene.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    confidence = st.slider(
        "Detection Confidence",
        min_value=0.10,
        max_value=0.90,
        value=0.35,
        step=0.05,
        help="Higher confidence may reduce false detections."
    )

    upload_type = st.radio(
        "Choose media type",
        ["Image", "Video"],
        horizontal=True
    )

    if upload_type == "Image":

        uploaded_image = st.file_uploader(
            "Upload an image",
            type=["jpg", "jpeg", "png", "webp"],
            key="image_upload"
        )

        if uploaded_image:

            image = Image.open(uploaded_image).convert("RGB")

            st.markdown(
                '<div class="section-title">Image Preview</div>',
                unsafe_allow_html=True
            )

            st.image(image, use_container_width=True)

            if st.button("✨ Analyze Image", use_container_width=True):

                with st.spinner("AI is detecting people..."):

                    annotated, people_count = detect_image(
                        image,
                        model,
                        confidence
                    )

                st.success("Image analysis completed!")

                st.markdown(
                    '<div class="section-title">Detection Results</div>',
                    unsafe_allow_html=True
                )

                m1, m2 = st.columns(2)

                with m1:
                    create_metric_card(
                        "👥",
                        "PEOPLE DETECTED",
                        people_count
                    )

                with m2:
                    create_metric_card(
                        "🎯",
                        "MODEL",
                        "YOLOv8n"
                    )

                st.markdown("<br>", unsafe_allow_html=True)

                st.image(
                    annotated,
                    caption="AI Processed Image",
                    use_container_width=True
                )

                success, encoded_image = cv2.imencode(
                    ".png",
                    cv2.cvtColor(
                        annotated,
                        cv2.COLOR_RGB2BGR
                    )
                )

                if success:
                    st.download_button(
                        "⬇️ Download Processed Image",
                        data=encoded_image.tobytes(),
                        file_name="visioncount_detected.png",
                        mime="image/png",
                        use_container_width=True
                    )

    else:

        uploaded_video = st.file_uploader(
            "Upload a video",
            type=["mp4", "avi", "mov", "mkv"],
            key="video_upload"
        )

        if uploaded_video:

            st.video(uploaded_video.getvalue())

            st.caption(
                f"Uploaded file: {uploaded_video.name}"
            )

            if st.button("🚀 Process Video", use_container_width=True):

                progress_bar = st.progress(
                    0,
                    text="Preparing video..."
                )

                try:

                    with st.spinner("YOLO is analyzing your video..."):

                        output_path, peak, unique_ids, frames = process_video(
                            uploaded_video,
                            model,
                            confidence,
                            progress_bar
                        )

                    progress_bar.progress(
                        1.0,
                        text="Video processing completed!"
                    )

                    st.success("Video analysis completed successfully!")

                    a, b, c = st.columns(3)

                    with a:
                        create_metric_card(
                            "👥",
                            "PEAK OCCUPANCY",
                            peak
                        )

                    with b:
                        create_metric_card(
                            "🆔",
                            "UNIQUE TRACK IDS",
                            unique_ids
                        )

                    with c:
                        create_metric_card(
                            "🎞️",
                            "FRAMES PROCESSED",
                            frames
                        )

                    st.markdown(
                        '<div class="section-title">Processed Video</div>',
                        unsafe_allow_html=True
                    )

                    with open(output_path, "rb") as output_file:
                        video_bytes = output_file.read()

                    st.video(video_bytes)

                    st.download_button(
                        "⬇️ Download Processed Video",
                        data=video_bytes,
                        file_name="visioncount_processed.mp4",
                        mime="video/mp4",
                        use_container_width=True
                    )

                except Exception as error:
                    st.error(f"Video processing failed: {error}")


# ==========================================
# ANALYTICS PAGE
# ==========================================

elif page == "📊 Analytics":

    st.markdown(
        '<div class="hero-title">Crowd Analytics</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="hero-subtitle">
        Understand the metrics generated by the VisionCount AI engine.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card">
        <h3>📈 Analytics Overview</h3>
        <p style="color:#A5AAC6;">
            The system analyzes video frames and estimates how many
            people are visible in each frame.
        </p>
        <hr style="border-color:rgba(255,255,255,0.1);">
        <p><b>Current people count</b> — people detected in one frame.</p>
        <p><b>Peak occupancy</b> — highest detected count in any processed frame.</p>
        <p><b>Unique tracking IDs</b> — different IDs assigned during tracking.</p>
        <p><b>Detection confidence</b> — model confidence threshold.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Technology Stack</div>',
        unsafe_allow_html=True
    )

    st.write(
        "YOLOv8n · OpenCV · ByteTrack · Streamlit · NumPy · Python"
    )

    st.info(
        "Unique tracking IDs are estimates. Tracking IDs may change "
        "when people leave the scene or are temporarily lost."
    )


# ==========================================
# ABOUT PROJECT PAGE
# ==========================================

elif page == "ℹ️ About Project":

    st.markdown(
        '<div class="hero-title">About VisionCount AI</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="hero-subtitle">
        An AI-powered people detection and crowd analytics application.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card">
        <h3>🎯 Project Objective</h3>
        <p style="color:#A5AAC6;">
            VisionCount AI uses computer vision to detect people in images
            and videos, assign tracking IDs and estimate crowd occupancy.
            It provides visual results and downloadable processed media.
        </p>
        <br>
        <h3>🧠 How It Works</h3>
        <p style="color:#A5AAC6;">
            1. User uploads an image or video.<br>
            2. YOLOv8 detects people (class 0).<br>
            3. ByteTrack maintains identities across video frames.<br>
            4. The system calculates people count and peak occupancy.<br>
            5. Annotated results are displayed and can be downloaded.
        </p>
        <br>
        <h3>🛠️ Built With</h3>
        <p style="color:#A5AAC6;">
            Python · YOLOv8 · OpenCV · ByteTrack · Streamlit · NumPy
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="footer">
        Built as Day 33 · Machine Learning Internship
    </div>
    """, unsafe_allow_html=True)
