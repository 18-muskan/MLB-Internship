
import streamlit as st
import numpy as np
from PIL import Image
import io

from programs.image_processor import process_image

st.set_page_config(
    page_title="Computer Vision Image Studio",
    page_icon="📸",
    layout="wide"
)

st.title("📸 Computer Vision Image Processing Studio")
st.write("Upload an image and apply different OpenCV operations.")

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)

operations = [
    "Grayscale",
    "Gaussian Blur",
    "Edge Detection",
    "Image Rotation",
    "Image Enhancement",
    "Contour Detection",
    "Shape Detection",
    "Brightness & Contrast",
    "Image Sharpening",
    "Image Flip",
    "Thresholding",
    "Multiple Filters"
]

operation = st.selectbox("Select Processing Operation", operations)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")
    image_array = np.array(image)

    angle = 90
    brightness = 0
    contrast = 1.0

    if operation == "Image Rotation":
        angle = st.slider("Rotation Angle", 0, 360, 90)

    if operation == "Brightness & Contrast":
        brightness = st.slider("Brightness", -100, 100, 0)
        contrast = st.slider("Contrast", 0.5, 3.0, 1.0)

    try:
        result = process_image(
            image_array,
            operation,
            brightness=brightness,
            contrast=contrast,
            rotation=angle
        )

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original Image")
            st.image(image_array, use_container_width=True)

        with col2:
            st.subheader("Processed Image")
            st.image(result, use_container_width=True)

        output = Image.fromarray(result)
        buffer = io.BytesIO()
        output.save(buffer, format="PNG")

        st.download_button(
            label="⬇️ Download Processed Image",
            data=buffer.getvalue(),
            file_name="processed_image.png",
            mime="image/png"
        )

        st.success("Image processed successfully!")

    except Exception as error:
        st.error(f"Processing Error: {error}")

else:
    st.info("Please upload an image to get started.")
