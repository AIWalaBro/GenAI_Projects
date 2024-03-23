# from fastapi import FastAPI

# # from langchain.chat_models import ChatOpenAI
# # from langchain_community.chat_models import ChatOpenAI

# from langchain_openai import ChatOpenAI
# # from langchain.prompts import ChatPromptTemplate
# from langchain_core.prompts import ChatPromptTemplate
# import uvicorn
# from langserve import add_routes
# import os
# from dotenv import load_dotenv
# load_dotenv()

from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
# from langchain.chat_models import ChatOpenAI
# from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"

)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

model=ChatOpenAI()
prompt=ChatPromptTemplate.from_template("provide me an essay about {topic}")
prompt1=ChatPromptTemplate.from_template("provide me a poem about {topic}")

add_routes(
    app,
    prompt|model,
    path="/essay"

)

add_routes(
    app,
    prompt1|model,
    path="/poem"

)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)