import streamlit as st
from gpt import Gpt
from prompt import prompt_marv_qa

st.header("GPT-3 application")
api_key = st.text_input("OpenAI API Key:", type="password")

st.header("Your personal sarcastic bot - Marv")
question_for_marv = st.text_input("Question For Marv:")

gpt = Gpt(api_key)

if st.button("Answer"):
    st.write(gpt.gpt_3(temp=0.8, prompt=prompt_marv_qa(question_for_marv)))

