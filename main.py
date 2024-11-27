import cv2
import streamlit as st
from PIL import Image


def to_shine_image(image, result):
    return cv2.convertScaleAbs(image, beta=result)


def to_blur_image(image, result):
    return cv2.GaussianBlur(image, (7, 7), result)


def to_enhance_detail(image):
    return cv2.detailEnhance(image, sigma_s=34, sigma_r=0.50)


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

    if not image:
        return None

    image_original = Image.open(image)

    st.text("Imagem original")
    st.image(image_original)


if __name__ == "__main__":
    main()
