import streamlit as st

# to load the environment variables
from dotenv import load_dotenv
load_dotenv()

import os
import  google.generativeai as genai
from PIL import Image

# configure the genrative ai api key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# function to load gemini pro vision model
# model = genai.GenerativeModel('gemini-pro-vision')

# create the fucntion for gemini pro response
def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,image[0],prompt])
    return response.text
    


# lets upalod the pdf or jpeg file and converts it into the bytes
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data =  uploaded_file.getvalue()
        image_parts = [
        {
            "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
            "data": bytes_data
        }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
        
        
# create the streamlit application

st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Application")

input = st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""  
 
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    
submit=st.button("Tell me about the image")

input_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image
               """
               
## If ask button is clicked

if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)