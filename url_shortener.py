import streamlit as st
import pyshorteners as pyst
shortener=pyst.Shortener()
st.markdown("<h1 style='text-align:center;'>URL Shortener<h1>", unsafe_allow_html=True)
form=st.form("name")
url=form.text_input("URL HERE")
short_btn=form.form_submit_button("Shorten")
if short_btn:
    shortened_url=shortener.tinyurl.short(url)
    st.write(shortened_url)