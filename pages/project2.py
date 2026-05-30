import streamlit as st

import streamlit as st

def set_bg_image():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://images.pexels.com/photos/34804021/pexels-photo-34804021.jpeg");
            background-attachment: fixed;
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function to apply the background
set_bg_image()

# Rest of your app code goes below



st.title("WHAT'S YOUR CODING LEVEL?")
st.text("You probably know where you are but have you ever thought in this way?")

st.text("Starting with the basic question")
phase = st.selectbox("Which phase of life are you in while coding?", ["Choose phase", "School 🙋‍♂️","In Between School and College period 👻", "College 🧑‍🎓", "Doing internship 😋", "Doing a job 🧑‍💻", "Jobless at Home 😭🙏"])
if phase == "School 🙋‍♂️":
    st.write("Starting at the right time gang!")
if phase == "In Between School and College period 👻":
    st.write("Us bro us")
if phase == "College 🧑‍🎓":
    st.write("Grind time twin!")
if phase == "Doing internship 😋":
    st.write("Amazinggg!")
if phase == "Doing a job 🧑‍💻":
    st.write("Alright techie!")
if phase == "Jobless at Home 😭🙏":
    st.write("Keep going! the work will definitely pay off!")

time = st.radio("How long have you been coding?" , ["0-2 months" , "2-6 months" , "6 months - 1 year" , "1-2 years" , "2-5 years" , "5-10 years" , "10+ years"])
if time == "0-2 months":
    st.write("So you are a beginner like me (when I am making this)✌️")
elif time == "2-6 months":
    st.write("So you surely know some things now 😼")
elif time == "6 months - 1 year":
    st.write("Getting Better and Better! 💪")
elif time == "1-2 years":
    st.write("Putting the work in! 🔥")
elif time == "2-5 years":
    st.write("That's Tufff 🥶")
elif time == "5-10 years":
    st.write("You're killing it ngl! 🫶")
elif time == "10+ years":
    st.write("A master of work 🫡")

