import streamlit as st
from gpt import GPT
from prompt import prompt_legal_statement

st.header("GPT-3 legal summariser")

api_key = st.text_input("OpenAI API Key:", type="password")

st.header("Simpler Terms of Service")

statement = st.text_input("Legal statement:")

gpt = GPT(api_key)

if st.button("Summarise"):
    complete_prompt = prompt_legal_statement(statement)
    print(complete_prompt)
    response = gpt.gpt_3(0.8, complete_prompt, 1250)

    st.write(response)



