import cv2
import streamlit as st
from PIL import Image


def main():
    st.title("OpenCV Data App")
    st.subheader(
        "Este aplicativo web permite integrar processamento de imagens com OpenCV"
    )
    st.text("Streamlit com OpenCV")

    image = st.file_uploader("Envie sua imagem", type=["jpg", "png", "jpeg"])

    if not image:
        return None

    image_original = Image.open(image)

    st.text("Imagem original")
    st.image(image_original)


if __name__ == "__main__":
    main()
