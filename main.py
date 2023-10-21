import streamlit as st

st.title('virtual Doctor')

gender_option = st.selectbox(
    'Gender',
    ('Male', 'Female'))

age_option = st.selectbox(
    'Age',
    range(1,99))

symptoms_txt = st.text_area(
    "Write your symptomps",

    )
submit_btn =  st.button(
    "Analyze"
)

