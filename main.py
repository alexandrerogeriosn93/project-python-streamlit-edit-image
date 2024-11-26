import cv2
import streamlit as st


def main():
    st.title("OpenCV Data App")
    st.subheader(
        "Este aplicativo web permite integrar processamento de imagens com OpenCV"
    )
    st.text("Streamlit com OpenCV")

    image = cv2.imread("img/placeholder.png")

    st.text("Imagem original")
    st.image(image)


if __name__ == "__main__":
    main()
