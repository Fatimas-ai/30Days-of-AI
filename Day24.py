import streamlit as st
st.write("Hello world")


import streamlit as st
st.title("Ai Assistant")
st.header("Student Management")
st.subheader("Add student")
st.write("Hello Fatima")
st.markdown("# welcome")
st.markdown("""
#AI
**Bold**
*Italic*
""")
st.success("saved successfully")
st.error("wrong password")
st.warning("upload file")
st.info("waiting...")
name=st.text_input("Enter name")
password=st.text_input("password",type="password")
age=st.number_input("Age",0,100)
bio=st.text_area("Bio")
date=st.date_input("DOB")
time=st.time_input("Time")
agree=st.checkbox("Acccept")
gender=st.radio("Gender",["Male","Female"])
city=st.selectbox("city",["Lahore","Karachi","FSD"])
skills=st.multiselect("skills",["python","AI","ML"])
age=st.slider("Age",1,100)
if st.button("Click me"):
    st.write("hello")
name=st.text_input("name")
if st.button("submit"):
    st.success(f"welcome {name}")
st.sidebar.title("Menu")
option=st.sidebar.selectbox("choose",["Home","About"])
col1,col2=st.columns(2)
with col1:
    st.write("left")
with col2:
    st.write("right")


uploaded_file=st.file_uploader(
"Upload File"
) 
uploaded_file=st.file_uploader(
"Image",
type=["png","jpg"]
)
st.image("cat.jpg")
st.image(
"cat.jpg",
width=300
)
st.audio("song.mp3")
st.video("movie.mp4")