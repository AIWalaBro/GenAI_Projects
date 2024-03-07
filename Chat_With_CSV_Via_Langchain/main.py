import os
import streamlit as st
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain_experimental.agents.agent_toolkits import create_csv_agent


def main():
    load_dotenv()
    
    # load openai api key from environment variable
    if os.getenv('OPENAI_API_KEY') is None or os.getenv('OPENAI_API_KEY') == '':
        print('OpenAI key does not setup')
        exit(1)
    else:
        print('OpenAI key is setup')
     
    # set the page title and header
    st.set_page_config(page_title = "Ask with your CSV")
    st.header("ask your CSV file")
    
    # to upload the csv file
    csv_file = st.file_uploader("upload the csv file", type = "csv")
    
    if csv_file is not None:
        agent = create_csv_agent(
            OpenAI(temperature = 0), csv_file, verbose = True)
        
        user_question = st.text_input("Please enter your query about your csv file")
        
        if user_question is not None or user_question  != "":
            with st.spinner(text = "in progress..."):
                st.write(agent.run(user_question))
        
if __name__ == '__main__':
    main()
   
    
    

