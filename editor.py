import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align:center;'>Image Editor<h1>", unsafe_allow_html=True)
st.markdown("---")
image=st.file_uploader("upload your image", type=["jpg","png","jpeg"])
size=st.empty()
mode=st.empty()
format_=st.empty()
if image:
    img=Image.open(image)
    size.markdown(f"<h6>size: {img.size}<h6>",unsafe_allow_html=True)
    mode.markdown(f"<h6>mode: {img.mode}<h6>",unsafe_allow_html=True)
    format_.markdown(f"<h6>format: {img.format}<h6>",unsafe_allow_html=True)
