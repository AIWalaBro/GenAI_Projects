import streamlit as st
from langchain_community.utilities import SQLDatabase
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()


# connect the database to connect button
def init_database(user:str, password:str, host:str, port:str, database:str) -> SQLDatabase:
    # db_uri = f"mysql+mysqlconnector://{user}{password}@{host}{port}/{databse}"
    db_uri = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
    return SQLDatabase.from_uri(db_uri)

# creating the few shot prompt template to prevent from haluusination , just like here is the 
# example here, here is your answer and need only answer
def get_sql_chain(db):
    template = """
        You are a data analyst at a company. You are interacting with a user who is asking you questions about the company's database.
        Based on the table schema below, write a SQL query that would answer the user's question. Take the conversation history into account.
        
        <SCHEMA>{schema}</SCHEMA>
        
        Conversation History: {chat_history}
        
        Write only the SQL query and nothing else. Do not wrap the SQL query in any other text, not even backticks.
        
        For example:
        Question: which 3 artists have the most tracks?
        SQL Query: SELECT ArtistId, COUNT(*) as track_count FROM Track GROUP BY ArtistId ORDER BY track_count DESC LIMIT 3;
        Question: Name 10 artists
        SQL Query: SELECT Name FROM Artist LIMIT 10;
        
        Your turn:
        
        Question: {question}
        SQL Query:
        """
    
    prompt = ChatPromptTemplate.from_template(template)
    # llm = ChatOpenAI(model="gpt-4-0125-preview")
    llm = ChatGroq(model="mixtral-8x7b-32768", temperature=0)
    # llm = ChatOpenAI(model = "gpt-3.5-turbo")

    def get_schema(_):
        return db.get_table_info()
    
    return (
        RunnablePassthrough.assign(schema = get_schema)
        | prompt 
        | llm
        | StrOutputParser()
        
        # this chain taking as an input the question, chat_history not schema
        # beacuse we already have schema right here in runnablepassthorugh
    )
    
    
def get_response(user_query: str, db: SQLDatabase, chat_history: list):
    sql_chain = get_sql_chain(db)
    template = """
        You are a data analyst at a company. You are interacting with a user who is asking you questions about the company's database.
        Based on the table schema below, question, sql query, and sql response, write a natural language response.
        <SCHEMA>{schema}</SCHEMA>

        Conversation History: {chat_history}
        SQL Query: <SQL>{query}</SQL>
        User question: {question}
        SQL Response: {response}"""
    prompt = ChatPromptTemplate.from_template(template)
    
    # llm = ChatOpenAI(model="gpt-4-0125-preview")
    llm = ChatGroq(model="mixtral-8x7b-32768", temperature=0)
    # llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    chain = (
        RunnablePassthrough.assign(query = sql_chain).assign(
            schema = lambda _: db.get_table_info(),
            response = lambda vars : db.run(vars['query']),
        )
        | prompt
        | llm
        | StrOutputParser()
    )
    
    return chain.invoke({
        "question" : user_query,
        "chat_history" : chat_history,
    })
    
#     chain = (
#     RunnablePassthrough.assign(query=sql_chain).assign(
#       schema=lambda _: db.get_table_info(),
#       response=lambda vars: db.run(vars["query"]),
#     )
#     | prompt
#     | llm
#     | StrOutputParser()
#   )


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
    # this is for to check the chain workings
    with st.chat_message("AI"):
        sql_chain = get_sql_chain(st.session_state.db)
        response = get_response(user_query, st.session_state.db, st.session_state.chat_history)
        st.markdown(response)
        
        
            # response = sql_chain.invoke(
            #     {
            #         "chat_history": st.session_state.chat_history,
            #         "question": user_query
            #     }
            # )
            
            # Instead of calling like directly we will created production ready
            #  response = get_response(user_query, st.session_state.db, st.session_state.chat_history)

        
    st.session_state.chat_history.append(AIMessage(content=response))
        
        
