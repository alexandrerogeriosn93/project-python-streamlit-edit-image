import cv2
import streamlit as st
import numpy as np
from PIL import Image
from skimage import morphology, filters


def to_shine_image(image, result):
    return cv2.convertScaleAbs(image, beta=result)


def to_blur_image(image, result):
    return cv2.GaussianBlur(image, (7, 7), result)


def to_enhance_detail(image):
    return cv2.detailEnhance(image, sigma_s=34, sigma_r=0.50)


def change_image_to_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def main():
    st.title("OpenCV Data App")
    st.subheader(
        "Este aplicativo web permite integrar processamento de imagens com OpenCV"
    )
    st.text("Streamlit com OpenCV")

    image = st.file_uploader("Envie sua imagem", type=["jpg", "png", "jpeg"])

    blur_level = st.sidebar.slider("Blur", min_value=0.2, max_value=3.5)
    shine_level = st.sidebar.slider("Brilho", min_value=-50, max_value=50, value=0)
    filter_level = st.sidebar.checkbox("Melhorar detalhes da imagem")
    image_gray = st.sidebar.checkbox("Converter para a escala de cinza")
    image_erosion = st.sidebar.checkbox("Filtro erosão")
    image_dilation = st.sidebar.checkbox("Filtro dilatação")
    image_edge = st.sidebar.checkbox("Filtro Edge")

    if not image:
        return None

    image_original = Image.open(image)
    image_original = np.array(image_original)

    image_processed = to_blur_image(image_original, blur_level)
    image_processed = to_shine_image(image_processed, shine_level)

    if filter_level:
        image_processed = to_enhance_detail(image_processed)

    if image_gray:
        image_processed = change_image_to_gray(image_processed)

    if image_erosion:
        image_processed = morphology.erosion(image_processed)

    if image_dilation:
        image_processed = morphology.dilation(image_processed)

    if image_edge:
        image_processed = filters.sobel(image_processed)

    st.text("Imagem original vs Imagem processada")
    st.image([image_original, image_processed])


if __name__ == "__main__":
    main()
