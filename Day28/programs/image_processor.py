
import cv2
import numpy as np


def process_image(image, operation, brightness=0, contrast=1.0, rotation=90):
    """
    Process an uploaded image using the selected OpenCV operation.
    """

    if image is None:
        return None

    # Convert RGB image to OpenCV format
    img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if operation == "Grayscale":
        result = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        result = cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)

    elif operation == "Gaussian Blur":
        result = cv2.GaussianBlur(img, (15, 15), 0)

    elif operation == "Edge Detection":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        result = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    elif operation == "Image Rotation":
        height, width = img.shape[:2]
        center = (width // 2, height // 2)

        matrix = cv2.getRotationMatrix2D(center, rotation, 1.0)
        result = cv2.warpAffine(img, matrix, (width, height))

    elif operation == "Image Enhancement":
        lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)

        clahe = cv2.createCLAHE(
            clipLimit=2.0,
            tileGridSize=(8, 8)
        )

        enhanced = clahe.apply(l)
        merged = cv2.merge((enhanced, a, b))

        result = cv2.cvtColor(
            merged,
            cv2.COLOR_LAB2BGR
        )

    elif operation == "Contour Detection":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(
            gray, 127, 255, cv2.THRESH_BINARY
        )

        contours, _ = cv2.findContours(
            thresh,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        result = img.copy()
        cv2.drawContours(result, contours, -1, (0, 255, 0), 2)

    elif operation == "Shape Detection":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)

        contours, _ = cv2.findContours(
            edges,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        result = img.copy()

        for contour in contours:
            area = cv2.contourArea(contour)

            if area < 500:
                continue

            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(
                contour, 0.04 * perimeter, True
            )

            corners = len(approx)

            if corners == 3:
                shape = "Triangle"
            elif corners == 4:
                shape = "Rectangle"
            elif corners > 7:
                shape = "Circle"
            else:
                shape = "Polygon"

            cv2.drawContours(result, [approx], -1, (0, 255, 0), 2)

            x, y, w, h = cv2.boundingRect(approx)
            cv2.putText(
                result,
                shape,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 0, 255),
                2
            )

    elif operation == "Brightness & Contrast":
        result = cv2.convertScaleAbs(
            img,
            alpha=contrast,
            beta=brightness
        )

    elif operation == "Image Sharpening":
        kernel = np.array([
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]
        ])

        result = cv2.filter2D(img, -1, kernel)

    elif operation == "Image Flip":
        result = cv2.flip(img, 1)

    elif operation == "Thresholding":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        _, threshold = cv2.threshold(
            gray, 127, 255, cv2.THRESH_BINARY
        )

        result = cv2.cvtColor(
            threshold,
            cv2.COLOR_GRAY2BGR
        )

    elif operation == "Multiple Filters":
        # Apply grayscale, blur and edge detection in sequence
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blurred, 50, 150)

        result = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    else:
        result = img.copy()

    # Convert processed image back to RGB
    result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

    return result
