import streamlit as st
import pandas as pd
import time as ts
from datetime import time
from matplotlib import pyplot as plt
import numpy as np
x=np.linspace(0,10,100)
bar_x=np.array([1,2,3,4,5])

st.title("Hi! i am the streamlit web app")
st.header("i am the header")
st.subheader("Hi i am the subheader")
st.text("Hi i am the text function programmers uses inplace of paragraph tag")


st.markdown("# Heading 1")
st.markdown("## Heading 2")
st.markdown("### Heading 3")
st.markdown("> 💡 Pro Tip: Use filters on the sidebar to refine your data analysis.") #blockquotes
st.markdown("![Alt Text](https://streamlit.io/images/brand/streamlit-mark-color.png)") #to add an image
st.markdown("This is **bold**, this is *italic*, and this is ~~strikethrough~~.")
st.markdown("You can also [add links](https://streamlit.io).")


# Text
st.write("Hello, Streamlit!")

# Numbers
st.write(2025)

# Markdown (basic formatting)
st.write("### This is a heading")

# DataFrame
df = pd.DataFrame({"Brand": ["Nike", "Adidas"], "Price": [2000, 3000]})
st.write(df)

# Math (LaTeX)
st.write("LaTeX: ", r"$a^2 + b^2 = c^2$")

st.metric(label="Total Price", value="12,345 Kshs")
st.metric(label="Discount", value="45%", delta="-5%")
st.metric(label="Returns", value="120", delta="+20", delta_color="inverse")




# Example values
total_price = 500000
mean_price = 1200
mode_price = 999
median_price = 1100
rating = 4.2

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Price", value=f"{total_price:,.0f} Kshs")

with col2:
    st.metric(label="Average Price", value=f"{mean_price:,.0f} Kshs", delta="+200")

with col3:
    st.metric(label="Ratings", value=rating, delta="-0.3", delta_color="inverse")


st.image("data/photo.jpg", caption="my image", width=100)
st.audio("data/audio.mp3")
st.video("data/video.mp4")

state=st.checkbox("kenyan", value=True)
if state:
    st.write("jambo kenya")
else:
    pass
radioButton=st.radio("which country do yo live?", options=("UK","US","KENYA"))

def btn_click():
    st.write("✅ Button was clicked!")
btn=st.button("click me!", on_click=btn_click)
select=st.selectbox("what is your favorite car?", options=("AUDI","BMW","VOLVO","FERRARI"))
st.write(select)

st.title("upload files")
st.markdown("---")
image=st.file_uploader("please upload an image",type=["png","jpg","jpeg"])
if image is not None:
    st.image(image)
#to uplad mutiple images
images=st.file_uploader("please upload an images",type=["png","jpg","jpeg"], accept_multiple_files=True)
if images is not None:
    for image in images:
         st.image(image)
       

myvideo=st.file_uploader("please upload a video",type="mp4")
if myvideo is not None:
    st.video(myvideo)


val=st.slider("this is the slider")#has parameters like min_value,max_value and value
val=st.text_input("enter in your course title", max_chars=60)
textArea=st.text_area("your course description") #you can write your essay or paragraph
date=st.date_input("enter your registration date")
timer=st.time_input("set timer", value=time(0,0,0))
bar=st.progress(0)
for i in range(10):
    bar.progress((i+1)*10)
    ts.sleep(1)

st.markdown("<h1 style='text-align:center;'>User Registration </h1>", unsafe_allow_html=True)
form=st.form("form 1")
form.text_input("First Name")
form.form_submit_button("submit")

# another method to create form:
with st.form("form 2",clear_on_submit=True):
    col1,col2=st.columns(2)
    f_name=col1.text_input("First Name")
    l_name=col2.text_input("Last Name")
    st.text_input("Email Address")
    st.text_input("Password")
    st.text_input("Confirm Password")
    day,month,year=st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("year")
    s_state=st.form_submit_button("submit")

    if s_state:
        if f_name == "" and l_name == "":
            st.warning("please fill the above fields")
        else:
            st.success("submitted successfully")

opt=st.sidebar.radio("Select any graph", options=("Line","Bar","H-Bar"))
if opt=="Line":
    st.markdown("<h1 style='text-align:center;'>Line Chart</h1>", unsafe_allow_html=True)
    fig=plt.figure()
    plt.style.use('ggplot')
    plt.plot(x, np.sin(x))
    plt.plot(x,np.cos(x),'--')
    st.write(fig)

elif opt=="Bar":
    st.markdown("<h1 style='text-align:center;'>Bar Chart</h1>", unsafe_allow_html=True)
    fig=plt.figure()
    plt.style.use('ggplot')
    plt.bar(bar_x,bar_x*10)
    st.write(fig)
else:
    st.markdown("<h1 style='text-align:center;'>H-Bar Chart</h1>", unsafe_allow_html=True)
    fig=plt.figure()
    plt.style.use('ggplot')
    plt.barh(bar_x,bar_x*10)
    st.write(fig)