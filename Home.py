import streamlit as st

st.title("Hello!")
st.text("I am learning streamlit which is a python framework")
st.header("These are small projects/pages I made while learning different syntax")
st.subheader("Just click on one of these or you can also access all the pages from the sidebar")

st.page_link("pages/project1.py", label="Know your Favourite Programming Language", icon="1️⃣")
st.page_link("pages/project2.py", label="Know your Coding Level", icon="2️⃣")

