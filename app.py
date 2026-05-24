import streamlit as st
import time

st.title("Webcam Security Monitoring")

img = st.camera_input("Open Webcam")

if img:
    st.success("Webcam is being used")

    with open("log.txt", "a") as f:
        f.write(f"Accessed at {time.ctime()}\n")

    st.image(img)
