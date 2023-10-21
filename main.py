import streamlit as st
import os
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title('Virtual Doctor')

gender_option = st.selectbox(
    'Gender',
    ('Male', 'Female'))

age_option = st.selectbox(
    'Age',
    range(1, 99))

symptoms_txt = st.text_area(
    "Write your symptomps",

)
submit_btn = st.button(
    "Analyze",
    type="primary"
)

system_message = "Given a person's age, biological sex, and a list of symptoms, determine the disease they are most likely to have"

if submit_btn:
    user_msg = f"Age: {age_option}\nSex: {gender_option}\nSymptoms: {symptoms_txt}"
    response = chat_completion = openai.ChatCompletion.create(model="ft:gpt-3.5-turbo-0613:personal::8BqMhMuj",
                                                   messages=[{"role": "system", "content": system_message},
                                                             {"role": "user", "content": user_msg}])
    
    predicted_illnes = response.choices[0].message['content']
    st.info(f"There's a chance you might be having {predicted_illnes}.", icon="ℹ️")


