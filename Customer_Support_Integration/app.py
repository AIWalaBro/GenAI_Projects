import streamlit as st
from utils import *
import os
from constants import *


if 'HuggingFace_API_Key' not in st.session_state:
    st.session_state['HuggingFace_API_Key'] = ''
if 'Pinecone_API_Key' not in st.session_state:
    st.session_state['Pinecone_API_Key'] = ''
    

# set the title 
st.title("Support Assistance Bot for Websites")


# set the side title bar for receving the api key
st.sidebar.title = ['receive the api key']

st.session_state['HuggingFace_API_Key']  = st.sidebar.text_input('what is your huggingface api key?', type = 'password')
st.session_state['Pinecone_API_Key'] = st.sidebar.text_input('what is your pincecone api key?', type = 'password')

# load api key

os.environ['PINECONE_API_Key'] = st.session_state['Pinecone_API_Key']

load_button = st.sidebar.button("Load data to Pinecone", key= "load_button")

if load_button:
    if st.session_state['PINECONE_API_Key'] != "" and st.session_state['HuggingFace_API_Key'] != "":
        
        # pull data from the server
        site_data = st.get_website_data(constants.WEBSITE_URL)
        st.write("Data pull done")
        
        # create chunks
        chunks_data = split_data(site_data)
        st.write('spliiting data done ')
        
        # create embed data
        embedd_data  = create_embeddings(chunks_data)
        st.write('embedding creation done')
        
        # push data to pinecone
        push_to_pinecone(st.session_state['Pinecone_API_Key'], constants.PINECONE_ENVIRONMENT, constants.PINECONE_INDEX, embedd_data, chunks_data )
        st.write("Pushing data to Pinecone done...")
        
        st.sidebar.success("Data pushed to Pinecone successfully!")
    else:
        st.sidebar.error("Ooopssss!!! Please provide API keys.....")
        
# capture inputs

prompt = st.text_input('How can I help you my friend ❓',key="prompt")
document_count = st.slider('No.Of links to return 🔗 - (0 LOW || 5 HIGH)', 0, 5, 2,step=1)

submit = st.button("Search")   


if submit:
    if st.session_state['PINECONE_API_Key'] != "" and st.session_state['HuggingFace_API_Key'] != "":
        embeddings = create_embeddings()
        st.write('Embedding insntance creation is done..')
        
        # pull from the pinecone
        index = pull_from_pinecone(st.session_state['Pinecone_API_Key'],constants.PINECONE_ENVIRONMENT, constants.PINECONE_INDEX, embeddings)
        st.write("Pinecone index retrieval done...")
        
        # Fetch relevent document from the pinecone
        relavant_docs = get_similar_docs(index, prompt, document_count)
        st.write(relavant_docs)
        
        #Displaying search results
        st.success("Please find the search results :")
        
        #Displaying search results
        st.write("search results list....")
        
       
        for document in relavant_docs:
            st.write("👉**Result : "+ str(relavant_docs.index(document)+1)+"**")
            st.write("**Info**: "+document.page_content)
            st.write("**Link**: "+ document.metadata['source'])
    else:
        st.sidebar.error("Ooopssss!!! Please provide API keys.....")