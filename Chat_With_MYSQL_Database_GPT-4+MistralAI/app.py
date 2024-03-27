import streamlit as st
from langchain_community.utilities import SQLDatabase
from langchain_core.messages import AIMessage, HumanMessage
from dotenv import load_dotenv
load_dotenv()


# connect the database to connect button
def init_database(user:str, password:str, host:str, port:str, database:str) -> SQLDatabase:
    # db_uri = f"mysql+mysqlconnector://{user}{password}@{host}{port}/{databse}"
    db_uri = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
    return SQLDatabase.from_uri(db_uri)


# create a session state 


if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
      AIMessage(content="Hello! I'm a SQL assistant. Ask me anything about your database."),
    ]
                                   

# create streamlit page

st.set_page_config(page_title="Chat with MYSQL Database",page_icon=":speech_balloon:",
                   layout="centered")

st.title("Chat with MYSQL Database")

with st.sidebar:
    st.subheader("Settings")
    st.write("This is a simple chat application using MySQL. Connect to the database and start chatting.")
    
    st.text_input("Host", value="localhost", key="Host")
    st.text_input("Port", value="3306", key="Port")
    st.text_input("User", value="root", key="User")
    st.text_input("Password", type="password", value="bhushankiran.1", key="Password")
    st.text_input("Database", value="chinook", key="Database")
    if st.button('connect'):
        with st.spinner('Connecting to database...'):
            db = init_database(
                st.session_state["User"],
                st.session_state["Password"],
                st.session_state["Host"],
                st.session_state["Port"],
                st.session_state["Database"]
                )
            st.session_state.db = db
            st.success('Connected to database')




            
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.markdown(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)
            
    
user_query = st.chat_input('write your message here..')
if user_query is not None and user_query.strip() != '':
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    
    with st.chat_message("Human"):
        st.markdown(user_query) 
    
    with st.chat_message("AI"):
        response = "I dont know how to respond"
        st.markdown(response)
        
    st.session_state.chat_history.append(AIMessage(content=response))
        
        
