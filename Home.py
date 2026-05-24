import streamlit as st
st.title("Pages")
st.subheader("I am learning streamlit which is a python framework")
st.text("These are small projects/pages I made while learning different syntax")
a = st.button("Know about your Favourite Programming Language")
if a:
    st.switch_page("pages/main.py")