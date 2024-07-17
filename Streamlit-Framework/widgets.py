import streamlit as st

st.title("Streamllit Text input")

name=st.text_input("Enter your name...")

age=st.slider("Age",0,100,25)
options=['Pythons',"java language ","C++"]
choice=st.selectbox("Choice:",options)


if name:
    st.write(f"Hello, {name}!")