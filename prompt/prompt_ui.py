from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import streamlit as st


st.header('Research Tool')

user_input = st.text_input('Enter your prompt')

if st.button('Summerize'):
    st.text('some random text')

