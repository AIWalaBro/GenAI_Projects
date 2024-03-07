import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector
from dotenv import load_dotenv

load_dotenv()

# create the user interface

st.set_page_config(page_title = "Marketing Tool",
                   page_icon = "🪶",
                   layout = "centered",
                   initial_sidebar_state="collapsed")


st.header("Hey How can i help you")
form_input = st.text_area("Enter your topics that you wants to generate a Campaign", height = 250)
task_type_option = st.selectbox("plese select the action to be perform",
                                ("write a sales copy","create a tweet", "write a product description")
                                , key = 1)