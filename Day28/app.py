
import gradio as gr
import os
from PIL import Image
from programs.image_processor import process_image

# Create output folder
os.makedirs("sample_outputs", exist_ok=True)


def run_processing(image, operation, brightness, contrast, rotation):

    if image is None:
        raise gr.Error("Please upload an image first!")

    result = process_image(
        image,
        operation,
        brightness,
        contrast,
        rotation
    )

    output_path = os.path.abspath(
        "sample_outputs/processed_image.png"
    )

    Image.fromarray(result).save(output_path)

    return result, output_path


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


custom_css = """
.gradio-container {
    max-width: 1100px !important;
    margin: auto !important;
}

#main-title {
    text-align: center;
    padding: 20px;
}

#process-btn {
    font-weight: bold;
}
"""


with gr.Blocks(
    theme=gr.themes.Soft(),
    css=custom_css,
    title="Computer Vision Image Processing Studio"
) as demo:

    gr.Markdown(
        """
        # Computer Vision Image Processing Studio
        ### Transform your images using Python, OpenCV and Gradio.

        Upload an image, select an operation and explore
        different computer vision techniques.
        """,
        elem_id="main-title"
    )

    gr.Markdown("## Image Upload & Preview")

    with gr.Row():

        input_image = gr.Image(
            label="Original Image",
            type="numpy",
            sources=["upload"]
        )

        output_image = gr.Image(
            label="Processed Image",
            type="numpy"
        )

    gr.Markdown("## Processing Settings")

    operation = gr.Dropdown(
        choices=operations,
        value="Grayscale",
        label="Choose Processing Operation"
    )

    with gr.Accordion("Advanced Adjustments", open=False):

        with gr.Row():

            brightness = gr.Slider(
                minimum=-100,
                maximum=100,
                value=0,
                step=5,
                label="Brightness"
            )

            contrast = gr.Slider(
                minimum=0.5,
                maximum=3.0,
                value=1.0,
                step=0.1,
                label="Contrast"
            )

            rotation = gr.Slider(
                minimum=0,
                maximum=360,
                value=90,
                step=15,
                label="Rotation Angle"
            )

    process_button = gr.Button(
        "Process Image",
        variant="primary",
        elem_id="process-btn"
    )

    download_file = gr.File(
        label="Download Your Processed Image"
    )

    process_button.click(
        fn=run_processing,
        inputs=[
            input_image,
            operation,
            brightness,
            contrast,
            rotation
        ],
        outputs=[
            output_image,
            download_file
        ]
    )

    gr.Markdown(
        """
        ---

        **Features:** Grayscale | Blur | Edge Detection |
        Rotation | Enhancement | Contours | Shape Detection |
        Sharpening | Thresholding | Custom Filters

        **Technologies:** Python • OpenCV • NumPy • Gradio

        **Project:** MLB Internship - Day 28
        """
    )


if __name__ == "__main__":
    demo.launch()
