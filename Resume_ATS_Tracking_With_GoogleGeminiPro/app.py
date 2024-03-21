# providing prompt template with the help of parameter inside prompt

import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf




# load all the api key from the environment
from dotenv import load_dotenv
load_dotenv() 

# load api key from .env variable
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function for gemini reponse
# def get_gemini_response(input):
#     model = genai.GenerativeModel('gemini-pro')
#     response = model.generate_content(input)
#     return response.text

def get_gemini_repsonse(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

# def input_pdf_text(uploaded_pdf):
#     reader = pdf.PdfReader(uploaded_pdf)
#     text=""
#     text = ""
#     for page in reader(len(reader.pages)):
#         page = reader.pages['page']
#         text += str(page.extract_text)
#         return text
    
def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text
    
    
input_prompt="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""

## streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_repsonse(input_prompt)
        st.subheader(response)