import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter


from langchain_google_genai import GoogleGenerativeAI
from langchain.llms import google_palm
import google.generativeai as palm
from langchain.embeddings import GooglePalmEmbeddings

from langchain.vectorstores import FAISS
from langchain.vectorstores import VectorStore
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
import os


from dotenv import load_dotenv
from utils import get_pdf_text

os.environ['GOOGLE_API_KEY'] = "GOOGLE_API_KEY"


def get_pdf_text(pad_doc):
    text = ""
    for page in pad_doc:
        no_pages = PdfReader(page)
        for page in no_pages.pages:
            text += page.extract_text()    
    return text

def get_text_chunks(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size = 10000, chunk_overlap = 1000)
    chuncks = splitter.split_text(text)
    return chuncks

def get_vector_store(text_chunk):
    embeddings = GooglePalmEmbeddings()
    vector = FAISS.from_texts(text_chunk , embedding = embeddings)
    return vector

def get_conversational_chain(vector_store):
    
    llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key= "GOOGLE_API_KEY")
    memory = ConversationBufferMemory(memory_key = "chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=vector_store.as_retriever(), memory=memory)
    return conversation_chain

def user_input(user_question):
    response = st.session_state.conversation({"question":"user_question"})
    st.session_state.chatHistory = response['chat_history']
    for i, message in enumerate(st.session_state.chatHistory):
        if i%2 == 0:
            st.write('Human:',message.content)
        else:
            st.write('Bot:', message.content)
            
            
def main():
    st.set_page_config("Char with multiple PDF file")
    st.header("Palm Questions & Answers Application")
    user_question = st.text_input("Ask a Questions from the PDF files")
    
    if "conversation" not in st.session_state:
        st.session_state.conversation = None  # Initialize as None

    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = None
    if user_question:
        user_input(user_question)
    with st.sidebar:
        st.title("Settings")
        st.subheader("Upload your Documents")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Process Button", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vector_store = get_vector_store(text_chunks)
                st.session_state.conversation = get_conversational_chain(vector_store)
                st.success("Done")

if __name__ == "__main__":
    main()

        
