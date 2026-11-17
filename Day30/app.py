
import streamlit as st
import cv2
import numpy as np
from PIL import Image
from io import BytesIO

st.set_page_config(
    page_title="Segmentation Studio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM DESIGN ----------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #080d1b, #10172b 55%, #11152b);
    color: #f1f5f9;
}

[data-testid="stSidebar"] {
    background: #0b1120;
    border-right: 1px solid #26314a;
}

.main-title {
    font-size: 38px;
    font-weight: 800;
    letter-spacing: -1.5px;
    background: linear-gradient(90deg, #a78bfa, #60a5fa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    color: #9ba9c4;
    font-size: 15px;
    margin-bottom: 25px;
}

.hero {
    background: linear-gradient(120deg, #22234a, #182d4b);
    border: 1px solid #38466b;
    border-radius: 18px;
    padding: 25px;
    margin-bottom: 25px;
}

.hero h2 {
    margin: 0;
    color: #ffffff;
    font-size: 23px;
}

.hero p {
    color: #c0cbe0;
    margin-bottom: 0;
}

.metric-card {
    background: #151f35;
    border: 1px solid #2c3a57;
    border-radius: 14px;
    padding: 18px;
    min-height: 100px;
}

.metric-label {
    color: #94a3b8;
    font-size: 13px;
}

.metric-value {
    color: #c4b5fd;
    font-size: 25px;
    font-weight: 700;
    margin-top: 7px;
}

.section-heading {
    color: #e2e8f0;
    font-size: 20px;
    font-weight: 700;
    margin-top: 25px;
}

.stButton > button {
    background: linear-gradient(90deg, #7c3aed, #2563eb);
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 600;
    min-height: 45px;
}

.stButton > button:hover {
    border: 1px solid #a78bfa;
    color: white;
}

div[data-testid="stFileUploader"] {
    background: #151f35;
    border: 1px dashed #6474a0;
    border-radius: 14px;
    padding: 12px;
}

.stSelectbox > div > div {
    background: #151f35;
    border-radius: 10px;
}

.footer {
    color: #71809d;
    text-align: center;
    font-size: 12px;
    padding: 25px 0 10px;
}
</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------

with st.sidebar:
    st.markdown("## ✦ SEGMENT AI")
    st.caption("IMAGE PROCESSING STUDIO")
    st.divider()

    page = st.radio(
        "NAVIGATION",
        ["Dashboard", "About Project"]
    )

    st.divider()
    st.markdown("**TOOLS & TECHNOLOGIES**")
    st.caption("OpenCV · NumPy · Streamlit")
    st.caption("Computer Vision Project")
    st.divider()
    st.caption("Developed by Muskan Ejaz")


# ---------------- ALGORITHMS ----------------

def apply_segmentation(image, method):

    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    if method == "Binary Thresholding":
        _, result = cv2.threshold(
            gray, 127, 255, cv2.THRESH_BINARY
        )
        return cv2.cvtColor(result, cv2.COLOR_GRAY2RGB)

    elif method == "Adaptive Thresholding":
        result = cv2.adaptiveThreshold(
            gray, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11, 2
        )
        return cv2.cvtColor(result, cv2.COLOR_GRAY2RGB)

    elif method == "Otsu Thresholding":
        _, result = cv2.threshold(
            gray, 0, 255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )
        return cv2.cvtColor(result, cv2.COLOR_GRAY2RGB)

    elif method == "GrabCut Background Removal":

        height, width = image.shape[:2]
        mask = np.zeros((height, width), np.uint8)

        margin_x = max(1, int(width * 0.05))
        margin_y = max(1, int(height * 0.05))

        rect = (
            margin_x,
            margin_y,
            max(1, width - 2 * margin_x),
            max(1, height - 2 * margin_y)
        )

        bg_model = np.zeros((1, 65), np.float64)
        fg_model = np.zeros((1, 65), np.float64)

        cv2.grabCut(
            image.copy(), mask, rect,
            bg_model, fg_model, 5,
            cv2.GC_INIT_WITH_RECT
        )

        foreground = np.where(
            (mask == cv2.GC_FGD) |
            (mask == cv2.GC_PR_FGD),
            255, 0
        ).astype(np.uint8)

        result = np.full_like(image, 255)
        result[foreground == 255] = image[foreground == 255]

        return result

    elif method == "Watershed Segmentation":

        _, binary = cv2.threshold(
            gray, 0, 255,
            cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
        )

        kernel = np.ones((3, 3), np.uint8)

        opening = cv2.morphologyEx(
            binary, cv2.MORPH_OPEN,
            kernel, iterations=2
        )

        sure_background = cv2.dilate(
            opening, kernel, iterations=3
        )

        distance = cv2.distanceTransform(
            opening, cv2.DIST_L2, 5
        )

        _, sure_foreground = cv2.threshold(
            distance, 0.4 * distance.max(), 255, 0
        )

        sure_foreground = np.uint8(sure_foreground)

        unknown = cv2.subtract(
            sure_background, sure_foreground
        )

        _, markers = cv2.connectedComponents(sure_foreground)
        markers = markers + 1
        markers[unknown == 255] = 0

        markers = cv2.watershed(
            cv2.cvtColor(image.copy(), cv2.COLOR_RGB2BGR),
            markers
        )

        result = image.copy()
        result[markers == -1] = [255, 0, 0]

        return result

    return image


# ---------------- DASHBOARD ----------------

if page == "Dashboard":

    st.markdown(
        '<div class="main-title">AI Image Segmentation Studio</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Transform images into meaningful regions using computer vision algorithms.</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="hero">
        <h2>✦ Intelligent Image Processing</h2>
        <p>Upload an image, select a segmentation technique and explore the results instantly.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">SEGMENTATION METHODS</div>
            <div class="metric-value">05</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">DATASET IMAGES</div>
            <div class="metric-value">15</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">PROCESSING ENGINE</div>
            <div class="metric-value">OpenCV</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-heading">Upload Your Image</div>',
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader(
        "Choose an image (JPG, JPEG, PNG)",
        type=["jpg", "jpeg", "png"]
    )

    methods = [
        "Binary Thresholding",
        "Adaptive Thresholding",
        "Otsu Thresholding",
        "GrabCut Background Removal",
        "Watershed Segmentation"
    ]

    col1, col2 = st.columns([2, 1])

    with col1:
        selected_method = st.selectbox(
            "Select Segmentation Method",
            methods
        )

    descriptions = {
        "Binary Thresholding":
            "Separates pixels using a fixed intensity threshold.",
        "Adaptive Thresholding":
            "Calculates local thresholds for different image regions.",
        "Otsu Thresholding":
            "Automatically calculates an optimal threshold.",
        "GrabCut Background Removal":
            "Separates the foreground object from its background.",
        "Watershed Segmentation":
            "Uses image regions and boundaries to separate objects."
    }

    with col2:
        st.markdown("**ABOUT METHOD**")
        st.caption(descriptions[selected_method])

    if uploaded_file is not None:

        original = Image.open(uploaded_file).convert("RGB")
        original_array = np.array(original)

        st.markdown(
            '<div class="section-heading">Image Processing</div>',
            unsafe_allow_html=True
        )

        if st.button("✦ Process Image", use_container_width=True):

            try:
                with st.spinner("Processing your image..."):

                    processed = apply_segmentation(
                        original_array,
                        selected_method
                    )

                    st.session_state["processed"] = processed
                    st.session_state["method"] = selected_method
                    st.session_state["original"] = original_array

                st.success("Image processed successfully!")

            except Exception as error:
                st.error(f"Processing error: {error}")

        if "processed" in st.session_state:

            if st.session_state["method"] == selected_method:

                left, right = st.columns(2)

                with left:
                    st.markdown("**Original Image**")
                    st.image(
                        st.session_state["original"],
                        use_container_width=True
                    )

                with right:
                    st.markdown("**Segmented Result**")
                    st.image(
                        st.session_state["processed"],
                        use_container_width=True
                    )

                result_image = Image.fromarray(
                    st.session_state["processed"]
                )

                buffer = BytesIO()
                result_image.save(buffer, format="PNG")

                st.download_button(
                    "⬇ Download Segmented Image",
                    data=buffer.getvalue(),
                    file_name="segmentation_result.png",
                    mime="image/png",
                    use_container_width=True
                )

    else:
        st.info("Upload an image to start segmentation.")

    st.markdown("""
    <div class="footer">
        AI Image Segmentation Studio · Built with Python, OpenCV & Streamlit
    </div>
    """, unsafe_allow_html=True)


# ---------------- ABOUT PAGE ----------------

elif page == "About Project":

    st.markdown(
        '<div class="main-title">About This Project</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    This project demonstrates image segmentation techniques using
    OpenCV and Python.

    ### Implemented Techniques

    - **Binary Thresholding:** Uses a fixed threshold to classify pixels.
    - **Adaptive Thresholding:** Uses local pixel neighborhoods.
    - **Otsu Thresholding:** Automatically selects a threshold value.
    - **GrabCut:** Separates foreground and background.
    - **Watershed:** Identifies boundaries between image regions.

    ### Technologies

    - Python
    - OpenCV
    - NumPy
    - Pillow
    - Streamlit

    ### Project Developer

    Muskan Ejaz

    **Objective:** Build an interactive image segmentation tool that
    allows users to upload images, apply computer vision techniques,
    compare results and download processed images.
    """)
