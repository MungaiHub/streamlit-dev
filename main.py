import streamlit as st
import pandas as pd

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