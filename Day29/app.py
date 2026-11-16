
import streamlit as st
import easyocr
import numpy as np
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="OCR Text Extractor",
    page_icon="📄",
    layout="wide"
)

# Load EasyOCR model only once
@st.cache_resource
def load_ocr_model():
    return easyocr.Reader(['en'], gpu=False)

# App heading
st.title("📄 OCR Text Extractor")
st.write(
    "Upload an image and extract its text using "
    "EasyOCR and Computer Vision."
)

st.divider()

# Image upload
uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    left, right = st.columns(2)

    with left:
        st.subheader("Original Image")
        st.image(image, use_container_width=True)

    with right:
        st.subheader("Extracted Text")

        if st.button("Extract Text", type="primary"):

            with st.spinner("Loading OCR model and extracting text..."):

                reader = load_ocr_model()

                image_array = np.array(image)

                results = reader.readtext(image_array)

                extracted_text = []
                confidence_scores = []

                for box, text, confidence in results:
                    extracted_text.append(text)
                    confidence_scores.append(confidence)

                final_text = "\n".join(extracted_text)

            if final_text:

                st.success("Text extracted successfully!")

                st.text_area(
                    "OCR Results",
                    value=final_text,
                    height=250
                )

                average_confidence = (
                    sum(confidence_scores) / len(confidence_scores)
                )

                st.metric(
                    "Average OCR Confidence",
                    f"{average_confidence:.2%}"
                )

                # Download extracted text
                st.download_button(
                    label="Download Extracted Text",
                    data=final_text,
                    file_name="extracted_text.txt",
                    mime="text/plain"
                )

            else:
                st.warning("No text detected in this image.")

else:
    st.info("Please upload an image to begin.")

st.divider()

st.caption("Developed using Python, Streamlit, OpenCV and EasyOCR.")
