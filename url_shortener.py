import streamlit as st
import pyshorteners as pyst
shortener=pyst.Shortener()
import pyperclip
def copy():
    pyperclip.copy(shortened_url)

st.markdown("<h1 style='text-align:center;'>URL Shortener<h1>", unsafe_allow_html=True)
form=st.form("name")
url=form.text_input("URL HERE")
short_btn=form.form_submit_button("Shorten")
if short_btn:
    shortened_url=shortener.tinyurl.short(url)
    st.markdown("<h3>Shortened url<h3>", unsafe_allow_html=True)
    st.markdown(f"<h6 style='text-align:center;'>{shortened_url}<h6>", unsafe_allow_html=True)
    st.button("Copy", on_click=copy)