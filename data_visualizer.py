import streamlit as st

st.markdown("<h1 style='text-align:center;'>Data Visualizer<h1>", unsafe_allow_html=True)
st.markdown("---")
files_names=list()
files=st.file_uploader("upload multiple files", type=["xls"],accept_multiple_files=True)
if files:
    for file in files:
        files_names.append(file.name)
selected_files=st.multiselect("Select fils", options=files_names)
if selected_files:
    option=st.radio("Select entity against date", options=["None","First Name", "Last Name","Gender", "Country", "Age","Date", "Id"]) 
    if option != "None":
       st.write(option) 

