import streamlit as st
import pandas as pd
def date_converter (date_col):
    result=list()
    values=date_col.values
    for value in values:
        result.append(str(value).split("T")[0])
    return result
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
       for file in files:
           if file.name in selected_files:
               sample_data=pd.read_excel(file,index_col=0)
               dates=date_converter(sample_data["Date"])
               st.write(dates)
               

