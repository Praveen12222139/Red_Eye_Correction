import streamlit as st
from PIL import Image
import numpy as np
import cv2


def fillHoles(mask):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)


def detect_eyes(image_file):
    ima = Image.open(image_file)
    filebyte = np.array(ima)
    img = cv2.cvtColor(filebyte, cv2.COLOR_RGB2BGR)

    eyesCascade = cv2.CascadeClassifier(r'haarcascade_eye.xml')
    if eyesCascade.empty():
        raise ValueError("Haar cascade XML file not found or unable to load.")

    eyeRects = eyesCascade.detectMultiScale(img, 1.2, 20)

    imgOut = img.copy()
    for (x, y, w, h) in eyeRects:
        eyeImage = img[y:y + h, x: x + w]
        blue, green, red = cv2.split(eyeImage)

        bg = cv2.add(blue, green)
        mask = (red > 50) & (red > bg)
        mask = mask.astype(np.uint8) * 255

        # Clean up mask by filling holes and dilating
        mask = fillHoles(mask)
        mask = cv2.dilate(mask, None, anchor=(-1, -1), iterations=1, borderType=1, borderValue=1)

        mean = bg // 2
        mask = mask.astype(bool)[:, :, np.newaxis]
        mean = mean[:, :, np.newaxis]

        # Copy the eye from the original image.
        eyeOut = eyeImage.copy()
        eyeOut = eyeOut.astype(np.ndarray)

        # Copy the mean image to the output image.
        np.copyto(eyeOut, mean, where=mask)

        # Copy the fixed eye to the output image.
        imgOut[y:y + h, x: x + w, :] = eyeOut

    return imgOut


# Streamlit app setup
st.title('Red-Eye Detection and Correction')

image_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if image_file is not None:
    our_image = Image.open(image_file)
    st.text('Original Image')
    st.image(our_image, use_column_width=True)

    if st.button('Show Corrected Result'):
        result_image = detect_eyes(image_file)
        st.text('Output Image')
        st.image(result_image, channels="BGR", use_column_width=True)
